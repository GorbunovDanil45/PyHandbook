best_line: str = ""
target: str = "зайка"

line1: str = input()
if target in line1:
    best_line = line1

line2: str = input()
if target in line2:
    if best_line == "" or line2 < best_line:
        best_line = line2

line3: str = input()
if target in line3:
    if best_line == "" or line3 < best_line:
        best_line = line3

print(best_line, len(best_line))
