import requests 
from bs4 import BeautifulSoup

f = open("C:/Users/Administrator/Downloads/prod27.csv", 'r', encoding='utf-8')
f_new = open("C:/Users/Administrator/Downloads/prod28.csv", 'a', encoding='utf-8')
lines = f.readlines()
for line in lines:
    cookies = {

    }

    headers = {

    }
    search = line.split(",")[1].lstrip().rstrip().replace(" ","+")
    url = f"https://stlbikes.clientes.appsaigroup.com/cart/public/home?q%5Bname%5D={search}#"
    response = requests.get(url, cookies=cookies, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    img_tags = soup.find_all("img")
    image_urls = [img["src"] for img in img_tags]
    if any("upload" in url for url in image_urls):
        matching = [url for url in image_urls if "upload" in url]
        matching[0] = matching[0].replace(" ","%20")
        new_line = line.replace("http",matching[0])
        f_new.write(new_line)
        # print(new_line)
    else:
        f_new.write(line)
        # print(line)
f.close()
f_new.close()