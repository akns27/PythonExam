n = int(input())
num = 0 

for i in range(1, n+1):
    num += i#15까지 만듦

for i in range(1, n+1):
    for j in range(1, i+1):
        print(num, end = " ")
        num -= 1
    print( )

"""
길이 n 이 입력되면 다음과 같은 숫자 피라미드를 출력한다.

예) n이 5이면

15

14 13

12 11 10

9 8 7 6

5 4 3 2 1 
"""