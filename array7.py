def ok(digit):
    digit.reverse()
    # print(digit)
    carry = 1
    for i in range(len(digit)):
        print(carry,digit[i])
        if carry == 0:
            digit.reverse()
            return digit
        digit[i] = digit[i] + 1
        if digit[i] > 9:
            digit[i] = digit[i]%10
            carry = 1 
        else:
            carry = 0
    if carry == 1:
        digit.append(1)
    digit.reverse()
    return digit
print(ok([9,9,9]))