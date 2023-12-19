
a,b = map(int, input().split())

while a%b !=0:
  a,b= b, a%b

print(b)

########################################################################

def f(a,b):
    while(b!=0):
      a, b = b, a%b
    return a

a, b = map(int, input().split())
print(f(a,b))

########################################################################

a,b = map(int, input().split())

def f(a,b):
  if a%b == 0:# 나머지가 0인지 확인
    return b
  return f(b, a%b)#a%b != 0

result = f(a,b)
print(result)

########################################################################
#1번과 동일
a,b = map(int, input().split())

def gcd(a,b):
  if a%b !=0: #나머지가 0이 아닌지 확인
    return gcd(b, a%b)
  return b#a%b == 0
  
result = gcd(a,b)
print(result)
