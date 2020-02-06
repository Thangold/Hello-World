def frequency(l):
    unique_l = list(set(l))
    freq_list = [l.count(x) for x in unique_l]
    min_freq_list = [unique_l[x] for x in range(len(freq_list)) if freq_list[x] == min(freq_list)]
    max_freq_list = [unique_l[x] for x in range(len(freq_list)) if freq_list[x] == max(freq_list)]
    min_freq_list.sort()
    max_freq_list.sort()
    return (min_freq_list, max_freq_list)



def onehop(l):
    c = []
    for i in l:
          c.append(i[0])
          c.append(i[1])
    c = list(set(c))
    m = [0] * len(c)
    for i in range(len(c)):
      m[i] = [0] * len(c)
    for i in range(len(l)):
      m[l[i][0] - 1][l[i][1]-1] = 1
      res = []
    for i in range(len(c)):
        for j in range(len(c)):
          for k in range(len(c)):
            if (m[i][k] == 1 and m[k][j] == 1 and k !=i and k !=j and i != j and (i + 1, j + 1)  not in res):
                res.append(i + 1, j + 1)
    return res

#print(res)