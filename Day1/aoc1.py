elves=""
elves_list=[]
with open("input.txt", encoding='utf-8') as f:
    elves=f.read()

elves_list=elves.split('\n')

total=0
maxi=0
for elf in elves_list:
    if elf == '':
        if total > maxi:
            maxi=total
        total=0
    else:
        total=total+float(elf)

print(maxi)
