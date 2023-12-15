numbers = [i for i in range(1, 11)]
print(numbers)

even_numbers = [i for i in range(1, 11) if i % 2 == 0]
print(even_numbers)

#1부터 10까지의 숫자 중 제곱한 값을 포함하는 리스트
squared_numbers = [i ** 2 for i in range(1, 11)]
print(squared_numbers)

#문자열 "Hello, world!"의 각 문자를 포함하는 리스트
letters = [i for i in "Hello, world!"]
print(*letters)
