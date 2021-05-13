import string
from time import *
import collections
		
		

	
	

def ceaser(rotate_str, num_to_rotate):
	upper = collections.deque(string.ascii_uppercase)
	lower = collections.deque(string.ascii_lowercase)
	upper.rotate(num_to_rotate)

	lower.rotate(num_to_rotate)
	upper = ''.join(list(upper))
	lower = ''.join(list(lower))
		
	print (rotate_str.translate(str.maketrans(string.ascii_uppercase, upper)).translate(str.maketrans(string.ascii_lowercase, lower)))

def ceaser_usage():
		
	text = str(input("Enter the text to be encrpyted using ceaser cipher: "))

	try:
		i = int(input("Enter the shift number (0-26): "))
	except ValueError:
		print("Enter a valid number!!")
	finally:
		ceaser(text, i)
def decipher_ceaser(rotate_str, num_to_rotate):
	upper = collections.deque(string.ascii_uppercase)
	lower = collections.deque(string.ascii_lowercase)
	upper.rotate(num_to_rotate)
	lower.rotate(num_to_rotate)

	upper = ''.join(list(upper))
	lower = ''.join(list(lower))
		
	print (rotate_str.translate(str.maketrans(string.ascii_uppercase, upper)).translate(str.maketrans(string.ascii_lowercase, lower)))

def decipher_ceaser_usage():
		
	text = str(input("Enter the text to decipher: "))

	i = int(input("Enter the shift: "))

	main_i = 26-i

	decipher_ceaser(text,main_i)


def brute_ceaser():

	text = str(input("Enter the cipher: "))
	for i in range(len(string.ascii_uppercase)):
		ceaser(text, i)
		sleep(.5)


def main_screen():

	print("Welcome to Ceaser Cipher toolkit!")

	print("Select a tool---")

	use = str(input("Press 'A' for Creating a cipher, Press 'B' for decrypting a cipher, Press 'C' for brute forcing a cipher, Press 'X' to exit: "))

	if use == 'A':
		ceaser_usage()
	elif use == 'B':
		decipher_ceaser_usage()
	elif use == 'C':
		brute_ceaser()

	elif use == 'X':
		exit()

	else:
		print("Enter a valid option!!!!")


main_screen()


again = str(input("Press Y for re-creation, Press 'X' to exit: "))

if again == 'Y':
	main_screen()

elif again == 'X':
	exit()



