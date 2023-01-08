def eq(let_1, let_2):  # compare the last letters
    return not(let_1 == let_2)


def space_clear(s):  # delete multiple spaces
    ans = ''
    tmp = 1
    for i in s:
        if tmp:
            ans += i
        if i == ' ':
            tmp = 1 - tmp
    return ans


s = input()  # input
ind = s.find('txt') + 3
a, b = s[:ind], s[(ind + 1):]
pairs = open(a, 'r')

ans = open(b, 'w')  # output file

for i in pairs.readlines():
    way_f1, way_f2 = i.rstrip().split()  # getting ways to scripts

    f1 = open(way_f1, 'r')
    f2 = open(way_f2, 'r')
    text_f1 = space_clear(f1.read().lower())  # getting text from scripts
    text_f2 = space_clear(f2.read().lower())

    n, m = len(text_f1) + 1, len(text_f2) + 1

    dp = [[0 for i in range(m)] for j in range(n)]   # the main list for the Levenshtein dist. calculation

    for k in range(1, n):   # start values of list
        dp[k][0] = k

    for j in range(1, m):
        dp[0][j] = j

    print(n, m)
    for k in range(1, n):  # dp realization
        for j in range(1, m):
            dp[k][j] = min(dp[k][j - 1] + 1, dp[k - 1][j] + 1, dp[k - 1][j - 1] + eq(text_f1[k - 1], text_f2[j - 1]))

    ans.write(str(dp[n - 1][m - 1] / max(n - 1, m - 1)) + '\n')  # output

    f1.close()
    f2.close()

pairs.close()
ans.close()
