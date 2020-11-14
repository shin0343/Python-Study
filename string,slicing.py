#### string

sentence = '나는 소년입니다'
print(sentence)

sentence2 = "파이썬은 쉬워요"
print(sentence2)

sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3) # 위아래 한줄씩 개행

#### slicing

jumin = "990120-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0부터 2 직전(=1)까지
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[:6]) # 처음부터 6 직전(=5)까지
print("뒤 7자리 : " + jumin[7:]) # 뒤에서 끝까지
print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) # 맨 뒤로부터 7번째에서 끝까지


#### string 처리

python = "Python is Amazing"
print(python.lower()) # 소문자로 출력
print(python.upper()) # 대문자로 출력
print(python[0].isupper())
print(print(len(python)))
print(python.replace("Python", "Java"))

index = python.index("n") # 첫 번째 n의 위치
print(index)
index = python.index("n",index + 1) # 두 번째 n의 위치(인덱스)
print(index)

print(python.find("Python"))
print(python.find("Java"))
#print(python.index("Java"))

print(python.count("n"))