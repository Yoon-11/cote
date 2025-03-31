# 백준 1929 : 소수 구하기

### 첫번째 풀이 : 주어진 숫자 범위 내에서 약수 개수를 count 해서 count를 이용해 소수 출력

#### 결과 : 시간초과

#### 원인 : 프루트 포스로 범위 내의 숫자들의 약수를 다 세봐야해서 시간초과가 일어났다.


    M, N = map(int, input().split())
    
    for i in range(M, N+1):
        count = 0
        for k in range(1, int(i**0.5) +1):
            if i % k == 0 :
                count += 1
        if count == 1:
            print(i)


### 두번째 풀이 : 소수가 아닌 수는 break를 이용해 반복문을 빠져나와 시간을 줄였다.

#### 결과 : 통과

#### 조건에 맞지 않는 수는 더 이상 약수를 구하지 않고 바로 빠져나오는 것이 큰 차이를 일으켰다.

    M, N = map(int, input().split())
    
    for i in range(M, N+1):
        if i == 1:
            continue
    
        for k in range(2, int(i**0.5) +1):
            if i % k == 0 :
                break
        else:
            print(i)


### 세번째 풀이 : **_에라토스테네스의 체 알고리즘_**

#### 결과 : 통과


    from math import sqrt
    
    M, N = map(int, input().split())
    is_prime = [True] * (N + 1)
    
    is_prime[0] = is_prime[1] = False
    
    
    for i in range(2, int(sqrt(N)) + 1):
        if not is_prime[i]:
            continue
    
        for j in range(i * i, N + 1, i):
            is_prime[j] = False
    
    
    for i in range(M, N + 1):
        if is_prime[i]:
            print(i)


#### 두번째 코드와 세번째 코드 시간 차이:

![img.png](img.png)

## 결론 : 소수를 구할때는 에라토스테네스의 체 알고리즘을 사용하는 것이 유리!
