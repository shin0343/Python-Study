cabinet = {3:"유재석", 100:"김태호"} # key:value

print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3)) # same as cabinet[3]
# print(cabinet[5]) # error
print(cabinet.get(5)) # print "None"
print(cabinet.get(5,"사용 가능")) # print "사용 가능" (temporary)

print(3 in cabinet) # True
print(5 in cabinet) # False

# 딕셔너리에 추가
cabinet[3] = "김종국"
cabinet[35] = "조세호"
print(cabinet)

# key 삭제
del cabinet["3"]
print(cabinet)

# key들만 출력
print(cabinet.keys())

# value들만 출력
print(cabinet.values())

# keys, values 출력
print(cabinet.items())

# 딕셔너리 내용 전부 삭제
cabinet.clear()