#!/usr/bin/python3


import re

rule_re = re.compile('^(?P<colour>[a-z]+ [a-z]+) bags contain (?P<contents>[0-9a-z, ]+)[.]$')
inner_bag_re = re.compile('^(?P<count>[0-9]+) (?P<colour>[a-z]+ [a-z]+) bag[s]?$')

with open('data.txt') as file:
    rules = file.read().splitlines()

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
    
print(rules_dict)
