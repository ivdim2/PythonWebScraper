import re

def print_phonenumbers(page):
    ''' find all phonenumbers pdf gifs and jpeg on the webpage input and print '''
    print('[*] print_phonenumbers()')
    # regex to match on phonenumbers
    phonenumbers = re.findall(r'''\d{4}[-\s]?\d{3}[-\s]?\d{4}|\+44[-\s]?\d{3}[-\s]?\d{7}|\+44[-\s\(]?[\d{1}\(]?[\d{1}\)]?[\)]?[\d]{3,10}[-\s]?[\d]{3}[-\s]?[\d]{4}''',page)
    # sort and print the phonenumbers
    phonenumbers.sort()
    print(f'[+] {len(phonenumbers)} Phonehumers :')
    for phone in phonenumbers :
        print(phone)