#!/usr/bin/python3

# part 1
with open('day3.txt', 'r') as f:
    lines = f.readlines()
    rucksacks = [entry.strip() for entry in lines]
    sum = 0
    for rucksack in rucksacks:
        # split the rucksacks in half
        compartment1 = set(rucksack[:len(rucksack)//2])
        compartment2 = set(rucksack[len(rucksack)//2:])
        #get the overlappin character
        overlap = (compartment1.intersection(compartment2)).pop()

        #translate the overlapping character to ascii and subtract the pase
        if overlap.isupper():
            sum += ord(overlap) - ord('A') + 27
        else:
            sum += ord(overlap) - ord('a') + 1
print("Part 1: {}".format(sum))
f.close()

# part 2
with open('day3.txt', 'r') as f:
    lines = f.readlines()
    rucksacks = [entry.strip() for entry in lines]
    sum = 0
    while len(rucksacks) > 0:
        first_rucksack = set(rucksacks.pop())
        second_rucksack = set(rucksacks.pop())
        third_rucksack = set(rucksacks.pop())
        overlap = (first_rucksack.intersection(second_rucksack).intersection(third_rucksack)).pop()

        #translate the overlapping character to ascii and subtract the pase
        if overlap.isupper():
            sum += ord(overlap) - ord('A') + 27
        else:
            sum += ord(overlap) - ord('a') + 1
print("Part 2: {}".format(sum))
