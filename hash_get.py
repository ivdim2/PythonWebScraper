#hash_get.py
import re
import sys
import hashlib
from hash_crack import dict_attack

def print_hashes(page):
	''' find all hashes pdf gifs and jpeg on the webpage input and print '''
	print('[*] print_hashes()')
# regex to match on hashes
	hashes = re.findall(r'[0-9a-f]{32}', page)
# sort and print the hashes
	hashes.sort()
	print(f'[+] {len(hashes)} Hashes Found:')
	for hash in hashes:
		print(hash)
		dict_attack(hash)
