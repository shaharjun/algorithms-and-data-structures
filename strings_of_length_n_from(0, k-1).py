list = []

def generator(n, k):
    if n < 1:
        print(list)
    else:
        for i in range(0, k):
            list[n-1] = i
            generator(n-1, k)

def create_array(n):
    for i in range(0, n):
        list.append(int(0))

n = int(input("enter the size of array : "))
k = int(input("enter the max value : "))

create_array(n)

generator(n, k)
