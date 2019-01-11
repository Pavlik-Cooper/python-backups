import requests
import time
from csv import writer
from bs4 import BeautifulSoup

url = "https://www.rithmschool.com"
articles_list = []
i = 1
while True:
    time.sleep(1)
    resp = requests.get(url + f"/blog?page={i}")
    soup = BeautifulSoup(resp.text, "html.parser")
    articles = soup.find_all("article")
    if articles is None or len(articles) == 0: break
    articles_list.extend(articles)
    i += 1


with open("rithmschool.csv", "w") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["title", "link", "time"])

    for article in articles_list:
        tag = article.select(".section-heading a")[0]
        title = tag.get_text()
        link = url + tag["href"]
        time = article.find("time")["datetime"]
        csv_writer.writerow([title, link, time])
        print(title, link, time)

