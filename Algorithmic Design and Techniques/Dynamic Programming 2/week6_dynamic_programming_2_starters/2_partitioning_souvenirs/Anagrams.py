
def find_anagram(input):
    NewD = {}
    #listing = input.split(',')
    for i in input:
        a = "".join(sorted(i))
        if a in NewD:
            #values = [NewD[a]]
            #values += " , " + i
            #values.append(i)
            NewD[a].append(i)
        else:
            NewD[a] = [i]

    return NewD

## Given an array

input = ["eat","tea","tan","ate","nat","bat"]
print(find_anagram(input))
