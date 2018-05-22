def dot( L, K ):
    if len[L]!=len[K]:
        return 0
    elif L == '' or L == []:
        return 0
    else:
        return sum(L[0]*K[0], L[1]*K[1], ect.)
    def dot(K, L):
   if len(K) != len(L):
      return 0

   return sum(i[0] * i[1] for i in zip(K, L))