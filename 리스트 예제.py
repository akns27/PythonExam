"""
리스트 예제1
무작위로 번호 부르기

출석 번호를 부른 횟수인 정수 n이 입력
두 번째 줄 에는 무작위로 부른 n개의 번호가 공백을 두고 순서대로 입력된다.
1번부터 번호가 불린 횟수를 순서대로 공백으로 출력하여 한줄로 출력한다.
"""
n = int(input)#정수로 입력
num = list(map(int, input.split('')))
result = list(0 for _ in range(24))

for i in range(n):
    result[num[i]]+=1

for i in range(1, 24):
    print(result[i], end=' ')
#list 연습하기
#주석도 달아보기
#append, extend, insert