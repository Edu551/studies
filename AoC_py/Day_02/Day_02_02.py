safe_reports = 0

def compare(nums: list[int]) -> bool:
    if len(nums) < 2:
        return True

    increasing = None

    for i in range(len(nums) - 1):
        diff = nums[i + 1] - nums[i]

        if abs(diff) > 3 or diff == 0:
            return False
        
        if increasing is None:
            increasing = diff > 0
        elif (diff > 0) != increasing:
            return False
        
    return True

def can_be_made_safe(nums: list[int]) -> bool:
    for i in range(len(nums)):
        new_nums = nums[:i] + nums[i+1:]
        if compare(new_nums):
            return True
    return False

with open("input_02.txt", "r", encoding="utf-8") as file:
    for line in file:
        list_int = [int(i) for i in line.split()]
        
        if compare(list_int) or can_be_made_safe(list_int):
            safe_reports += 1



print("safe_reports: ", safe_reports)