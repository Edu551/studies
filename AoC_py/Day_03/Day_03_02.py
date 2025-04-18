import re

regex = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|don't\(\)|do\(\)")

def string_filter(s: str) -> int:
    is_to_sum = True
    res = 0

    for match in regex.finditer(s):
        if match.group() == "don't()":
            is_to_sum = False
        elif match.group() == "do()":
            is_to_sum = True
        elif is_to_sum:
            x, y = match.groups()
            res += int(x) * int(y)

    return res

with open("input_03.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(string_filter(content))