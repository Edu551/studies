import re

regex = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

def string_filter(s: str) -> int:
    matches = regex.findall(s)
    # print(matches)
    return sum(int(a) * int(b) for a, b in matches)

with open("eg_03.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(string_filter(content))