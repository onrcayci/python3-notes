"""
Web Scraping with BeautifulSoup

Install the library first: pip install bs4

BeautifulSoup lets us navigate through HTML with Python.

Beautiful Soupc does NOT download HTML - for this, we need the requests module!

- Parsing and Navigating HTML

BeautifulSoup(html_string, "html.parser") - parse HTML.

Once parsed, there are several was to navigate:
    By Tag Name
    Using find - returns one matching tag
    Using find_all - returns a list of matching tags

- Navigating with CSS Selectors

select - returns a list of elements matching a CSS selector

- Accessing Data in Elements

get_text - access the inner text in an element
name - tag name
attrs - dictionary attributes
You can also access attribute values using brackets!

- Navigating with Beautiful Soup

via Tags

    parent / parents
    cotnents
    next_sibling / next_siblings
    previous_sibling / previous_siblings

via Searching

    find_parent / find_parents
    find_next_sibling / find_next_siblings
    find_previous_sibling / find_previous_siblings
"""
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, "html.parser")
print(soup)                                 # prints the parsed version of HTML
print(soup.body)                            # prints on the body of the HTML
print(soup.find('div'))                     # prints out the first div it finds
print(soup.find_all(class_='special'))      # returns a list of elements with class='special'