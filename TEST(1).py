1.# this program using print () write hello world

print("hello world")

2.# make multiple value in single line use of lst datatype

list=(7623,736.3,321312,"dholka",676+88j)

print(list)

3.# make swap function using three variable

a=10
b=30

temp=a
a=b
b=temp

swap=a
swap1=b

print("the swap real value of a is=",swap)
print("the swap real value of b is=",swap1)

4.# use of type () and isinstance () in program

# type()
n1=78
n2=90.89
n3=90+89j
n4= "dholka"


print("the data type is like =",type(n1))
print("the data type is like =",type(n2))
print("the data type is like =",type(n3))  #the type function is check what is a type of data
print("the data type is like =",type(n4))


# isinstance ()

n1=89
n2=90.56
n3="dholka"

print(isinstance(n1,int))
print(isinstance(n2,str))
print(isinstance(n3,float))
print(isinstance(n2,float))
print(isinstance(n3,str))

5.# tuple using (:) operator in programm

tuple=(78,78.09,"computer engineering",67+98j,78.90)

print(tuple)
print(tuple[2])
print(tuple[1:3])
print(tuple[:4])
print(tuple[3:])

string="AKASH TECHNOLABS"

print(string)
print(string[4])
print(string[2:5])


6.# make first name,middle name,last name pogramm 

n=str(input("enter first name ="))
z=str(input("enter middle name ="))
x=str(input("enter last  name ="))

name=n+z+x

print("the full name is = ",name)

7.# calculate area of circle program

pi=int(input("enter the value of pi = "))
r=int(input("enter the value of r = "))
r=int(input("enter the value of r = "))

circle=pi*r*r

print("the area of circle is = ",circle)

8.# calculate avrege of 5 numbers 

n1=int(input("enter the value of n1 = "))
n2=int(input("enter the value of n2 = "))
n3=int(input("enter the value of n3 = "))
n4=int(input("enter the value of n4 = "))
n5=int(input("enter the value of n5 = "))

avrege=n1+n2+n3+n4+n5/5

print("the avrege is = ",avrege)

9.# calculate simple intrest program

p=float(input("enter the value of p = "))
r=float(input("enter the value of r = "))
t=float(input("enter the value of t = "))

intrest=p*r*t/100

print("the intrest is = ",intrest)

10.# calculate area of rectangle programm

l=int(input("enter the value of l = "))
b=int(input("enter the value of b = "))

rectangle=l*b
print("the area of rectangle is = ",rectangle)

11.# calculate area of square programm

l=int(input("enter the value of l = "))
l=int(input("enter the value of l = "))

square=l*l
print("the area of rectangle is = ",square)

12.# check year is leap or not

year=int(input("Enter year to be checked:"))
if(year%4==0 and year%100!=0 or year%400==0):
    print("The year is a leap year!")
else:
    print("The year isn't a leap year!")
  
