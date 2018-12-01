def decrypting(enclave):
	full_list=map(chr,range(32,127))
	private_key=enclave[1]
	privatekey_list=[]
	for var2 in range(len(str(private_key))):
	                privatekey_list.append(str(str(private_key)[var2]))
	privatekey_list_1=[str(private_key)[i:i+3] for i in range(0,95*3,3)]
	privatekey_list_2=[str(private_key)[z:z+2] for z in range(285,474,2)]
	privatekey_list=privatekey_list_1+privatekey_list_2
	for var3 in range(len(privatekey_list_1)):
		privatekey_list[var3]=str(int(privatekey_list_1[var3])+int(privatekey_list_2[var3]))
	privatekey_list=privatekey_list[0:95]
	privatekey_list=map(lambda x :int(x)/4 ,privatekey_list)
	dic={}
	for var4 in range(len(privatekey_list)):
		dic[privatekey_list[var4]]=var4
	output=[]
	for var5 in enclave[0]:
		for var6 in range(len(full_list)):
			if var5==full_list[var6]:
				output.append(full_list[dic[var6+32]])
	decrypted_message=''.join(output)
	return decrypted_message
print 
print "enter the encrypted message"
en=raw_input()
print "enter the private  key"
puk=input()
print decrypting([en,puk])
print
		
