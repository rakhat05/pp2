#1 
def generate(n): 
    for i in range(n+1): 
        yield pow(i, 2) 
n = int(input())         
at = generate(n) 
for j in generate(n): 
    print(next(at)) 

#2 
def even(n): 
    for i in range(0, n+1): 
        if i % 2 == 0: 
            yield i 
n = int(input()) 
a = even(n) 
for j in even(n): 
    print(next(a), end = ", ") 

#3 
def divided_3_4(n): 
    for i in range(0, n+1): 
        if i % 3 == 0 and i % 4 == 0: 
            yield i 
n = int(input()) 
a = divided_3_4(n) 
for j in divided_3_4(n): 
    print(next(a), end = " ") 
    
#4 
def square(a, b): 
    for i in range(a, b): 
        yield pow(i, 2) 

a = int(input()) 
b = int(input()) 

q = square(a, b) 

for j in square(a, b): 
    print(next(q), end = " ") 

#5 
def numbers(n): 
    i = n 
    while i >=0: 
        yield i 
        i = i-1 
n = int(input()) 
a = numbers(n) 
for j in numbers(n): 
    print(next(a), end = " ")
