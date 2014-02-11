"""
Just Another Caesar Cipher
I wanted to make it unicode so it's harder to decipher, but it's always giving me unicode errors.
After much frustruation, I put it in to normal ascii mode.
"""

__author__ = "Fayang Pan"
__date__ = "7/24/13"

import random,re
"""
1. read the txt file, assume it's written in ASCII code (128)
2. randomly generate a list of keys
"""

class Cipher():
	def __init__(self):
		pass

	def encrypt(self,text,secret):
		encryptedText = list(text)
		for key in secret:
			for i in range(key[0],len(encryptedText)):
				num = (ord(encryptedText[i])+key[1])%128
				print num
				encryptedText[i] = chr(num)
		return "".join(encryptedText)

	def decrypt(self,text,secret):
		decryptedText = list(text)
		print decryptedText
		for key in secret:
			for i in range(key[0],len(decryptedText)):
				num = (ord(decryptedText[i])-key[1])%128
				print num
				decryptedText[i] = chr(num)
		return "".join(decryptedText)

	def secretParser(self,secStr):
		secret = []
		pattern = re.compile(r'\d+')
		numlist = pattern.findall(secStr)
		for i in range(0,len(numlist),2):
			secret.append((int(numlist[i]),int(numlist[i+1])))
		return secret

cipher = Cipher()


class RandNumGen():
	def __init__(self):
		pass

	def placeGen(self,text):
		return random.randint(0,len(text)-1)

	def numGen(self):
		return random.randint(0,128)

if __name__ == "__main__":
	prompt = raw_input("Welcome to the ultimate Caesar Cipher! \nPlease enter '1' for encrypt mode or '2' for decrypt mode: ")
	while True:
		try:
			assert(int(prompt) and 0<int(prompt) and int(prompt)<3)
			break
		except ValueError, AssertionError:
			prompt = raw_input("Invalid input. Please enter '1' for encrypt mode or '2' for decrypt mode: " )
	if prompt is '1':
		stdin = raw_input("Encrypt Mode: please enter your text here: ")
		secret = []
		for i in range(min(((len(stdin)/10)+1),20)):
			secret.append((RandNumGen().placeGen(stdin),RandNumGen().numGen()))
		writer = open("encryptedText.txt", 'w')
		outputStr = "Your input text was: " + stdin  + "\nYour output string is: " \
	                    + cipher.encrypt(stdin,secret) + "\nYour key is:" + str(secret)
		print outputStr
		writer.write(outputStr)
		writer.close()
		print "Your secret key is: " + str(secret) +", and your encrypted text is saved in encryptedText.txt"
	else:
		stdin = raw_input("Decrypt Mode: please enter your text here: ")
		secret = raw_input("Decrypt Mode: Pleae enter your key here: ")
		try:
			secret = cipher.secretParser(secret)
		except IndexError:
			print "invalid key, please review it and try again."
			raise IOError, "Invalid key input"
		else:
			writer = open("decryptedText.txt", 'w')
			outputStr = "Your input text was: " + stdin  + "\nYour output string is: " \
		                    + cipher.decrypt(stdin,cipher.secretParser(str(secret))) + "\nYour key was:" + str(secret)
			print cipher.secretParser(str(secret))
			writer.write(outputStr)
			writer.close()
			print "Your secret key was: " + str(secret) +", and your decrypted text is saved in decryptedText.txt"
