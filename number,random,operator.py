print("lol"*9) # lollollollollollollollollol
print(2**3) # 2^3
print(5//3) # 몫

print(abs(-5))
print(round(3.14))
print(round(4.99))

from math import *
print(floor(4.99))
print(ceil(3.14))
print(sqrt(16))

from random import *
print(random()) # 0.0 ~ 1.0 미만의 임의의 값
print(random() * 10) # 0.0 ~ 10.0 미만
print(int(random() * 10)) # 0 ~ 10 미만

date = randint(4, 28) # 4 ~ 28 이하
print("오프라인 스터디 모임 날짜는 매월"+str(date)+" 일로 선정되었습니다.")
