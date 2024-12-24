'''
Advent of Code Day 2
author: akaranam
'''

def read_reports(file_name):
    """
    Processes the input file and returns two lists of integers.
    :param file_name: Name of the input file.
    :return: An array of arrays
    """
    # First, read in the input file
    report_list = []
    
    with open(file_name, 'r') as file:
        for line in file:
            report = line.split()
            report_list.append(report)
            
    return report_list

def safety_check(report_list): 
    num_safe = 0
    for report in report_list:
        if check_single_report(report):
            num_safe += 1
    
    return num_safe

def within_bounds(num1, num2, increasing):
    if increasing: 
        upper_bound = (num1 + 1, num1 + 3)
        if num2 >= upper_bound[0] and num2 <= upper_bound[1]:
            return True 
        else: 
            return False
    
    else: 
        lower_bound = (num1 - 1, num1 - 3)
        if num2 <= lower_bound[0] and num2 >= lower_bound[1]:
            return True 
        else:
            return False
        
def check_single_report(report):
    
    # Deal with special cases 
    if len(report) == 1:
        return True 
    
    # If we get here, we know if is at least 2 long, and can establish the direction
    increasing = True
    if int(report[1]) < int(report[0]):
        increasing = False
    
    # Now iterate through and see if the rules are violated 
        
    prev_result = None
    for result in report:
        if prev_result != None:
            if not within_bounds(int(prev_result), int(result), increasing):
                return False
        prev_result = result
    
    return True   


if __name__ == '__main__':
    report_list = read_reports("day_2_input.txt")
    print(report_list[0])
    num_safe = safety_check(report_list)
    print(num_safe)
    