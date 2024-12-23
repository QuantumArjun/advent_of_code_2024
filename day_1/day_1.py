'''
Advent of Code Day 1
author: akaranam
'''

from collections import Counter
from typing import List, Tuple

# Optional 1: Write the sort function myself 

def process_input() -> Tuple[List[int], List[int]]:
    """
    Processes the input file and returns two lists of integers.
    :param file_name: Name of the input file.
    :return: A tuple of two integer lists.
    """
    # First, read in the input file
    array1, array2 = [], []
    
    with open('day_1_input.txt', 'r') as file:
        for line in file: 
            values = line.split()
            array1.append(int(values[0]))
            array2.append(int(values[1]))
    
    return array1, array2

def list_difference(array1, array2):   
    """
    Calculate the element-wise absolute difference between two lists.
    :param array1: First list of integers.
    :param array2: Second list of integers.
    :return: Total difference.
    """
    # Second, sort each array from smallest to largest 
    array1.sort()
    array2.sort()
    
    # Third, calculate element wise difference between the two arrays
    difference = sum(abs(a - b) for a, b in zip(array1, array2))
        
    print("Difference between two lists", difference)

def similarity_score(array1, array2):
    """
    Calculate a similarity score based on value frequencies in the second list.
    :param array1: First list of integers.
    :param array2: Second list of integers.
    :return: Similarity score.
    """
    
    similarity_score = 0
    frequencyDict = Counter(array2)
    similarity_score = sum(value * frequencyDict.get(value, 0) for value in array1)
    print("This is the similarity score", similarity_score)

if __name__ == '__main__':
    array1, array2 = process_input()
    list_difference(array1, array2)
    similarity_score(array1, array2)
    