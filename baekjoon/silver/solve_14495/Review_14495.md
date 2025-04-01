# 백준 14495 : 피보나치 비스무리한 수열


### ✅ 첫번째 풀이 : 초기값을 설정하고 반복문을 이용해서 풀이함

#### 결과 : 통과

    def likeFibo(n):
        size = max(3, n+1)
        array = [0]*size
    
        array[0] = array[1] = array[2] = 1
    
        for i in range(3, n+1):
            array[i] = array[i-1] + array[i-3]
    
        return array[n-1]
    
    
    n = int(input())
    
    print(likeFibo(n))

### ✅ 두번째 풀이 : 재귀함수를 이용해서 풀이함

#### 결과 : 시간 초과 ❌

#### 원인 : 이미 구한 값들도 계속해서 구하고, 재귀를 계속 돌려서 시간초과가 일어남

    def likeFibo(n):
        if n == 0 or n == 1 or n == 2:
            return 1
        return likeFibo(n-1) + likeFibo(n-3)
    
    n = int(input())
    print(likeFibo(n-1))


### ✅ 세번째 풀이 : 재귀함수 + 메모이제이션 이용해서 풀이함

#### 결과 : 통과

### 🔥 두번째 풀이와 차이 : 이미 구한 값들은 저장해두고 다시 이용해 시간을 단축시킴
    
    def likeFibo(n, memo = None):
        if memo is None:
            memo = [-1] * (n+1)
    
        if n == 0 or n == 1 or n == 2:
            return 1
    
        if memo[n] != -1:
            return memo[n]
    
    
        memo[n] = likeFibo(n-1, memo) + likeFibo(n-3, memo)
        return memo[n]
    
    n = int(input())
    print(likeFibo(n-1))


### ✅ 정리

### 👉🏻 초기값을 잘 설정하면 재귀함수를 이용해 값을 구할 수 있다. 

### 👉🏻 재귀함수를 이용한다면 메모이제이션을 사용해, 이전에 구한 값들은 다시 계산하지 않아 시간을 단축시킬 수 있다.