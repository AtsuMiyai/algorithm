N = int(input())
S = input()
A = [0]*(N+1)
H１ = [0]*N
H2 = [0]*N
h = 10**9+7


def RollingHash(text_):
    text = [0]*N
    text1 = [0]*N
    for i in range(N):
        text[i] = ord(text_[i])
        text1[N-1-i] = text[i]
    base = 1007
    t_len = len(text)
    a = 1
    for i in range(t_len+1):
        A[i] = a % h
        a = a*base % h
    for i in range(t_len):
        # 先頭からのhash値を計算していく。
        if i == 0:
            H１[i] = A[0]*text[i] % h
            H2[i] = A[0]*text1[i] % h
            continue
        H１[i] = (H１[i-1]*base % h+text[i] % h) % h
        H2[i] = (H2[i-1]*base % h+text1[i] % h) % h


RollingHash(S)


def kaibun2(x, y):  
    h = 10**9+7
    w1 = 0
    w2 = 0
    if (x == 0 and y == N-1):

        w1 = H1[y]
        w2 = H2[N-1-x]
    elif (x == 0):
        w1 = H1[y]
        w2 = (H2[N-1-x] % h-A[y-x+1]*H2[N-1-y-1] % h) % h

    elif (y == N-1):
        w1 = (H1[y] % h-A[y-x+1]*H1[x-1] % h) % h
        w2 = H2[N-1-x]
    else:
        w1 = (H1[y] % h-A[y-x+1]*H1[x-1] % h) % h
        w2 = (H2[N-1-x] % h-A[y-x+1]*H2[N-1-y-1] % h) % h
    if (w1 == w2):
        return 1
    else:
        return 0

