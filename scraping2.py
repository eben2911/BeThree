from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from datetime import datetime
import urllib.request
import json


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.imdb.com/search/title/?genres=action&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=DM4S90RJKTH0QBJ0YD76&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_1")

film = []
i = 1

now = datetime.now()
waktu = now.strftime("%d %B %Y %H:%M:%S")

while i <= 100:   
    for parrent in driver.find_elements_by_class_name("mode-advanced"):
        print(parrent.text.split("\n"))
        for img in parrent.find_elements_by_tag_name("img"):
            # print(img.get_attribute("src")) 
            # urllib.request.urlretrieve(img.get_attribute("src"), str(i)+".png")
            i = i+1
            film.append({
            "Rank": parrent.text.split("\n")[0].split(".")[0],
            "Judul": parrent.text.split("\n")[0].split(". ")[1].split(" (")[0],
            "Link_judul": parrent.find_element_by_tag_name("a").get_attribute("href"),
            "Durasi": parrent.text.split("\n")[1].split(" | ")[1],
            "Rating": parrent.text.split("\n")[2].split(" ")[0],
            "Direktor": parrent.text.split("\n")[5].split(": ")[1].split(" | ")[0],
            "Image": img.get_attribute("src"),
            "Waktu_scrapping":waktu
            })

    try:
        driver.find_element_by_class_name("desc").find_element_by_partial_link_text("Next").click()
    except NoSuchElementException as e:
        break;

hasil_scraping = open("hasilscraping.json", "w")
json.dump(film, hasil_scraping, indent = 6)
hasil_scraping.close()
driver.quit()