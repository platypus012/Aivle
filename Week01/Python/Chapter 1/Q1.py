# Q1. 두 정수의 최소공배수를 구하라. 최소공배수는 두 정수의 배수인 수 중 최솟값을 가진 값을 수이다.
a = int(input())
b = int(input())
    
def solution(a, b):
    if a > b: a, b = b, a

    for i in range(b, (a*b)+1):
         if i % a == 0 and i % b == 0:
            answer = i
            break
    return answer

c = solution(a,b)
print(c)
