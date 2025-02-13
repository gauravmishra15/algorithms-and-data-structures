def oddNumbers(l, r):
    # Write your code here

    # define return Array
    a = []
    first_element = 0
    last_element = 0
    # is l an add number
    if l % 2 == 0:
        first_element = l + 1
    else:
        first_element = l

    # is r an odd number
    if r % 2 == 0:
        last_element = r - 1
    else:
        last_element = r

    # list all odd numbers between l and r
    i = first_element

    while i <= last_element:
        a.append(i)
        i += 2
    return a

print(oddNumbers(2, 50))