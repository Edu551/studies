safe_reports = 0
index = None

def compare(nums: list[int]) -> bool:
    global index
    if len(nums) < 2:
        return True

    add = None

    for i in range(len(nums) - 1):
        diff = nums[i + 1] - nums[i]

        if abs(diff) > 3 or diff == 0:
            if index is None:
                index = i
            return False
        
        if add is None:
            add = diff > 0
        elif (diff > 0) != add:
            if index is None:
                index = i
            return False
        
    return True

with open("input_02.txt", "r", encoding="utf-8") as file:
    for line in file:
        list_int = [int(i) for i in line.split()]
        comp = compare(list_int)

        if not comp:
            if index > 0:
                comp = compare([n for idx, n in enumerate(list_int) if idx != index - 1])

            if index >= 0 and not comp:
                comp = compare([n for idx, n in enumerate(list_int) if idx != index])

            if index < len(list_int) - 1 and not comp:
                comp = compare([n for idx, n in enumerate(list_int) if idx != index + 1])

        if comp:
            safe_reports += 1
        index = None



print("safe_reports: ", safe_reports)