# Q0. 두 정수의 최대공약수를 구하라. 최대공약수는 두 정수를 나머지가 0이 되게 나누는 공통된 약수 중 최대값을 가진 수이다

a = int(input())
b = int(input())

def solution(a, b):
    if a > b: a,b = b,a
    
    for i in range(1, a+1):
        if a % i == 0 and b % i == 0:
            answer = i
    return answer

c = solution(a,b)
print(c)
