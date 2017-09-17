from urllib.request import urlopen as uopen
from bs4 import BeautifulSoup as soup
from PyQt5 import Qt
import sys
from time import sleep

class CricketScore:
    def getScore(self,your_team):

        request = uopen("https://www.cricbuzz.com")
        html_code = request.read();
        request.close()
        soup_page = soup(html_code,"html.parser")

        matches = soup_page.findAll("div",{"class":"cb-col cb-col-25 cb-mtch-blk"})
        l = len(matches)
        c = c1 = 0
        for i in range(l):
            if(your_team in matches[i].a["title"]):
                team = matches[i].a["title"]
                str1 = matches[i].div.text
                c1 = 1
                for j in str1:
                    if j.isdigit():
                        msg = matches[i].div.text
                        c = 1
                        break
                if(c==0):
                    msg = "Match not Started Yet!!!"
                    break
            if(c1==1):
                break

        if(c1==0):
            team = your_team
            msg = "Match Not Found!!!"
        app = Qt.QApplication(sys.argv)
        systemtray = Qt.QSystemTrayIcon(app)
        systemtray.show()
        systemtray.showMessage(team, msg)
