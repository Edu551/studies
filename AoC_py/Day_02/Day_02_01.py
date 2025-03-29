safe_reports = 0

def compare(nums: list[int], add: bool = None) -> bool:
    if len(nums) < 2:
        return True
    
    if add is None:
        add = nums[0] < nums[1]

    if abs(nums[0] - nums[1]) > 3 or nums[0] == nums[1]:
        return False
    
    return compare(nums[1:], add) if (nums[0] < nums[1]) == add else False

with open("input_02.txt", "r", encoding="utf-8") as file:
    for line in file:
        list_int = [int(i) for i in line.split()]
        if compare(list_int):
            safe_reports += 1


print("safe_reports: ", safe_reports)