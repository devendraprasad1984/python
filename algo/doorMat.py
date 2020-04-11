

n, m = map(int,"9 27".split())
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
# print(pattern)
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))


