import requests
from bs4 import BeautifulSoup
import csv

date = input("Please enter a Date in the following format mm/dd/yyyy:")
page = requests.get(f"https://www.yallakora.com/match-center/%D9%85%D8%B1%D9%83%D8%B2-%D8%A7%D9%84%D9%85%D8%A8%D8%A7%D8%B1%D9%8A%D8%A7%D8%AA?date={date}#days")

def main(page):
    src = page.content
    soup = BeautifulSoup(src, "lxml")
    matched = []

    champion = soup.find_all
main(page)