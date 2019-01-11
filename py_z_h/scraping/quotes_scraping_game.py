import requests
import time
from csv import DictWriter, DictReader
from bs4 import BeautifulSoup
from random import randint

url = "http://quotes.toscrape.com"
quotes_list = []


def scrape_quotes(url):
    i = 1
    quotes_list = []
    while True:
        resp = requests.get(url + f"/page/{i}")
        print("Scraping " + url + f"/page/{i}")
        soup = BeautifulSoup(resp.text, "html.parser")
        quotes = soup.select(".quote")

        if len(quotes) == 0: break

        for quote in quotes:
            text = quote.find(class_="text").get_text()
            author = quote.find(class_="author").get_text()
            author_url = url + quote.find("a")["href"]
            quotes_list.append({"text": text, "author": author, "author_url": author_url})

        i += 1
    return quotes_list


def write_quotes(quotes_list):
    with open("quotes.csv", "w") as csv_file:
        csv_writer = DictWriter(csv_file,["text", "author", "author_url"])
        csv_writer.writeheader()
        for q in quotes_list:
            csv_writer.writerow({"text": q["text"],"author": q["author"],"author_url": q["author_url"]})


def read_quotes(name="quotes.csv"):
    try:
        with open(name, "r") as csv_file:
            csv_reader = DictReader(csv_file)
            quotes = list(csv_reader)
    except FileNotFoundError:
        print(f"{name} not found, scrapping..")
        quotes = scrape_quotes(url)
        write_quotes(quotes)
        # try to open again
        read_quotes()
    return quotes


def get_answer(author, guesses):
    answer = input("Who said this? Guesses remaining: " + str(guesses) + "\n")
    if answer == author:
        print("You've guessed, congrats!")
    return answer == author


def start_game(quotes):
    while True:
        guesses = 4
        r_quote = randint(0, len(quotes) - 1)
        author = quotes[r_quote]["author"]
        full_name = author.split()

        resp = requests.get(quotes[r_quote]["author_url"])
        soup = BeautifulSoup(resp.text, "html.parser")

        bio_info = soup.find(class_="author-born-date").get_text() + " " + soup.find(class_="author-born-location").get_text()

        hints = iter(["The author was born on " + bio_info, "The author's first name starts with " + full_name[0][0],
                 "The author's last name starts with " + full_name[-1][0]])

        print("Here's a quote: \n\n" + quotes[r_quote]["text"] + "\n\n")

        print(author)
        while not get_answer(author,guesses):
            try:
                print("Here's a hint: " + next(hints) + "\n")
            except:
                pass
            guesses -= 1
            if guesses == 0:
                print("You lost. The answer was " + author)
                break

        play_again = input("Play again? (y/n) ")
        if play_again.lower() != "y": break


quotes = read_quotes()
start_game(quotes)


