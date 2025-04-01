
l = []

def is_prime(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

def divide(x, str):

    if is_prime(x):
        return x

    list = []
    for i in range(1, x):
        if x % i == 0:
            list.append(i)
        
    print(str+'-',x)

    i = list[len(list) // 2]

    m = divide(i, str+'-')
    if m != None:
        print(str+'--', m)
        l.append(m)
    n = divide(int(x/i), str+'-')
    if n != None:
        print(str+'--', n)
        l.append(n)

def quantity(l, i):
    x = 0
    for j in l:
        if j == i:
            x += 1
    return x

def last_cells(l):
    number_list = []
    power_list = []
    for i in l:
        if i not in number_list:
            number_list.append(i)
            power_list.append(quantity(l, i))
    return(number_list, power_list)

def dif_format(number_list, power_list):
    for i in range(len(number_list)):
        if not(i < len(number_list) - 1):
            print(f'({number_list[i]}^{power_list[i]})', sep='',end='')
        else:
            print(f'({number_list[i]}^{power_list[i]})*', sep='',end='')

if __name__ == '__main__':
    x = int(input())
    divide(x,'')
    
    if l == []:
        print(f'{x} is a prime number.')
    else:
        number_list, power_list = last_cells(l)
        dif_format(number_list, power_list)








