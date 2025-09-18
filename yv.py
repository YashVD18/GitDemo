a = int(input("enter the number : "))
b = int(input("enter the number :"))

sum=a+b
sub=a-b
mul=a*b
div=a/b

print("enter the operation:")
c = int(input("enter 1,2,3,4 :"))

if c == 1:
    print(sum)
elif c == 2:
    print(sub)
elif c == 3:
    print(mul)
elif c == 4:
    print(div)
else:
    print("invalid")