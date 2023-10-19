
a = int(input("Enter a: "))
b = int(input("Enter b: "))

print(a, "+", b, "=",a+b)
print("%d - %d = %d"%(a,b,a-b))
print(f"{a}  *  {b} = {a*b}")
print("{} / {} = {}" ,format(a,b,a/b))
print("{} ** {} = {}",format(a,b,a**b))
print("{} % {} = {}",format(a,b,a%b))
print("{} // {} = {}",format(a,b,a//b))

print("Addition of {} and {} is {}".format(a,b,a+b))