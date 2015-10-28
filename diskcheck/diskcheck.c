

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <errno.h>
#include <assert.h>
#include <sys/stat.h>
#include <stdint.h>


// ELEMENT_T is governed by the type returned by random()
#define ELEMENT_T long int
#define BUFFER_SIZE ((size_t)(1024*1024))
#define BUFFER_ELEMENTS ( BUFFER_SIZE / sizeof(ELEMENT_T) )


static ELEMENT_T buffer[BUFFER_ELEMENTS];
static ELEMENT_T expected[BUFFER_ELEMENTS];

static void print_progress(size_t bytes, size_t remaining);


/* Write random data to file.  This relies on random() being in the
 * correct state when this function is called. */
static void write(FILE *f, size_t bytes_to_write) {

  size_t i;
  size_t elements_written;
  size_t elements_to_write;

  assert(bytes_to_write <= BUFFER_SIZE);
  assert(bytes_to_write % sizeof(ELEMENT_T) == 0);

  elements_to_write = bytes_to_write / sizeof(ELEMENT_T);

  for (i=0; i<elements_to_write; i++) {
    buffer[i] = random();
  }

  elements_written = fwrite(&buffer, sizeof(ELEMENT_T), elements_to_write, f);
  if (elements_to_write != elements_written) {
    perror("Write to DEVICE failed");
    exit(1);
  }
}


/* Verifies what's read back from disk is correct.  verify relies on
 * random() being in the correct state when this function is called.
 *
 * Returns non-zero on failure, and sets failed_on_byte to the index into the
 * block the failure occurred */
static int verify(FILE *f, size_t count, size_t *failed_on_byte) {

  size_t i;
  size_t n;
  assert(count<=BUFFER_SIZE);
  assert(count % sizeof(buffer[0]) == 0);
  assert(failed_on_byte != NULL);

  count = count / sizeof(buffer[0]);

  /* Re-generate the random sequence */
  for (i=0; i<count; i++) {
    expected[i] = random();
  }

  /* Re-read the file */

  n = fread(&buffer, sizeof(buffer[0]), count, f);
  if (n != count) {
    fprintf(stderr, "Failed to read from file.\n");
    exit(errno);
  }

  /* Verify the file against the sequence */

  for (i=0; i<count; i++) {
    if (i == 10200000) {
      expected[i]++;
    }
    if (expected[i] != buffer[i]) {
      //print_progress(sizeof(expected), i);
      *failed_on_byte = i * (int)sizeof(buffer[0]);
      return 1;
    }
  }

  return 0;
}


static size_t progress;

static void print_progress(size_t bytes, size_t remaining) {

  while((((bytes - remaining) * 40) / bytes) > progress) {
    printf(".");
    fflush(stdout);
    progress++;
  }
}


/* Performs a single write/verify cycle.  Returns 0 on success, or 1 on
 * failure, failbyte to the index of the byte on which failed */

static int write_cycle(const char *path, time_t seed, size_t bytes, size_t *failbyte) {

  int r = 0;
  time_t start;
  FILE *f = NULL;
  size_t remaining;

  /* Set seed and write a random sequence to the file */

  srandom((unsigned int)seed);  // truncating seed

  f = fopen(path, "w");
  if (f == NULL) {
    perror("Unable to open DEVICE for write");
    exit(errno);
  }

  progress = 0;

  printf("  Write:   ");
  fflush(stdout);

  start = time(NULL);

  remaining = bytes;
  while (remaining > 0) {
    if (remaining > BUFFER_SIZE) {
      write(f, BUFFER_SIZE);
      remaining -= BUFFER_SIZE;
    } else {
      write(f, remaining);
      remaining = 0;
    }
    print_progress(bytes, remaining);
  }

  printf(" %d seconds\n", (int)(time(NULL) - start));

  fclose(f);

  /* Reset seed, re-read data from file descriptor and verify */

  srandom((unsigned int)seed);

  f = fopen(path, "r");
  if (f == NULL) {
    perror("Unable to open DEVICE for read");
    exit(errno);
  }

  progress = 0;

  printf("  Verify:  ");
  fflush(stdout);

  start = time(NULL);

  remaining = bytes;
  while (remaining > 0) {

    size_t chunk;
    size_t chunk_failbyte;

    chunk = (remaining > BUFFER_SIZE) ? BUFFER_SIZE : remaining;

    if (verify(f, chunk, &chunk_failbyte)) {
      *failbyte = (bytes - remaining) + chunk_failbyte;
      r = 1;
      goto failend;
    }

    remaining -= chunk;
    print_progress(bytes, remaining);
  }

  r = 0;
  printf(" %d seconds\n", (int)(time(NULL) - start));

  *failbyte = 0;

failend:

  if (f) fclose(f);

  return r;
}


int main(int argc, const char** argv) {

  time_t seed;
  struct stat st;
  const char *path;
  int i;
  int iterations;
  size_t bytes;
  double pretty;
  int failed = 0;
  size_t failbyte = 0;

  seed = time(NULL);

  /* Yes, I'd have loved to use NFOPT.  However, this doesn't have a real home
   * from which to nc_find cutils.  It can stay wishlist for now. */

  if (argc != 4) {
    fprintf(stderr, "Usage: diskcheck ITERATIONS DEVICE BYTES\n\n" \
                    "  ITERATIONS  Number of iterations; negative for infinite\n" \
                    "  DEVICE      e.g. /dev/sdb\n" \
                    "  BYTES       Number of bytes to write (from fdisk -l /dev/sdb)\n\n" \
                    "USE THIS UTILITY WITH CARE.  This will need to be run as root.\n" \
                    "I've already overwritten my bootsector once.\n");
    return 1;
  }

  if (sscanf(argv[1], "%d", &iterations) != 1) {
    fprintf(stderr, "Unable to parse an int from ITERATIONS.\n");
    return 1;
  }

  path = argv[2];

  /* Check file descriptor */

  if (stat(path, &st)) {
    perror("Unable to stat DEVICE");
    return errno;
  }

  /* Get disk geometry */

    /* IWBNI - Using hdparm as an example, it's not perfectly
     * straightforward. */

  if (1 != sscanf(argv[3], "%zu", &bytes)) {
    fprintf(stderr, "Unable to parse a size_t from BYTES.\n");
    return 1;
  }

  if (bytes % sizeof(ELEMENT_T)) {
    fprintf(stderr, "BYTES should be a multiple of 4 bytes.\n");
    return 1;
  }

  /* Report my brief */

  pretty = bytes;
  const char *hread[4] = {"bytes", "KB", "MB", "GB"};
  int suf = 0;
  while (pretty>=1000 || suf>4) {
    pretty = pretty / 1024;
    suf++;
  }

  printf("\n  Verifying:   %s\n", path);
  printf("  Bytes:       %zu (%4.2lf %s)\n", bytes, pretty, hread[suf]);
  printf("  Iterations:  %d %s\n", iterations, (iterations<0) ? "(infinite)" : "");
  printf("  Started:     %s\n", ctime(&seed));

  printf("        0%% |                                      | 100%%\n");

  i = iterations;

  while (i !=0 ) {

    if (write_cycle(path, seed, bytes, &failbyte)) {
      printf("FAIL (%zu/%zu)\n", failbyte, bytes);
      failed++;
    }

    if (i > 0) i--;
  }

  if (failed) {
    printf("\nFAILS (%d/%d)\n", failed, iterations);
    return 1;
  } else {
    printf("\nSUCCESS\n");
    return 0;
  }
}
