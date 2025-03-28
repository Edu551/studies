left_list = []
right_list = []
right_counts = {}

with open("input_01.txt", "r", encoding="utf-8") as file:
    for line in file:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)

        if right in right_counts:
            right_counts[right] += 1
        else:
            right_counts[right] = 1

sim_score = 0
for left in left_list:
    count = right_counts[left] if left in right_counts else 0
    sim_score += left * count

print("similarity score: ", sim_score)



"""
Using external lib
from collections import Counter

left_list = []
right_list = []

with open("input_01.txt", "r", encoding="utf-8") as file:
    for line in file:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)

right_counts = Counter(right_list)

sim_score = sum(left * right_counts.get(left, 0) for left in left_list)"
print("similarity score: ", sim_score)
"""