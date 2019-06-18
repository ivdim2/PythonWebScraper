import re

def print_mailto(page):
    ''' find all mailto pdf gifs and jpeg on the webpage input and print '''
    print('[*] print_mailto()')
    # regex to match on mailto
    mailto = re.findall(r'mailto:[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+', page)
    # sort and print the mailto
    mailto.sort()
    print(f'[+] {len(mailto)} Mailto Email Found:')
    for email in mailto:
        print(email)