n = int(input("Введите число:"))
maxim = 0
while n>0:
    last=n%10
    if last > maxim:
        maxim = last
    n = n//10
print("Maxim:{a}".format(a=maxim))