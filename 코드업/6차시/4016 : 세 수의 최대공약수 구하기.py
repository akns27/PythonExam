#세 수 를 입력받아 세 수의 최대공약수를 구하는 프로그램을 작성하시오.
def three(a, b):
  while(a%b != 0):
    a, b = b, a%b#64, 32
  return b

a,b,c = map(int, input().split())
step = three(a,b)
print(three(step, c))