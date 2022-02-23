from bs4 import BeautifulSoup

import requests

site="https://lms.netacad.com/grade/report/grader/index.php?id="
id=0
site=site+str(id)

html = requests.get(site).content

soup=BeautifulSoup(html, 'html.parser')


print(soup.prettify())
