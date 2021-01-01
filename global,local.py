gun = 10

def checkpoint(soldiers): # 경계근무
    global gun # 전역 공간에 있는 gun 사용. 밖의 gun 변수를 가져옴
    gun = gun - soldiers # 함수 내의 gun을 사용함
    print("[함수 내] 남은 총의 수 : {0}".format(gun))

def checkpoint_ret(gun, soldiers): # 경계근무
    gun = gun - soldiers # 함수 내의 새로운 지역변수 gun을 사용함
    print("[함수 내] 남은 총의 수 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
#checkpoint(2) # 2명이 경계 근무 나감
gun = checkpoint_ret(gun, 2) # 2명이 경계 근무 나감
print("전체 총 : {0}".format(gun))