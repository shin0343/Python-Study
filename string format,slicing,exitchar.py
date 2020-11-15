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


#### string format

print("나는 %d살입니다." % 20)
print("나는 %s를 좋아해요." % "파이썬")
print("Apple은 %c로 시작해요." % "A")

print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란","빨간"))

print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))

age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")


#### 탈출문자

print("백문이 불여일견\n 백견이 불여일타")
print("저는 \"나도코딩\"입니다.")


#### Quiz) 사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오
# 예) http://naver.com
# 규칙1: http://부분은 제외 => naver.com
# 규칙2: 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3: 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 "!" 로 구성
# 예) 생성된 비밀번호: nav51!

site = "http://naver.com"
index = site.index("/")
secondSlashIndex = site.index("/",index+1)
simpleSite = site[secondSlashIndex+1:]
site = simpleSite
firstPoint = site.index(".")
simpleSite = site[:firstPoint]
site = simpleSite
firstThreeWord = site[0:3]
countWordE = site.count("e")
password = firstThreeWord + str(len(site)) + str(countWordE) + "!"
print("{site}사이트의 비밀번호는 {pw}입니다.".format(site=site, pw=password))