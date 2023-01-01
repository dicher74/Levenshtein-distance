def eq(let_1, let_2):  # compare the last letters
    return not(let_1 == let_2)


s = input()  # input
ind = s.find('txt') + 3
a, b = s[:ind], s[(ind + 1):]
pairs = open(a, 'r')

ans = open(b, 'w')  # output file

for i in pairs.readlines():
    way_f1, way_f2 = i.rstrip().split()  # getting ways to scripts

    f1 = open(way_f1, 'r')
    f2 = open(way_f2, 'r')
    text_f1 = f1.read()  # getting text from scripts
    text_f2 = f2.read()

    n, m = len(text_f1), len(text_f2)

    dp = [[0 for i in range(m)] for j in range(n)]   # the main list for the Levenshtein dist. calculation

    for i in range(n):  # dp realization
        for j in range(m):
            dp[i][j] = min(dp[i][j - 1] + 1, dp[i - 1][j] + 1, dp[i - 1][j - 1] + eq(text_f1[i], text_f2[j]))

    ans.write(str(dp[n - 1][m - 1]) + '\n')  # output

    f1.close()
    f2.close()

pairs.close()
ans.close()
