#program that accepts 2 lists and add all the even numbers from both lists which ever matches
n=int(input("no of lists"))
list1=eval(input("enter the value of list1"))
list2=eval(input("enter the value of list2"))
list1=list(set(list1))
list2=list(set(list2))
s=0
for i in list1:
    if i in list2:
        if(i%2==0):
            k=list2.count(i)
            s=s+i+k*i
print(s)







