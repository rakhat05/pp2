#1
import math
print(math.radians(float(input())))

#2
x=int(input())
y=int(input())
z=int(input())
ar=((z+y)/2)*x
print(ar)

#3
num = int(input("Input number of sides: "))
length = float(input("Input the length of a side: "))
p = num * length
a = length / (2 * math.tan(math.pi / num))
area = (1 / 2) * p * a
print("The area of the polygon is:", area)

#4
length = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))
area = length * height
print("The area of the parallelogram is:", area)