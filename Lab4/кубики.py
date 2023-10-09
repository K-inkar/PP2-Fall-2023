n, m = [int(i) for i in input().split()]

ani = set()
bori = set()

for _ in range(n):
    color = int(input())
    ani.add(color)
    
for _ in range(m):
    color = int(input())
    bori.add(color)
    
common = ani & bori

ani_colors = ani - bori
bori_colors = bori - ani

print(len(common))
print(*sorted(common))
print(len(ani_colors))
print(*sorted(ani_colors))
print(len(bori_colors))
print(*sorted(bori_colors))
