import sys
reload(sys)  
sys.setdefaultencoding('gbk')  

import re
from urllib2 import urlopen, Request

import pdfkit
from bs4 import BeautifulSoup

def main(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(urlopen(req), features="html.parser")
    file_name = '1.pdf'#soup.title.string.replace(":", "--") + ".pdf"
    path_wk = 'D:/wkhtmltopdf/bin/wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf = path_wk)
    pdfkit.from_url(url, './%s' % file_name, configuration=config)

if __name__ == '__main__':
    try:
        if(len(sys.argv) >= 2):
            for url in sys.argv[1:]:
                main(url)
        else:
            print("Please provide a single url as an argument.")
    except ValueError as e:
        print(e)

