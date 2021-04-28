n=int(input('n= '))
Arr=[int(x) for x in input('Arr= ').split()]
min_swaps0=0
min_swaps1=0
l=0
for i in range(n): # case when 0s are shifted to right
	if(Arr[i]==0):
		min_swaps0+=l
	if(Arr[i]==1):
		l+=1
l=0
for i in range(n): # case when 1s are shifted to ritht
	if(Arr[i]==1):
		min_swaps1+=l
	if(Arr[i]==0):
		l+=1
min_swaps=min(min_swaps1,min_swaps0)
print(min_swaps)
