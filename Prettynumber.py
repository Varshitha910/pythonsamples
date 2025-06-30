# a=int(input("enter a value"))
# if(a%10==7 or a%100==7):
#     print("yes")
# else:
#     print("no")
 
# for i in range(10):
#     if i%10==7 or i//10==7:
#         print(i,end="*")
#comprehensive list
# list1=[10,20,False]
# print(sum(list1))
n=10
list1=[]
for i in range(n):
    if 1%2==0:
        list1.append(1)
print(list1)
#comprehensive list => used dealing with huge data
list2=[x for x in range(n) if x%2==1]
print(list2)