import getpass as gpt
import platform as plt
import subprocess as sbp
import tbin
from pyfiglet import Figlet
cstm = Figlet(font = 'graffiti')
print(cstm.renderText("zWR417H"))
print("						 [Login Encrypter]")
print("\n")




usn = input("\nEnter Your Username : ")

psd = gpt.getpass("\nEnter Your Password : ")


print("\n  					    Encrypting....\n")
tbin.sk(10)
plft = plt.system()

if plft == "Windows":

	sbp.call("cls", stdout=sbp.PIPE, shell=True)
	print("\nEncrypted Text\n")
else:
	sbp.call("clear", stdout=sbp.PIPE, shell=True)
	print("\nEncrypted Text\n")


sake = usn.encode('utf-16', 'strict')

fake = psd.encode('utf-16', 'strict')

print(sake)

print("\n")

print(fake)

print("\nCopy these encrypted Username and Password to autologin.py file ...!\n\n")