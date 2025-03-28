safe_reports = 0
add = None

def compare(nums: list[int]) -> bool:
    global add
    if add is None:
        add = nums[0] < nums[1]

    if nums[0] == nums[1]:
        return False
    
    if len(nums) > 2:
        if nums[0] < nums[1] and add and abs(nums[0] - nums[1]) <= 3:
            return compare(nums[1:])
        elif nums[0] > nums[1] and add == False and abs(nums[0] - nums[1]) <= 3:
            return compare(nums[1:])
        else:
            return False
    else:
        if nums[0] < nums[1] and add and abs(nums[0] - nums[1]) <= 3:
            return True
        elif nums[0] > nums[1] and add == False and abs(nums[0] - nums[1]) <= 3:
            return True
        else:
            return False

with open("input_02.txt", "r", encoding="utf-8") as file:
    for line in file:
        list_str = line.split()
        list_int = [int(i) for i in list_str]
        comp = compare(list_int)
        if comp:
            safe_reports += 1
        add = None


print("safe_reports: ", safe_reports)