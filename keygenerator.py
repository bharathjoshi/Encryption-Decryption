import random 
def publickey():
	normal=range(32,127)
	shey=True
	while(shey):
	
		k=range(32,127)	
		random.shuffle(normal)
		juu=[]
		if any(normal[king]==k[king] for king in range(len(normal))):
			continue
		normal=map(lambda  x:4*x,normal)
		l=[-1 for x in range((len(normal)*2))]
		for k1 in range(len(normal)):
			random_no=random.randint(100,999-normal[k1])
			l[k1]=normal[k1]+random_no
			l[95+k1]=random_no
		l1=map(str,l)
		zee=''.join(l1)
		returning=[zee]
		private_=[-1 for x in range((len(normal)*2))]
		for var3 in range(len(normal)):	
			random2=random.randint(10,28)
			private_[var3]=normal[var3]-random2
			private_[95+var3]=random2
		l2=map(str,private_)
		zeee=''.join(l2)
		returning.append(zeee)
		return returning
		shey=False
	
if __name__=="__main__":
	val=publickey()
	print "public key is ",val[0],"\n"
	print "private key is",val[1],"\n"
