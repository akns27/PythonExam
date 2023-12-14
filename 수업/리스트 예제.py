"""
리스트 예제1
무작위로 번호 부르기

출석 번호를 부른 횟수인 정수 n이 입력
두 번째 줄에는 무작위로 부른 n개의 번호가 공백을 두고 순서대로 입력된다.
1번부터 번호가 불린 횟수를 순서대로 공백으로 출력하여 한줄로 출력한다.
"""
n = int(input)#출석번호 부른 횟수
num = list(map(int, input.split('')))#학생들의 번호
result = list(0 for _ in range(24))#학생들을 차례대로 배열시킬 리스트 생성

for i in range(n):
    result[num[i]]+=1#i번째로 입력받은 학생의 번호이다. 따라서 result[num[i]]+=1은 해당 학생의 번호가 부른 횟수를 1 증가시킨다.

for i in range(1, 24):
    print(result[i], end=' ')
#list 연습하기
#주석도 달아보기
#append, extend, insert