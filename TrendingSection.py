from selenium import webdriver
import pymysql.cursors

Connection = pymysql.connect("localhost", 'root', "sarveshsj25", 'WS')
cursor = Connection.cursor()

driver = webdriver.Chrome('/home/sarvesh/Desktop/Tools/Chromedrivers for Selenium /chromedriver')
driver.get("https://www.youtube.com/feed/trending")
Title = driver.find_elements_by_xpath('//*[@id="video-title"]/yt-formatted-string')
Uploader = driver.find_elements_by_xpath('//*[@id="text"]/a')
allTitles = []
allUploader = []
for title in Title:
    allTitles.append(title.text)
for uploader in Uploader:
    if uploader.text != "Karuveppilai Samayal" and uploader.text != "":
        allUploader.append(uploader.text)
for i in range(len(allTitles)):
    cursor.execute("Insert into TRENDING(TITLE,UPLOADER) VALUES(\"%s\",\"%s\") " % (allTitles[i].replace('"',' '), allUploader[i]))
    Connection.commit()
