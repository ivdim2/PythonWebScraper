import os
import urllib
import re
import shutil
import urllib.request
from urllib.parse import urlparse
import urllib

def download_images(page,url,dwd_dir):
    ''' find all images and download them '''   

    file_name = re.findall(r'[\"\']([^\"\']*.jpg|[^\"\']*.bmp|[^\"\']*.gif|[^\"\']*.jpeg|[^\"\']*.png|[^\"\']*.JPG)[\"\']',page,re.IGNORECASE)
    file_name.sort()


    try:
        os.mkdir(dwd_dir)
        print("Directory ",dwd_dir," Created ")
    except FileExistsError:
        print("Directory",dwd_dir," already exists")
        shutil.rmtree(dwd_dir)
        print("Directory",dwd_dir,"Removed")
        os.mkdir(dwd_dir)
        print("Directory",dwd_dir,"Created")
    
    print(f'[+] Trying to  Download {len(file_name)} images :')
    for image in file_name: #for each image in file_name to download the image
        print(f'[+] Trying to  Download {image} :')
        try:
             try:
                urllib.request.urlretrieve(url+image ,f'{dwd_dir}/{image}')
                print(f'[!] Download Succesful {image}')
             except:
                b = os.path.basename(urlparse(image).path)
                urllib.request.urlretrieve(url+image ,f'{dwd_dir}/attempt_{b}')  
                
        except:
            print(f'Was unable to download {image}')     