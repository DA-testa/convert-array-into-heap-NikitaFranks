def build_heap(data, i, swaps):
  n = len(data)
  min = i
  l = 2 * i + 1
  r = 2 * i + 2

  if l < n and data[l] < data[min]:
    min = l

  if r < n and data[r] < data[min]:
    min = r

  if i != min:
    swaps.append((i, min))
    data[i], data[min] = data[min], data[i]
    build_heap(data, min, swaps)
  return swaps


def main():
  input_type = input().lower()

  if input_type == "I":
    n = int(input())
    data = list(map(int, input().split()))
  elif input_type == "F":
    while True:
      try:
        file_name = input().strip()
        if 'a' not in file_name:
          step = './tests/' + file_name
          with open(step) as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))
          break
      except FileNotFoundError:
        print("File not found, please enter a valid file name")
  else:
    n = 0
    data = []

  assert len(data) == n
  swaps = []
  for i in range(n // 2, -1, -1):
    swaps = build_heap(data, i, swaps)

  print(len(swaps))
  for i, j in swaps:
    print(i, j)


if __name__ == "__main__":
  main()
