from queue import PriorityQueue
import string

q = PriorityQueue()
myfile = ""
with open("input3.txt", "r") as f:
    myfile = f.read().strip()

myfile_list = myfile.split("\n")

alphabet_lower = list(string.ascii_lowercase)
alphabet_upper = list(string.ascii_uppercase)


def totality(mylist):
    total = 0
    loca = 0
    for line in mylist:
        for letter in line:
            if letter in alphabet_lower:
                loca = alphabet_lower.index(letter)
                # Account for index
                loca += 1
            elif letter in alphabet_upper:
                loca = alphabet_upper.index(letter)
                loca += 27
            total = total + loca
    print(total)


def all_three(badges: list):
    common = []
    for badge in badges:
        common.append(list(set.intersection(*map(set, badge))))
    totality(common)


def divide_list():
    step = 3
    end = len(myfile_list)
    start = 0
    temp = []
    for i in range(start, end, step):
        x = i
        temp.append(myfile_list[x : x + step])

    return temp


all_three(divide_list())
