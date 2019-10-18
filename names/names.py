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

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

