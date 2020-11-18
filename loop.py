# for
for waiting_no in range(5): # 0~4
    print("대기번호 : {0}".format(waiting_no))

starbucks = ["아이언맨", "토르", "캡틴"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))

# 한 줄 for
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)

students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)


# while
customer = "토르"
index = 5
while index >= 1:
    print("{0}, 커피가 준비되었습니다. {1}번 남았어요." .format(customer,index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")

person = "Unknown"
while person != customer:
    print("{0}, 커피가 준비되었습니다." .format(customer))
    person = input("이름은? ")


# continue,break
absent = [2, 5]
no_book = [7]
for student in range(1, 11): # 1,2,3,4,5,6,7,8,9,10
    if student in absent:
        continue
    elif student in no_book:
        break
    print("{0}, 책을 읽어봐.".format(student))
