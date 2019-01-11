from scrap_habr import html
from bs4 import BeautifulSoup
from csv import writer

data = BeautifulSoup(html,"html.parser")
articles = data.find_all("article")

with open("habr.csv","a") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["title", "link"])

    for article in articles:
        tag = article.select(".post__title a")[0]
        link = tag["href"]
        title = tag.text
        csv_writer.writerow([title, link])
        print(link, title)
        # print(article.select(".post__title a")[0]["href"])


# print(articles)
# print(html)