
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



def how_many_unique_letters(group):
    unique_letters = set()
    for person in group:
        for letter in person:
            unique_letters.add(letter)

    return len(unique_letters)

total = 0
for group in groups:
    print(group)
    unique_letters = how_many_unique_letters(group)
    total += unique_letters

print(total)

