n, m = map(int, input().split())

cl, sz = [], []

for _ in range(n):
    a, b = map(int, input().split())
    cl.append(a)
    sz.append(b)


def chk(n, m, cl, sz):
  max_dct = {}
  
  for i in range(len(cl)):
    if cl[i] not in max_dct:
      max_dct[cl[i]] = sz[i]
    else:
      max_dct[cl[i]] = max(sz[i], max_dct[cl[i]])
  
  fl = []
  
  for color in range(1, m + 1):
    fl.append(str(max_dct.get(color, -1)))

  return " ".join(fl)
    
  


print(chk(n, m, cl, sz))
    
