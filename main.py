import sys
import sys
from urllib.request import urlopen, Request
import pdfkit
from bs4 import BeautifulSoup

def main(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(urlopen(req), features="html.parser")
    pdfkit.from_url(url, f"./saved_pages/{soup.title.string}.pdf")

if __name__ == '__main__':
    try:
        if(len(sys.argv) >= 2):
            for url in sys.argv[1:]:
                main(url)
        else:
            print("Please provide a single url as an argument.")
    except ValueError as e:
        print(e)

