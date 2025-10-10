n = int(input())
p = list(map(int, input().split()))
p.sort(reverse=True)

tourist_score = sum(p[i] for i in range(0,n,2))

blade_score= sum(p[i] for i in range(1,n,2))


if tourist_score> blade_score:
    print("Tourist")
else:
    print("Blad")
