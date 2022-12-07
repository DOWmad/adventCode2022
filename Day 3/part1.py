from queue import PriorityQueue
import string

q = PriorityQueue()
myfile = ""
with open("input3.txt", "r") as f:
    myfile = f.read().strip()

myfile_list = myfile.split("\n")

alphabet_lower = list(string.ascii_lowercase)
alphabet_upper = list(string.ascii_uppercase)

total = 0
loca = 0
for line in myfile_list:
    common = []
    first, second = line[: len(line) // 2], line[len(line) // 2 :]
    first_list = list(first)
    print(f"Checking {first_list}")
    for letter in first_list:
        if letter in second:
            common.append(letter)
            common = list(set(common))
    for letter in common:
        if letter in alphabet_lower:
            loca = alphabet_lower.index(letter)
            # Account for index
            loca += 1
        elif letter in alphabet_upper:
            loca = alphabet_upper.index(letter)
            loca += 27
        total = total + loca
print(total)
