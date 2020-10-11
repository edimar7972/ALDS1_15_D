import heapq
from heapq import heapify, heappush, heappop 

def soma(l):
	soma=0
	for i in range (len(l)):
		soma += l[i]
	return soma
	
def frequencia(A):
	f=[]
	l=[]
	l.append(A[0])
	cont=1
	for i in range(1,len(A)):
		if A[i] == A[i-1]:
			cont+=1
		else:
			l.append(A[i])
	for i in range(len(l)):
		f.append(A.count(l[i]))
	i=0
	j=0
	dic={}
	while i < len (l):
		dic[l[i]]=f[i]
		i+=1
	a=soma(f)
	v=[]
	for i in range (len(l)):
		b=(f[i]*100)//a
		v.append(b)
	heapq.heapify(v)
	return v

class NovaCel:
	def __init__(self,esquerda,direita):
		self.esquerda = esquerda
		self.direita = direita
		
def huffman(A,f,n):
	if len(A) == 1:
		return 1
	Q= frequencia(aux)
	for i in range (1,n-1):
		x=	heapq.heappop(Q)
		y = heapq.heappop(Q)
		z = NovaCel(x,y) 
		heapq.heappush(Q,x+y)
	return heapq.heappop(Q)+1


A= input()                   
aux=[]
for i in range(len(A)):
	aux.append(A[i])
aux.sort()
f=frequencia(aux)
n=len(f)
huffman(aux,f,n)
frequencia(A)
print(huffman(A,f,n))
