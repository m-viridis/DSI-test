import requests
from bs4 import BeautifulSoup

#TELL PYTHON WHERE TO RETRIEVE DATA & MAKE IT A VARIABLE
url = "https://www.businessoffashion.com/articles/retail/ssense-job-cuts/" #copy paste your article url here
page = requests.get(url)

#FUNCTION TO: PARSE DATA W BSOUP, REMOVE CODE/TAGS, RETURN DATA
def remove_tags(html):
    soup = BeautifulSoup(page.content, "html.parser")

    for data in soup(['style', 'script']):
        data.decompose()
    
    return ' '.join(soup.stripped_strings) #blank space between '' is telling join to join the strings with a space.

#PRINT THE ARTICLE SANS HTML CODE
print(remove_tags(page.content))