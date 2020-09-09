"""
Write a tool, which will take an url as input, and download all the images 
from that url/webpage (https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

steps i think i need to do

1. get a url from the command line. ensure only one site comes in at at time (for now)
2. sanitise it? check for basic errors
3. use requests to get the web content
4. use bs4 to check for image links
5. create an images subfolder. if one exists, use it
6. download the images and save them to the images subfolder
"""

import sys

import requests
from bs4 import BeautifulSoup


def main():
    if len(sys.argv) > 2:
        print("Please enter only one webpage link at a time.")
    elif len(sys.argv) == 1:
        print("Please enter a webpage link, to get images from.")
    else:
        print(f"number of command line arguments given: {len(sys.argv)}")
        print(f"Arguments are: {sys.argv=}")


if __name__ == "__main__":
    main()
