# 수열

# 시간초과

N, K = map(int, input().split())
tmp_list = list(map(int, input().split()))

result = []

for i in range(0, len(tmp_list) -K +1):
    list_sum = 0
    front_pointer = i
    after_pointer = front_pointer + K

    slice_tmp_list = tmp_list[front_pointer:after_pointer] # 매 반복마다 슬라이싱을 계속 일으켜 성능저하

    result.append(sum(slice_tmp_list))


print(max(result))


# 통과

N, K = map(int, input().split())
tmp_list = list(map(int, input().split()))

current_sum = sum(tmp_list[:K])
max_sum = current_sum

for i in range(K, N):
    current_sum = current_sum - tmp_list[i - K] + tmp_list[i] # 슬라이싱말고 기존값에서 제외되는 값, 추가되는 값 빼고 더하고가 성능에 더 유리함
    max_sum = max(max_sum, current_sum)

print(max_sum)

