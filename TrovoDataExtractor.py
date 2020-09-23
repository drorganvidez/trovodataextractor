from bs4 import BeautifulSoup
import time
import datetime
import os
import sys
from os import system, name 
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

# Vars
streamerURL = "alexropi"
url = "https://trovo.live/" + streamerURL

def greeting():
    print("Trovo Data Extractor | Version 1.0 | GPL v3 License")
    print("https://github.com/drorganvidez/trovodataextractor\n")

def clear(): 
  
    if name == 'nt': 
        _ = system('cls') 
  
    else: 
        _ = system('clear')

    greeting()

def write_in_file(file_name,value):
    file = open(file_name, "w")
    file.write(value)
    file.close()

def extract_value(soup,tag):
    span = soup.find("span", attrs={tag:True})
    items = span.text
    sep = ' '
    return items.split(sep, 1)[0]

#Start loop
def loopit():

    # Greeting
    greeting()

    # Open ChromeWeb Driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    print("\nOpening Google Chrome helper window, please wait...")

    driver.get(url)

    while True:
        
        try:
            time.sleep(1)
            html = None

            html = driver.page_source
            soup = BeautifulSoup(html,"html.parser")

            # Viewers
            p = soup.find("p",{"class","viewer"})
            spans_p = cat_button = p.find_all("span")
            viewers = spans_p[0].text.split(' ', 1)[0]

            # Followers
            div = soup.find("div",{"class","feature-wrap"})
            cat_button = div.find_all("button")
            button = cat_button[3]
            spans = button.find_all("span")
            followers = spans[1].text
            write_in_file("TrovoFollowerCount.txt",followers)

            # Console print
            clear()
            print(str(viewers) + " viewers | " + str(followers) + " followers")

        except selenium.common.exceptions.WebDriverException:
            print("\nChrome window closed. You must leave the window open for the program to work.")
            print("Thank you for using Trovo Data Extractor. See u soon.\n")
            break

# Main
loopit()