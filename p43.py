def check_property(num_lst):
    num = (''.join(num_lst))
    x = int(num[1:5])
    if int(num[1:4])%2 != 0:
        return False
    if int(str(num[2:5]))%3 != 0:
        return False
    if int(str(num[3:6]))%5 != 0:
        return False
    if int(str(num[4:7]))%7 != 0:
        return False
    if int(str(num[5:8]))%11 != 0:
        return False
    if int(str(num[6:9]))%13 != 0:
        return False
    if int(str(num[7:10]))%17 != 0:
        return False
    return True

def heapPermutation(a, size,res_sum):
    # if size becomes 1 then prints the obtained
    # permutation
    if size == 1:
        if(check_property(a)):
            res_sum = res_sum + int(''.join(a))
        return res_sum

    for i in range(size):
        res_sum = heapPermutation(a, size - 1,res_sum)

        # if size is odd, swap 0th i.e (first)
        # and (size-1)th i.e (last) element
        # else If size is even, swap ith
        # and (size-1)th i.e (last) element
        if size & 1:
            a[0], a[size - 1] = a[size - 1], a[0]
        else:
            a[i], a[size - 1] = a[size - 1], a[i]

    return res_sum




if __name__ == '__main__':
    # Driver code
    a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    n = len(a)
    res = 0
    print(heapPermutation(a, n,res))

