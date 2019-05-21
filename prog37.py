n,W=map(int,input().split())
vt=list(map(int,input().split()))
val1=list(map(int,input().split()))
ratio=[]
for i in range(n):
  ratio.append(val1[i]/vt[i])
cost=0
while W>=0 and len(ratio)>0:
  if W>=vt[ratio.index(max(ratio))]:
    cost+=val1[ratio.index(max(ratio))]
    W-=vt[ratio.index(max(ratio))]
  val1.pop(ratio.index(max(ratio)))
  vt.pop(ratio.index(max(ratio)))
  ratio.pop(ratio.index(max(ratio)))
print(cost)
