# 리스트 []

# 지하철 칸 별로 10명, 20명, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30
subway = [10,20,30] # 위 3줄을 1줄로 짧게
print(subway)

subway = ["유재석","조세호","박명수"]

# 인덱스 위치
print(subway.index("조세호"))

# 뒤에 추가
subway.append("하하")
print(subway)

# 특정 인덱스 위치에 추가
subway.insert(1, "정형돈")
print(subway)

# 리스트 맨 뒤를 pop
print(subway.pop())
print(subway)

# 리스트 맨 뒤에 추가 후, 인자로 들어간 요소가 리스트에 몇개 있는지
subway.append("유재석")
print(subway.count("유재석"))

# 정렬
num_list = [5,2,4,3,1]
num_list.pop()
print(num_list)

# 순서 뒤집기
num_list.reverse()
print(num_list)

# 다양한 자료형 함께 사용
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)

# 모두 지우기
num_list.clear()