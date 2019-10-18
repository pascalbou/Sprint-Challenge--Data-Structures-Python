import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

# this solution is n * n, very slow
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# Final solution
# create 26 lists for each of letter in alphabet
# loop through names_1 and append name according to its first letter
# loop through names_2 and only search in the array with the same first letter
# compute time is around 1/10th of a second

all_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
all_names1 = {letter: [] for letter in all_letters}
for name_1 in names_1:
    first_letter = name_1[0].lower()
    all_names1[first_letter].append(name_1)
# print(all_names1)

for name_2 in names_2:
    first_letter = name_2[0].lower()
    if name_2 in all_names1[name_2[0].lower()]:
        duplicates.append(name_2)

# first solution
# try hash table
# each array contains 26 letters
# loop all names in names1 and at first letter of name, add to first array, etc until end of name
# loop names 2 and stop if letter of name is not in array else if iteration of name2 is complete append the name in duplicate

# second solution
# use singly linked list
# a node contains
    # value equals letter
    # next is list of node
# loop through all names in names1 and create a list of singly linked list
# loop through names2 and check if it exists in the first list

# class ListNode:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = []

#     def insert_letter(self, value):
#         self.next.append(ListNode(value))

# all_names = []

# for name_1 in names_1:
#     all_names.append(ListNode(name_1[0]))
#     for i in range(1, len(name_1)):
#         if name_1[i-1] in all_names

# print(all_names)

# third solution
# use hash function
    # return int according to first letter of name
    # example A returns 0, B returns 1
    # do the same for last name
# create 26 lists for each letter
# loop through names2, should be faster than looping through whole names1 list

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

