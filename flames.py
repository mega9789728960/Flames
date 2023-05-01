name=input("enter the name: ")
name1=input("enter the name: ")
list1=[]
for i in name:
	list1.append(i)
list2=[]
for j in name1:
	list2.append(j)
fb=list1.copy()
fs=list2.copy()
for i in list1:
	if i in list2:
		fb.remove(i)
		list2.remove(i)
s=len(fb)+len(list2)
j=0
f=["f","l","a","m","e","s"]*s
d=s-1
for i in range(4):
	if j==0:
		t=f[s-1]
		f[s-1]=0
		for ye in range(len(f)):
			if f[ye]==t:
				f[ye]=0
				j=1
	else:
		b=0
		while b<s:
			if f[d+1]!=0:
				b+=1
			d+=1
		c=f[d]
		f[d]=0
		for k in range(len(f)):
			if f[k]==c:
				f[k]=0
q=[]
for k in range(len(f)):
	if f[k]!=0:
		q.append(f[k])
gr=q[:2]
te={1:"f",2:"l",3:"a",4:"m",5:"e",6:"s"}
te1={"f":1,"l":2,"a":3,"m":4,"e":5,"s":6}
fd=te1[c]
pr=gr[0]
pv=gr[1]
if te1[pr]<fd and te1[pv]>fd:
	if s%2==0:
		tr=gr[1]
	else:
		tr=(gr[0])
elif te1[pr]<fd and te1[pv]<fd:
	if s%2==0:
		tr=(gr[0])
	else:
		tr=(gr[1])
elif te1[pr]>fd and te1[pr]>fd:
	if s%2==0:
		tr=gr[0]
	else:
		tr=gr[1]
final5={"f":"friends","l":"lovers","a":"affection","m":"marrige","e":"enemy","s":"sister"}
print(final5[tr])