
# 6711 too low

with open('data.txt') as f:
    data = f.read().splitlines()

groups = []
group = []
groups.append(group)

for person in data:
    if person == '':
        group = []
        groups.append(group)
        continue

    group.append(person)


def get_unique_letters(group):
    unique_letters = set()
    for person in group:
        for letter in person:
            unique_letters.add(letter)
    return unique_letters

def letters_in_every_person(group):
    letters_to_try = get_unique_letters(group)
    letters_in_all = set(letters_to_try)
    for letter in letters_to_try:
        for person in group:
            if letter not in person:
                if letter in letters_in_all:
                    letters_in_all.remove(letter)
    return letters_in_all

total = 0
for group in groups:
    total += len(letters_in_every_person(group))

print(total)