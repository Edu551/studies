left_list = []
right_list = []

with open("input_01.txt", "r", encoding="utf-8") as file:
    for line in file:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)

left_list.sort()
right_list.sort()

dist = 0

for i in range(len(left_list)):
    left = left_list[i]
    right = right_list[i]
    diff = abs(left - right)
    dist += diff

print("dist: ", dist)
