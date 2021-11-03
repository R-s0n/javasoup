# JavaSoup - Modern Web Scraping

This library returns the HTML of a Single Page Application (SPA) after the page has loaded.  This HTML can then be passed to BeautifulSoup for parsing.

#### !! WARNING: This library requires node, npm, and puppeteer to work !!
##### !! If the method runs and nothing is returned, this is MOST LIKELY the issue !!

##### Install JavaScript Components (on Kali):

`sudo apt-get install -y nodejs npm`

`npm i puppeteer`

### Library Overview

The traditional method of web scraping in Python w/ requests and BeautifulSoup isn't effective for more modern pages and SPAs.  This library dynamically generates a JavaScript file that uses puppeteer to fully load the page and return the HTML that is dynamicaly generated in the Document Object Model (DOM).

The primary method, get_soup, accepts a full URL as a string and returns the page's content as a string.

Typical Workflow (requests/BeautifulSoup):

`res = requests.get('http://example.com')`

`soup = BeautifulSoup(res.text, 'html.parser')`

New Workflow w/ javasoup:

`from javasoup import get_soup`

`soup = BeautifulSoup(get_soup('http://example.com'), 'html.parser')`

### Execution Process

1. Creates the necessary JavaScript file in the current working directory (MUST HAVE WRITE PRIVILEGES)
2. Runs that JavaScript file using the URL provided and stores the value returned
3. Deletes the temporary JavaScript file
4. Returns the HTML content

### Install

#### After JavaScript components have been installed, javasoup can be downloaded through pip

`pip install javasoup`
