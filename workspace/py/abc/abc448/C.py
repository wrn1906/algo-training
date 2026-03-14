import sys
import copy

def solve():
    n,q = map(int, input().split())
    a = list(map(int, input().split()))
    aa = sorted([(j,i) for i,j in enumerate(a)])
    for i in range(q):
        k = int(input())
        q = list(map(int, input().split()))
        for i,j in aa:
            if j not in q:
                print(i)
                break


if __name__ == "__main__":
    solve()
