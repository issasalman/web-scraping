import requests

from bs4 import BeautifulSoup


URL = "https://en.wikipedia.org/wiki/Egypt"


def  get_citations_needed_count(url):

    res  = requests.get(url)

    soup = BeautifulSoup(res.text, 'html.parser')

    result = soup.find_all( 'a', title = 'Wikipedia:Citation needed')

    return (len(result))

citation_paragraphs = []

def get_citations_needed_report(url):

    res  = requests.get(url)

    soup = BeautifulSoup(res.text, 'html.parser')

    result = soup.find_all('a', title='Wikipedia:Citation needed')


    for p in result:
        citation_paragraphs.append(p.parent.parent.parent.text)
 
    final_result= '\n\n'.join(citation_paragraphs)
    return final_result


print(get_citations_needed_report(URL))
sentence_count=get_citations_needed_count(URL)
print(f"The count of citations needed Is '{sentence_count}'")

import json

with open('all_jobs.json', 'w') as f:
    content = json.dumps(citation_paragraphs)
    f.write(content)
