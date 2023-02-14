#function2.py

print("--불변--")
a = 1.2
print(id(a))
a = 3.4
print(id(a))

print("--가변--")
lst = [1,2,3]
print(id(lst))
lst.append(4)
print(id(lst))

x = 5
def func(a):
    return a+x

#호출(전역)
print(func(1))

def func2(a):
    x = 6 
    return a+x

#호출(지역)
print(func2(1))