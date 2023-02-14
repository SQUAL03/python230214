#demodict.py

device = {"아이폰":5,"아이패드":10,"윈도우":20}
print(device["아이폰"])
device["맥"] = 15
print(device)
device["아이폰"] = 6
del device["맥"]
print(device)

print("-----명함관리---")
phone = {"kim":1111,"lee":2222,"park":3333}
print("kim" in phone)
print("moon" in phone)



print("참조를 전달")
p = phone
phone["moon"] = "1234"
print(phone)
print(p)
print(id(phone),id(p))       

isRight = True
print(type(isRight))
print(1<2)
print(2==2)
print(1 != 2)

print( True and True and True)
print( True and True and False)
print( True and True or False)