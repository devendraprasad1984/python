def solution(p, c):
    num = p
    arr = []
    while True:
        num = num - c
        arr += [num]
        if num < 0: break
    return len(arr[:-1]), arr[:-1]


def chunkIt(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0
    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg
    return out


p, c = 5, 3
print(solution(p, c))
print(chunkIt(range(p),c))
