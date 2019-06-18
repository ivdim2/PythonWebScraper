import re

def print_images(page):
    ''' find all images pdf gifs and jpeg on the webpage input and print '''
    print('[*] print_images()')
    # regex to match on images # Think this could b optimized !
    images = re.findall(r'[\"\']([^\"\']*.jpg|[^\"\']*.bmp|[^\"\']*.gif|[^\"\']*.jpeg|[^\"\']*.png|[^\"\']*.JPG)[\"\']',page,re.IGNORECASE)
    # sort and print the images
    images.sort()

    #prints the lenth of images 
    print(f'[+] {len(images)} images has been found :')
    for image in images: #for each image in images to print the image
        print(image)

            