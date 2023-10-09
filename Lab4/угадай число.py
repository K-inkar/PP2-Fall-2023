n = int(input())
Set = set()
for i in range(1, n+1):
  Set.add(i)
numbers = (input().split())
while numbers[0] != "HELP":
  numbers = {int(i) for i in numbers}
  ans = input()
  if ans == 'NO':
    Set -= numbers
  elif ans == 'YES':
    Set &= numbers
  numbers.clear()
  numbers = (input().split())
print(*sorted(list(Set)))
