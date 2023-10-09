'''def test(n):
    if n == 0:
        return 
    print(n)
    test(n-1)
    
test(5)'''


number  = int(input("Enter number: "))    
def p(n):
    if n == number + 1:
        return
    print(n)
    p(n+1)
    
p(1)


