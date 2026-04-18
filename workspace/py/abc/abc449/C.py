import sys

def solve():
    n, l, r = map(int, input().split())
    s = list(input())
    
    count = [0] * 26
    for c in s:
        count[ord(c) - ord('a')] += 1
    
    ans = 0

    for i in range(n):
        b = max(0, i-r)
        t = i-l
        if b <=t:
            c = s[i]
            ans += count[ord(c) - ord('a')] - 1

    print(ans)

if __name__ == "__main__":
    solve()
