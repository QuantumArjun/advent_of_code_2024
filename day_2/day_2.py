'''
Advent of Code Day 2
author: akaranam

This solution checks reports for safety based on two rules:
1. Numbers must be all increasing or all decreasing
2. Adjacent numbers must differ by 1-3
'''

def read_reports(file_name):
    """
    Processes the input file and returns two lists of integers.
    :param file_name: Name of the input file.
    :return: An array of arrays
    """
    report_list = []
    with open(file_name, 'r') as f:
        for line in f:
            # Convert each line to a list of integers
            report_list.append([int(x) for x in line.strip().split()])
    return report_list

def is_safe_report(report, use_dampener=False):
    """
    Check if a report is safe based on the rules:
    1. Numbers must be all increasing or all decreasing
    2. Adjacent numbers must differ by 1-3
    
    With Problem Dampener (use_dampener=True), a report is safe if removing
    any single number would make it safe.
    
    Args:
        report (list): List of integers representing the report
        use_dampener (bool): Whether to use the Problem Dampener
    Returns:
        bool: True if the report is safe, False otherwise
    """
    def is_valid_sequence(nums):
        if len(nums) < 2:
            return True
            
        is_increasing = None
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i-1]
            
            # First determine if sequence is increasing or decreasing
            if is_increasing is None:
                is_increasing = diff > 0
            
            # Check if direction matches and difference is within bounds
            if (diff > 0) != is_increasing:
                return False
            if abs(diff) < 1 or abs(diff) > 3:
                return False
        return True
    
    # First check if the sequence is valid without dampener
    if is_valid_sequence(report):
        return True
        
    # If dampener is enabled and sequence is invalid, try removing each number
    if use_dampener:
        for i in range(len(report)):
            # Create new list without the i-th element
            dampened_report = report[:i] + report[i+1:]
            if is_valid_sequence(dampened_report):
                return True
                
    return False


if __name__ == '__main__':
    report_list = read_reports("day_2_input.txt")
    
    # Part 1: Without Problem Dampener
    safe_count = sum(1 for report in report_list if is_safe_report(report))
    print(f"Part 1 - Number of safe reports: {safe_count}")
    
    # Part 2: With Problem Dampener
    safe_count_dampened = sum(1 for report in report_list if is_safe_report(report, use_dampener=True))
    print(f"Part 2 - Number of safe reports with dampener: {safe_count_dampened}")