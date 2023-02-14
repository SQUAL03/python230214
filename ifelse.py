# ifelse.py

score = int(input("점수를 입력:"))
if 90 <= score:
      grade = 'A'
elif 80 <= score:
      grade = 'B'
elif 60 <= score:
      grade = 'C'
elif 50 <= score:
      grade = 'D'
else:
     grade = 'F'

print("등급은 ?", grade)     
     
      
