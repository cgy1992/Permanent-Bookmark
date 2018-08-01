import sys
import sys
from urllib.request import urlopen, Request
import pdfkit
from bs4 import BeautifulSoup

def main(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'}, features="html.parser")
    soup = BeautifulSoup(urlopen(req))
    pdfkit.from_url(url, f"./saved_pages/{soup.title.string}.pdf")

if __name__ == '__main__':
    try:
        if(len(sys.argv) >= 2):
            for i in range(1, len(sys.argv)):
                main(sys.argv[i])
        else:
            print("Please provide a single url as an argument.")
    except ValueError as e:
        print(e)

