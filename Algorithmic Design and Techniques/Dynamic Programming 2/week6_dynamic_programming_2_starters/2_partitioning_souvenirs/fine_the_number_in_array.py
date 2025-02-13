

def find_element(arr, value):
    if value in arr:
        return "YES"
    else:
        return "No"


arr = [1,4, 8, 9]
value = 10
print(find_element(arr, value))