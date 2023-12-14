def f(n):
  if(n==1):
    return 1
  else:
    return f(n-1)*n#1씩 뺀걸 곱하기
  
n = int(input())
print(f(n))
#n이 입력되면 n!의 값을 출력하시오.