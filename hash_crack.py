import sys
import hashlib

def dict_attack(passwd_hash):
    """Checks password hash against a dictionary of common passwords"""
    # list of passwords
    file = open("passwords.txt", "r",encoding="latin-1")
    dic = file.readlines()

    # create list of corresponding md5 hashes using a list comprehension
    stripped_dic = [x.rstrip() for x in dic]
    hashes = [hashlib.md5(password.encode("latin-1")).hexdigest() for password in stripped_dic] 
    dic1=dict(zip(hashes,stripped_dic))
    rainbow = {hashes:dic for (dic,hashes) in dic1.items()} 
    print (f'[*] Cracking hash: {passwd_hash}')
    passwd_found =  dic1.get(passwd_hash)
    ### replace None with a lookup using .get() on rainbow
                    
    if passwd_found:
        print (f'[+] Password recovered: {passwd_found} ')
    else:
        print (f'[-] Password not recovered')
    
    file.close()     


   
    
if __name__ == '__main__':
	main()
