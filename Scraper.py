import sys,re,os
from webpage_get import wget 
from links_get  import print_links 
from images_get import print_images
from documents_get import print_docs
from phonenumbers_get import print_phonenumbers
from emails_get import print_emails
from mailto_get import print_mailto
from hash_get import print_hashes
from image_download import download_images
from documents_download import download_documents


def main():
    # Checks the amount of arguments provided.
    if len(sys.argv) != 3: #if the length is not = to 3 print the message
        print('[-] Usage:Scraper.py "URL" "Folder"')
        return
    
    dwd_dir = sys.argv[2]  #Varible that is taken for the name of the directory
    url = sys.argv[1]  #Varible that is taken to get the url
    page = wget(url)   #Varaible used  to call wget function to get the page. 
    

    print("\n")
    print("---------- Getting all the HyperLinks-----------")
    print_links(page) #Gets all the links from the webpage
    print("\n")
    print("---------- Getting all the Images-----------")
    print_images(page)  #Gets all the Images from the webpage
    print("\n")
    print("---------- Getting all the Documents-----------")
    print_docs(page)  #Gets all the Documents from the webpage
    print("\n")
    print("---------- Getting all the phonemumbers-----------")  
    print_phonenumbers(page) #Gets all the Phonenumbers from the webpage.
    print("\n")
    print("---------- Getting all the emails-----------")  
    print_emails(page) #Gets all the emails from the webpage.
    print("\n")
    print("---------- Getting all Mailto email-----------")  
    print_mailto(page) #Gets all the mailto emails from the webpage.
    print("\n")
    print("---------- Getting and Trying to Crack all Hashes-----------")  
    print_hashes(page) #Gets all the hashes and tries to crack them from the webpage.
    print("\n")
    print("---------- Getting and Trying to Download all the Images-----------")  
    download_images(page,url,dwd_dir) #Downlaod all the Images  from the webpage.
    print("\n")
    print("---------- Getting and Trying to Download all the Documents-----------")  
    download_documents(page,url,dwd_dir) #Downlaod all the Documents from the webpage.
    

if __name__ == '__main__':
    main()
