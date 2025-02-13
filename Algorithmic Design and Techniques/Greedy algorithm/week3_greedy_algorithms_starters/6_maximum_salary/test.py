#a = ["28", "2"]
#[54, 546, 548, 60]

# Python3 implementation this is to use itertools.
# permutations as coded below:
def largestNumber(array):
    # extval is a empty list for extended
    # values and ans for calculating answer
    extval, ans = [], ""

    # calculating the length of largest number
    # from given and add 1 for further operation
    l = len(str(max(array))) + 1

    # iterate given values and
    # calculating extended values
    for i in array:
        temp = str(i) * l

        # make tuple of extended value and
        # equivalant original value then
        # append to list
        extval.append((temp[:l:], i))

        # sort extval in descending order
    extval.sort(reverse=True)

    # iterate extended values
    for i in extval:
        # concatinate original value equivalant
        # to extended value into ans variable
        ans += str(i[1])

    if int(ans) == 0:
        return "0"
    return ans


# Driver code
#a = [1, 34, 3, 98, 9, 76, 45, 4, 12, 121]
#a = ["28", "2", "2", "8", "2", "3", "6", "4", "1", "1", "10", "6", "3", "3", "6", "1", "3", "8", "4", "6", "1", "10", "8", "4", "10", "4", "1", "3", "2", "3", "2", "6", "1", "5", "2", "9", "8", "5", "10", "8", "7", "9", "6", "4", "2", "6", "3", "8", "8", "9", "8", "2", "9", "10", "3", "10", "7", "5", "7", "1", "7", "5", "1", "4", "7", "6", "1", "10", "5", "4", "8", "4", "2", "7", "8", "1", "1", "7", "4", "1", "1", "9", "8", "6", "5", "9", "9", "3", "7", "6", "3", "10", "8", "10", "7", "2", "5", "1", "1", "9", "9", "5"]
print(largestNumber(a))

# This code is contributed by Chhekur