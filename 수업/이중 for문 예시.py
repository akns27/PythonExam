
#숫자 역순 출력
for i in range(5, 0, -1):
    print(i, end=' ')
print( )

#짝수 출력
for i in range(0, 10, 2):
    print(i, end=' ')
print( )

#구간 합계 출력
total = 0
for i in range(1, 11, 2):
    total += i
    print(f"Sum from 1 to {i}: {total}")

# 별찍기 - 삼각형:

for i in range(5):
    for j in range(i + 1):
        print("*", end=" ")
    print()

# _________
for i in range(5):
  print('hello', end = ' ')
print( )

for i in range(0, 5):
  print('hello', end = ' ')
print( )
"""
for i in range(0, 5, +1):
  print('hello', end = ' ')
print( )
_________

# for i in range(1, 6, 2): # n부터 m-1까지 k씩 증가
# 	for j in range(2, 8, 3): # o부터 p-1까지 q씩 증가
# 		print(i+j, end=" ")

for i in range(1, 6, 2): # n부터 m-1까지 k씩 증가
	for j in range(2, 8, 3):
		result = i + j
		print(f"{i} + {j} = {result}", end="\n")
"""