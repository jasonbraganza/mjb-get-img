"""
Write a tool, which will take an url as input, and download all the images 
from that url/webpage (https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

steps i think i need to do

1. get a url from the command line. ensure only one site comes in at at time (for now) 
- done!

2. sanitise the url? check for basic errors 
- managed to do basic sanity checks using a regex from an old django validator.
https://github.com/django/django/blob/stable/1.3.x/django/core/validators.py#L45
- done

3. use requests to get the web content

4. use bs4 to check for image links

5. create an images subfolder. if one exists, use it

6. download the images and save them to the images subfolder

"""

import re
import sys

import requests
from bs4 import BeautifulSoup


def main():
    if len(sys.argv) > 2:
        print("Please enter only one webpage link at a time.")
    elif len(sys.argv) == 1:
        print("Please enter a webpage link, to get images from.")
    else:
        raw_url = sys.argv[1]
        if sanitise_url(raw_url):
            raw_page = get_page_from_requests(raw_url)
            if raw_page:
                print(raw_page.status_code)
            else:
                print("Uh-oh, something is wrong.")

        else:
            print(
                f"{raw_url} is not a well formed domain name.\nPlease enter a valid url."
            )


def sanitise_url(raw_url):
    """
    Validates urls using an old django validator from https://github.com/django/django/blob/stable/1.3.x/django/core/validators.py#L45

    TODO someday - use the new django validator

    :param raw_url: a url string
    :type raw_url: string
    :return: true or false
    :rtype: boolean
    """
    regex = re.compile(
        r"^(?:http|ftp)s?://"  # http:// or https://
        r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|"  # domain...
        r"localhost|"  # localhost...
        r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # ...or ip
        r"(?::\d+)?"  # optional port
        r"(?:/?|[/?]\S+)$",
        re.IGNORECASE,
    )

    return re.match(regex, raw_url)


def get_page_from_requests(raw_url):
    try:
        r = requests.get(raw_url)
        return r
    except:
        return None


if __name__ == "__main__":
    main()
