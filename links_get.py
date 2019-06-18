import re

def print_links(page):
    ''' find all hyperlinks on the webpage and  '''
    print('[*] print_links()')
    # regex to match on hyperlinks
    links = re.findall(r'href=[\'"]?([^\'" >]+)', page)
    # sort and print the links
    links.sort()
    print(f'[+] {len(links)} Hyperlinks has been found:')
    for link in links:
        print(link)