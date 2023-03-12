import bs4
import requests

url = "https://www.zensiren.or.jp/nwide-info/"
res = requests.get(url)
soup = bs4.BeautifulSoup(res.text, "html.parser")
anchors = soup.find_all("a")
ret = ""

for anchor in anchors:
    if (href := anchor.get("href")) and href.startswith("https://www.zensiren.or.jp/archives/area/"):
        res_area = requests.get(href)
        soup_area = bs4.BeautifulSoup(res_area.text, "html.parser")
        soup_area_tr = soup_area.find_all("tr")
        for school in soup_area_tr:
            ret += ",".join(['"' + i.text + '"' for i in school.find_all("td")]) + "\n"

with open("list.csv", "w+") as fw:
    fw.write(ret)
