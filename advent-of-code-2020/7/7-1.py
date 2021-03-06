#!/usr/bin/python3


import re

rule_re = re.compile('^(?P<colour>[a-z]+ [a-z]+) bags contain (?P<contents>[0-9a-z, ]+)[.]$')
inner_bag_re = re.compile('^(?P<count>[0-9]+) (?P<colour>[a-z]+ [a-z]+) bag[s]?$')

with open('data.txt') as file:
    rules = file.read().splitlines()


# Process data into a dict { colour: [(colour, number), ...]

rules_dict = {}

for rule in rules:
    rule_match = rule_re.match(rule)
    assert(rule_match)
    
    colour = rule_match['colour']
    assert(not colour in rules_dict)

    inner_bags = set()

    contents = rule_match['contents']
    if contents != 'no other bags':    
        contents_list = contents.split(', ')
        for contents in contents_list:
            inner_bag_match = inner_bag_re.match(contents)
            assert(inner_bag_match)
            inner_bags.add(inner_bag_match['colour'])

    rules_dict[colour] = inner_bags
    
# Search for "shiny gold"

class FoundException(Exception):
    pass

colours_that_can_contain = []

def traverse(bag):
    if bag == 'shiny gold':
        raise FoundException()
    else:
        for inner_bag in rules_dict[bag]:
            traverse(inner_bag)

for start_bag in rules_dict:
    if start_bag == 'shiny gold':
        continue
    try:
        traverse(start_bag)
    except FoundException:
        colours_that_can_contain.append(start_bag)

print(colours_that_can_contain)
print(len(colours_that_can_contain))


