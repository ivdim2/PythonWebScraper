import re

def print_docs(page):
    ''' find all docs pdf gifs and jpeg on the webpage input and print '''
    print('[*] print_docs()')
    # regex to match on docs
    docs = re.findall(r'([^\"\']*docx|[^\"\']*pdf|[^\"\']*DOCX|[^\"\']*PDF)', page)
    # sort and print the docs
    docs.sort()
    print(f'[+] {len(docs)} Documents Found:')
    for doc in docs:
        print(doc)