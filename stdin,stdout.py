print("Python", "Java", "Javascript", sep=" vs ") # 명시된 sep에 의해 각 문자열이 sep으로 분리됨
print("Python", "Java", "Javascript", sep=",", end="?") # 명시된 end에 의해 개행 안됨
print("무엇이 더 재밌을까요?")

import sys
print("Python", "Java", file=sys.stdout)
print("Python", "Java", file=sys.stderr)

# 시험 성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":") # ljust: 8칸 확보한 상태에서 왼쪽 정렬


# 은행 대기순번표
# 001, 002, 003 ...
for num in range(1,21):
    print("대기번호 : "+str(num).zfill(3)) # zfill: 실제 숫자값 대신 3자리 수를 잡고 비는 공간은 0으로 채운다 ex. 1->001

# 표준 입력
answer = input("아무 값이나 입력하세요 : ")
print(type(answer)) # 사용자 입력으로 입력받은 숫자는 string로 변환되어 처리된다.
print("입력하신 값은 " + answer + "입니다.")