f = open("bypass2FALIST.txt", "w")
print("Welcome To 2FA LIST GENERATOR\n\n")
print("to know you target 2fa code length \n")
print("sign up account and reset password if code for\n")
print("example = 4526 then length is 4 \n\n")
NG = input("How many you want to generate :")

tfal = input("Enter 2FA code Length:")
for i in range(0,int(NG)):
	x = str(i)
	l = len(x)
	while(l < int(tfal)):
		x= "0"+ x
		l = len(x)
	print(x)
	f.write(x+"\n")
print("Done ! Happy hunting");
f.close()