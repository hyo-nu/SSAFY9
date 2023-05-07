import sys;sys.stdin=open('input.txt')
input = sys.stdin.readline

N,M = map(int,input().split())
site_dict = {}
for _ in range(N):
    site,password = input().split()
    site_dict.setdefault(site,password)

find_pass = [input().rstrip() for _ in range(M)]

for find in find_pass:
    print(site_dict[find])

