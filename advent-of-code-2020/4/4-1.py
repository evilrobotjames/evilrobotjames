#!/usr/bin/python3

def ignoring(field, value):
    print('ignoring {0}: {1}'.format(field, value))


class Passport():
    def __init__(self):
        self.data = {}

    def add(self, field, value):
#        if field == 'byr':
#            if not (int(value) >= 1920 and int(value) <= 2002):
#                ignoring(field, value)
#                return
#        if field == 'iyr':
#            if not (int(value) >= 2010 and int(value) <= 2020):
#                ignoring(field, value)
#                return
        self.data[field] = value


    def is_valid(self):
        req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
        for r in req_fields:
            if r not in self.data.keys():
                return False  
        return True


with open('data.txt') as f:
    lines = f.read().splitlines()

# process

passports = []

passport = Passport()
passports.append(passport)

for line in lines:
    print(line)
    if line == '':
        passport = Passport()
        passports.append(passport)
        continue
    
    fields = line.split()
    for f in fields:
        passport.add(f[:3], f[4:])
        
valid_count = 0
for p in passports:
    if p.is_valid():
        valid_count += 1


print(valid_count)


