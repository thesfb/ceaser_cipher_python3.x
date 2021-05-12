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


text = str(input("Enter the text to be encrpyted using ceaser cipher: "))

i = int(input("Enter the shift number (0-26): "))

ceaser(text, i)


input("press any key to exit")




#use this to print the cipher text with all 26 shifts
###########################
# for i in range(len(string.ascii_uppercase)):
# 	ceaser(text, i)
# 	sleep(1)
###########################



