
# quiz4
# 당신의 학교에서 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.

# 조건1: 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
# 조건2: 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3: random 모듈의 shuffle과 sample을 활용

print("===== QUIZ 4 =====")

from random import *
users = range(1, 21) #users = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
users = list(users)
shuffle(users)
print("-- 당첨자 발표 -- ")
winners = sample(users, 4)
print("치킨 당첨자 : %d " %winners[0])

print("커피 당첨자 : {0}" .format(winners[1:]))
print("-- 축하합니다 --")


# quiz5
# 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건1: 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건2: 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

# (출력문 예제)
# [O] 1번째 손님 (소요시간: 15분)
# [ ] 2번째 손님 (소요시간: 50분)
# [O] 3번째 손님 (소요시간: 5분)
# . . .
# [ ] 50번째 손님 (소요시간: 16분)

# 총 탑승 승객: 2명

print("===== QUIZ 5 =====")

from random import *
total_cnt = 0 # 총 승객 수
for i in range(1, 51): # 1 ~ 50
    passenger_need = randrange(5, 51)
    if 5 <= passenger_need <= 15:
        total_cnt += 1
    else:
        continue

print(total_cnt)


# quiz6 - 표준 체중을 구하는 프로그램 작성
# 남자: 키(m) x 키(m) x 22
# 여자: 키 x 키 x 21
# 조건1: 표준 체중은 별도 함수 내에서 계산
#         * 함수명: std_weight
#         * 전달값: 키(height), 성별(gender)
# 조건2: 표준 체중은 소수점 둘째자리까지 표시

# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

print("===== QUIZ 6 =====")

def std_weight(height, gender):
    if gender == "male":
        return height*height*22
    elif gender == "female":
        return height*height*21
    else:
        return -1

height = 175
gender = "male"
weight = round(std_weight(height/100,gender),2) # 소수점 3번째에서 반올림
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))