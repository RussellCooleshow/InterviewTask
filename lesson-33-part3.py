from urllib import request
import sys


myUrl = "https://pp.userapi.com/c834400/v834400897/e4b3/7h-TAdu_EoM.jpg"
myFile = "/Users/RuslanKuleshov/Desktop/python try/mykartinka.jpg"

try:
    print("Start downloading file from:" + myUrl)
    request.urlretrieve(myUrl, myFile)
except Exception:
    print("AHTUNG!!")
    print(sys.exc_info()[1])
    exit()

print("File downloaded and saved at " + myFile)