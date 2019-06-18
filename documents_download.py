import os
import urllib
import re
import shutil
import urllib.request
from urllib.parse import urlparse

def download_documents(page,url,dwd_dir):
    ''' find all documents and download them '''   

    file_name = re.findall(r'([^\"\']*docx|[^\"\']*pdf|[^\"\']*DOCX|[^\"\']*PDF)',page,re.IGNORECASE)
    file_name.sort()

    # regex to match on documents # Think this could b optimized !

    print(f'[+] Trying to  Download {len(file_name)} documents :')
    for doc in file_name: #for each doc in file_name to download the doc
        print(f'[+] Trying to  Download {doc} :')
        try:
            try:
                urllib.request.urlretrieve(url+doc ,f'{dwd_dir}/{doc}')
            except:
              print(f"Trying to download with basename {doc}")
              base = os.path.basename(urlparse(doc))
              urllib.request.urlretrieve(url+doc ,f'{dwd_dir}/attempt_{base}')
        except:
               print(f'Was unable to download {doc}') 


