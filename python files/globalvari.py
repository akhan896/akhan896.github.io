a = 5
def test():
    global a
    a=a+2
    print(a)
    
test()

print(a)