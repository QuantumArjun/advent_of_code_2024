'''
Advent of Code Day 3
author: akaranam

This solution checks reports uncorrupted multiplication via regex
'''

import re

def read_file():
    inputDoc = None
    with open('input.txt', 'r') as f:
        inputDoc = f.read()
    return inputDoc

def instruction_to_number(instruction: str) -> int:
    match = re.search(r"mul\((\d{1,3}),(\d{1,3})\)", instruction)

    if match:
        a = int(match.group(1))  # '5' → 5
        b = int(match.group(2))  # '7' → 7
        return a * b

    print("Malformed instruction")
    return 0

    
    

def check_for_corrupted():
    inputDoc = read_file()
    regexSearch = re.findall(r"mul\(\d{1,3},\d{1,3}\)", inputDoc)
    
    sum = 0
    for instruction in regexSearch:
        sum += instruction_to_number(instruction)
    print(sum)

if __name__ == '__main__':
    check_for_corrupted()
    