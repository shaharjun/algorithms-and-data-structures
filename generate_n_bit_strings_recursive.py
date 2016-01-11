array = []

def create_array(n):
    for i in range(0, n):
        array.append(int(0))

def n_bit_string(n):

    if n < 1:
        print(array)
    else:
        array[n-1] = 0
        n_bit_string(n-1)
        array[n-1] = 1
        n_bit_string(n-1)

n = int(input("enter the no of bits : "))
create_array(n)
n_bit_string(n)