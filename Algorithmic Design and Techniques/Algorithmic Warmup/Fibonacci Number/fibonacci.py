# Uses python3

MyArray = [0,1]
 
def calc_fibonacci(n):
    if n<=0:
        print("Fibonacci series is applicable for positive integers only")
    elif n<=len(MyArray):
        return MyArray[n-1]
    else:
        result = calc_fibonacci(n-1)+calc_fibonacci(n-2)
        MyArray.append(result)
        return result

n = int(input())
print(calc_fibonacci(n))