import re
def find_lcsubstr(s1, s2):
    m=[[0 for i in range(len(s2)+1)] for j in range(len(s1)+1)]
    mmax = 0
    p = 0
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                m[i+1][j+1] = m[i][j]+1
                if m[i+1][j+1] > mmax:
                    mmax = m[i+1][j+1]
                    p=i+1
                    # print(m[i][j])
                    # print(p)
                    # print(i,j)
                    # T2:(A+C,B+C)
                    if s1[len(s1)-1] == s2[len(s2)-1] and abs(len(s1)-len(s2)) == abs(i-j):
                        sign = 'T2'
                    else:
                        sign = 'None'
    # T1:(C,A+C)
    if len(re.findall(s1, s2)) != 0:
        sign = 'T1'
    print((s1,s2,sign))
    # print(len(s1))
    # return s1[p-mmax:p], mmax
find_lcsubstr('xxxabcde','xxvvabcde')

