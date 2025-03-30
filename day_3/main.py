'''
Advent of Code Day 3
author: akaranam

This solution checks reports uncorrupted multiplication via regex. Part 2 extends this to check for do and don't flags
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
    

def check_for_corrupted(inputDoc):
    sum = 0
    regexSearch = re.findall(r"mul\(\d{1,3},\d{1,3}\)", inputDoc)
    for instruction in regexSearch:
        sum += instruction_to_number(instruction)
    print("Part 1", sum)
    

def mul_check(inputDoc, index):
    result = ""
    start = index
    if inputDoc[index:index+4] != 'mul(': 
        return (False, result)

    index += 4 # skip 'mul('
    num_digits = 0
    while inputDoc[index] != ',':
        if num_digits == 3 or not inputDoc[index].isdigit():
            return (False, result)
        index += 1
        num_digits += 1

    index += 1 # skip ','
    num_digits = 0
    while inputDoc[index] != ')':
        if num_digits == 3 or not inputDoc[index].isdigit():
            return (False, result)
        index += 1
        num_digits += 1

    result = inputDoc[start:index+1]
    return (True, result)


# Optimization; If the current flag is don't, then you can just skip ahead to the next do; Preprocess by extracting chunks of do

def manual_check_for_corrupted(inputDoc):
    instruction_list = []
    current_flag = True
    for count, i in enumerate(inputDoc):
        if i == 'd':
            if inputDoc[count:count+4] == "do()":
                current_flag = True
            elif inputDoc[count:count+7] == "don't()":
                current_flag = False
        if i == 'm': 
            (is_valid, result) = mul_check(inputDoc, count)
            if is_valid and current_flag:
                instruction_list.append(result)
    
    sum = 0 
    for instruction in instruction_list:
        sum += instruction_to_number(instruction)
    
    print("Part 2", sum)
    
    
if __name__ == '__main__':
    inputDoc = read_file()
    
    check_for_corrupted(inputDoc)
    
    # For part 2, we'll have to write a manual search, because we need to also manually check for the flags
    manual_check_for_corrupted(inputDoc)