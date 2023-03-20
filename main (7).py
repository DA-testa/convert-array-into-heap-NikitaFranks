def heap(info, i, n, swaps):
  minimums = i
  kreisais = 2 * i + 1
  labais = 2 * i + 2
  if kreisais < n and info[kreisais] < info[minimums]:
    minimums = kreisais

  if labais < n and info[labais] < info[minimums]:
    minimums = labais
  if i != minimums:
    info[i], info[minimums] = info[minimums], info[i]
    swaps.append((i, minimums))
    heap(info, minimums, n, swaps)


def build_heap(info):
  swaps = []
  n = len(info)

  for i in range(n // 2 - 1, -1, -1):
    heap(info, i, n, swaps)

  return swaps


def check(info, swaps):
  n = len(info)
  for i in range(n):
    for j in range(i + 1, n):
      if info[j] < info[i]:
        info[i], info[j] = info[j], info[i]
        swaps.append((i, j))

  return swaps


def main():
  txt = input().strip()

  if 'I' in txt:
    n = int(input())
    info = list(map(int, input().split()))

  if 'F' in txt:
    filename = input().strip()
    if 'a' not in filename:
      step = './tests/' + filename
      with open(step) as f:
        n = int(f.readline())
        info = list(map(int, f.readline().split()))

  assert len(info) == n

  swaps = build_heap(info)

  print('swaps')
  print(len(swaps))
  for i, j in swaps:
    print(i, j)


if __name__ == '__main__':
  main()
