data = [];

# 하위 트리를 최대 원소가 루트에 오도록 힙으로 변환합니다.
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # 왼쪽 자식이 루트보다 크면
    if left < n and arr[i] < arr[left]:
        largest = left

    # 오른쪽 자식이 현재까지의 최대값보다 크면
    if right < n and arr[largest] < arr[right]:
        largest = right

    # 최대값이 루트가 아니라면
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # 교환

        # 루트를 힙으로 변환
        heapify(arr, n, largest)

# 배열에 힙 정렬을 수행합니다.
def heapSort(arr):
    n = len(arr)

    # 최대 힙 구성
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 하나씩 원소를 추출
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 교환
        heapify(arr, i, 0)

with open("input.txt", "r") as f:
    for line in f:
        data.append(int(line.strip()))

# 파일에서 읽은 데이터 숫자 배열에 힙 정렬 적용
heapSort(data)

# 정렬된 배열을 새 파일에 작성 준비
with open("output.txt", 'w') as file:
    for number in data:
        file.write(str(number) + '\n')
