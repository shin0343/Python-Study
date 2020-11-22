def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다." .format(balance+money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance-money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
        return balance

def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission # tuple 반환

balance = 0
balance = deposit(balance, 3000)
balance = withdraw(balance, 500)
print(balance)

commission, balance = withdraw_night(balance, 500)
print("수수료 {0} 원이며, 잔액은 {1} 원입니다." .format(commission, balance))


#기본값
def profile(name, age=17, main_lang="파이썬"):
    print("이름: {0}\t나이 : {1}\t주 사용 언어: {2}" \
        .format(name, age, main_lang))

profile("유재석",20,"파이썬")
profile("김태호")
#키워드값
profile(main_lang="자바", age=25, name="김태호")

#가변인자
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름: {0}\t나이: {1}\t" .format(name,age), end= " ") #end를 이렇게 붙혀주면, 아래 print문과 하나의 문장으로 출력!
#     print(lang1, lang2, lang3, lang4, lang5)

def profile(name,age,*language): #매개변수 앞에 * 붙히면 가변인자로 사용
    print("이름: {0}\t나이: {1}\t" .format(name,age), end= " ") #end를 이렇게 붙혀주면, 아래 print문과 하나의 문장으로 출력!
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호",25,"Kotlin","Swift")