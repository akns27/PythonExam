"""
시작수(a)와 마지막 수(b)가 입력되면
a부터 b까지의 모든 홀수를 출력하시오.

"""
def f(a, b):
    if(a%2==0):
      a+=1
    if (a <= b):
      print(a, end = ' ')
      f(a + 2, b)#다음 홀수 ~ b까지

a,b = map(int, input().split())
f(a, b)
