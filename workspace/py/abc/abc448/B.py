import sys

def solve():
    n,m = map(int, input().split())
    c = list(map(int, input().split()))
    l = [0] * m
    ans = 0
    for i in range (n):
        a,b = map(int, input().split())
        l[a-1] += b

    for i in range (m):
        if l[i] == c[i]:
            ans += c[i]
        elif l[i] > c[i]:
            ans += c[i]
        else:
            ans += l[i]
    print(ans)


if __name__ == "__main__":
    solve()
