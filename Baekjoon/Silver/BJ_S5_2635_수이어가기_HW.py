one = int(input())
two = one//2
Max = []

while one >= two:
    result = [one]
    tmp_o , tmp_t = one,two
    while tmp_t >= 0:
        tmp_o, tmp_t = tmp_t, (tmp_o-tmp_t)
        result.append(tmp_o)
    two += 1
    if len(Max) < len(result):
        Max = result

print(len(Max))
print(*Max)







