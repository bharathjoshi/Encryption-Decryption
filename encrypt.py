import random
def fun(enclave):
	
		public_key=enclave[1]
		publickey_list=[]
		for var1 in range(len(str(public_key))):
			publickey_list.append(str(str(public_key)[var1]))
		decode=[publickey_list[var2:var2+3] for var2 in range(0,(len(publickey_list)),3)]
		decode=map(lambda x : ''.join(x),decode)
		for var3  in range(95):
			decode[var3]=str(abs(int(decode[var3])-int(decode[95+var3])))
		decode=decode[:95]
		decode=map(lambda x :int((int(x)/4)),decode)
		output = []
		full_list=map(lambda x : chr(x),range(32,127))
		s={}
		for var4 in range(len(full_list)):
			s[var4]=decode[var4]
		for characters in enclave[0]:
			for var5 in range(len(full_list)):
				if full_list[var5]==characters:	
					output.append(full_list[s[var5]-32])
		encrypted_msg="".join(output)
		return encrypted_msg
		
		
if __name__=="__main__":
	enclave= fun([raw_input("Enter the message.I assure you that your information is safe!!!"),input("Enter public key : ")])
	print "\n", "Encypted data is ",enclave,"\n"
