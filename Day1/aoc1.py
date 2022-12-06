elves=""
elves_list=[]
with open("input.txt", encoding='utf-8') as f:
    elves=f.read()

elves_list=elves.split('\n')

# Part 1
total=0
maximum=0
for elf in elves_list:
    if elf == '':
        if total > maximum:
            maximum=total
        total=0
    else:
        total=total+float(elf)

print(maximum)

# part 2
for elf in elves_list:
    if elf == "":
        if total > maximum:
            third_max = second_max
            second_max = maximum
            maximum = total
        elif total > second_max:
            second_max = total
        elif total > third_max:
            third_max = total
        total = 0
    else:
        total = total + float(elf)

print(maximum + second_max + third_max)