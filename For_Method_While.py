my_list = ['a','b','c']
my_list2 = [1,65,2,3,854]

i = 0
while i < len(my_list):
    print my_list[i]
    i = i+1

for i in range(len(my_list)):
    print my_list[i]

for i in my_list:
    print i

def jack(a_list):
    for i in range(len(a_list)):
        print a_list[i]

def jack2(a_list):
    for i in a_list:
        print i

def jack3(b_list):
    sum = 0
    for i in range(len(b_list)):
        sum = sum + b_list[i]
    return sum

def jack4(b_list):
    sum = 0
    for i in b_list:
        sum = sum + i
    return sum

jack(my_list)
jack2(my_list)
print jack3(my_list2)
print jack4(my_list2)


