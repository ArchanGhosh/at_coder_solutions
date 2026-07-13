def chk(happ):
  
  for h in happ:
    if h>=0:
      return "No"
    
  return "Yes"
  

n = int(input())
happ = list(map(int, input().split()))

print(chk(happ))
