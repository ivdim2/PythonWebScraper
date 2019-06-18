import sys, urllib.request

        
def wget(url):
    ''' Retrieve a webpage via its url, and return its contents'''
    print ("\n")
    print (f"Retrieving webpage {url}")
    # open url like a file, based on url instead of filename
    webpage = urllib.request.urlopen(url)
    # get webpage contents
    page_contents = webpage.read().decode() #Decode is done here so we dont decode it everytiem we cll the text.
    return page_contents

if __name__ == '__main__':
	main()
