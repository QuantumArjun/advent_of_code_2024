

def process_input():
    # First, read in the input file
    array1 = []
    array2 = []
    
    with open('day_1_input.txt', 'r') as file:
        for line in file: 
            values = line.split()
            array1.append(int(values[0]))
            array2.append(int(values[1]))
    
    return array1, array2

def list_difference(array1, array2):    
    # Second, sort each array from smallest to largest 
    array1.sort()
    array2.sort()
    
    # Third, calculate element wise difference between the two arrays
    difference = 0 
    for i in range (0, len(array1)):
        difference += abs(array1[i] - array2[i])
        
    print("Difference between two lists", difference)
        
    # Optional 1: Write the sort function myself 
    
    # Optional 2: Ask Claude or something for the more efficient way to do this 

def similarity_score(array1, array2):
    similarity_score = 0
    frequencyDict = getCounts(array2)
    for i in range(0, len(array1)):
        currValue = array1[i]
        if currValue in frequencyDict:
            similarity_score += currValue * frequencyDict[currValue]
    print("This is the similarity score", similarity_score)
        
def getCounts(array2): 
    countDict = {}
    
    for i in range (0, len(array2)):
        currValue = array2[i]
        if currValue in countDict:
            countDict[currValue] += 1 
        else: 
            countDict[currValue] = 1
    
    return countDict
if __name__ == '__main__':
    array1, array2 = process_input()
    list_difference(array1, array2)
    similarity_score(array1, array2)
    