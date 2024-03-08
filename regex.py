#1
import re
with open("text.txt", "r") as fp:
    r = fp.readlines()
s = ''.join(r)

def test(pattern, testinput):
    if re.search(pattern, testinput) == True:
        print("test is not passed")
    elif re.search(pattern, testinput) != None:
        print("test is passed!")
    else:
        print("test is not passed")
pattern = '^a(b*).'
test(pattern, )
test(pattern, "123ab45as")
test(pattern, "123ab452")
test(pattern, "abb")
test(pattern, "abbb452")

#2
def test(alo, Data):
    if re.search(alo, Data) == True:
        print("test is passed!")
    elif re.search(alo, Data) != None:
        print("test is passed!")
    else: 
        print("test is not passed!")
alo = 'ab{2,3}'

#3
def test(alo, inp):
    if re.search(alo, inp) == True:
        print("test is passed!")
    elif re.search(alo, inp) != None:
        print("test is passed")
    else: 
        print("test is not passed!")
alo = '[a-z]_[a-z]'

#4
def test(alo, Data):
    if re.search(alo, Data) == True:
        print("Test is passed!")
    elif re.search(alo, Data) != None:
        print("test is passed!")
    else: 
        print("test is not passed!")
alo = '[A-Z][a-z]'
Data = re.compile(input())
#5
def test(alo, Data):
    if re.search(alo, Data) == True:
        print("test is passed!")
    elif re.search(alo, Data) != None:
        print("test is passed!")
    else: 
        print("test is not passed!")
alo = '^a.*b$'

#6
def test(alo, inp):
    result = re.sub(alo, ':', inp)
    if result == True:
        print("test is passed!")
    else:
        print("test is not passed!")

alo = '[,]|[" "]|[@]'

#7
def test(alo, inp):
    result = re.sub(alo, "", inp)
    if result == True:
        print("test is passed!")
    else:
        print("test is not passed!")
alo = '[_]'

#8
def test(alo, data):
    result = re.split(alo, data)
    print(result)
    if result == True:
        print("test is passed!")
    else: 
        print("test is not passed!")

alo = r'([A-Z][a-z]*)'

#9
def test(pattern, testData, testNumber):
    result = re.sub(pattern, r"\1 \2", testData)
    print(result)
    if result == True:
        print(testNumber + " is passed!")
    else: 
        print(testNumber + " is not passed!")
pattern = r'(\w)([A-Z])'
test(pattern, "MySuperTest", "test1", "My Super Test")
test(pattern, " MySuperTest IAmRobot", "test2", " My Super Test I Am Robot")

#10
def test(pattern, testData):  
    result = re.sub(pattern, r"\1 \2", testData)  
    print(result)  
    if result == True:  
        print("test is passed!")  
    else:   
        print("test is not passed!")  
pattern = r'([a-zA-Z])([A-Z])'  
test(pattern, "MySuperTest", "My Super Test")  
test(pattern, " MySuperTest IAmRobot", " My Super Test I Am Robot")
