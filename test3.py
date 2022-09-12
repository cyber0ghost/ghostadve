from webbrowser import get
import requests
from bs4 import BeautifulSoup




def getimg(url, name):
#send get request
    response = requests.get(url)

    html_page = BeautifulSoup(response.text, 'html.parser')

    images = html_page.find_all("img")

    for index, image in enumerate(images):
        image_url= image.get("src")      #img src value
    
        image_extension= image_url.split(".")[-1]       #get image extension

    #get image data
        image_bytes = requests.get(image_url).content
    
        if image_bytes:
        #write the image data
            with open(f"{name}.{image_extension}", "wb") as file:
                file.write(image_bytes)


