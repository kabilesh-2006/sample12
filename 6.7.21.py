
list=eval(input("enter the list"))

for i in list:
    if(i%2==0):
        print(i,"is an even number")
    else:
        print(i,"is an odd number")


mylist=eval(input("enter the list"))
print("intial list :",mylist)
length=len(mylist)

x=mylist[0]
mylist[0]=mylist[length-1]
mylist[length-1]=x

#mylist[0],mylist[3]=mylist[3],mylist[0]

print("list after swapping :",mylist)
print("computer"," science",sep=" and",end=" ")

