l1=[1,8,9,7,2,3,4,5,6]
l2=[2,3,4,5,6]
print(list({x for x in l1 if x in l2 or x in l1}))