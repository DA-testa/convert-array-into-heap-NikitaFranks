def build_heap(data, i, swaps):
    n = len(data)
    min = i
    l = 2*i+1
    r = 2*i+2

    if l < n and data[l] < data[min]:
        min = l
        
    if r < n and data[r] < data[min]:
        min = r

    if i != min: 
        swaps.append((i,min))
        data[i],data[min] = data[min],data[i]
        build_heap(data,min,swaps)
    return swaps


def main():
    input_type = input().lower()

    if input_type.startswith('i'):
        n = int(input())
        data = list(map(int, input().split()))
    elif input_type.startswith('f'):
        while True:
            try:
                file_name = "tests/" + input()
                with open(file_name, 'r', encoding="utf-8") as f:
                    n = int(f.readline().strip())
                    data = list(map(int, f.readline().strip().split()))
                break
            except FileNotFoundError:
                print("File not found, please enter a valid file name")
                continue
    else:
        n = 0
        data = []

    swaps = []
    for i in range(n//2,-1,-1):
        swaps = build_heap(data, i, swaps)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)
    