import re

def print_emails(page):
    ''' find all emails pdf gifs and jpeg on the webpage input and print '''
    print('[*] print_emails()')
    # regex to match on emails
    emails = re.findall(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+', page)
    emails = list(set(emails))
    # sort and print the emails
    emails.sort()
    print(f'[+] {len(emails)} Emails Found:')
    for email in emails:
        print(email)