import heapq

min_heap = [5, 3, 9, 4, 1, 2, 6]
heapq.heapify(min_heap)

print(heapq.heappop(min_heap))
print(heapq.heappop(min_heap))
print(heapq.heappop(min_heap))
print(heapq.heappop(min_heap))

heapq.heappush(min_heap, 1)
print(heapq.heappop(min_heap))

# max heap 구현 1
max_heap = [5, 3, 9, 4, 1, 2, 6]
heapq._heapify_max(max_heap)
value = heapq._heappop_max(max_heap)

print(value)

# max heap 구현 2
max_heap = [5, 3, 9, 4, 1, 2, 6]
max_heap = [i * -1 for i in max_heap]
heapq.heapify(max_heap)
weight = heapq.heappop(max_heap)
value = -1 * weight

