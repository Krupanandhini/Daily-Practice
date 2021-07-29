def Solution(lst):
  pile = float('inf')
  while lst:
    num = lst.pop(0) if lst[0] > lst[-1] else lst.pop(-1)
    if num > pile: return "No"
    pile = num
  return "Yes"

def main():
  t = int(input())
  for _ in range(t):
    n = int(input())
    lst = list(map(int, input().strip().split()))
    print(Solution(lst))

if __name__ == "__main__":
  main()
