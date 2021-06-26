import requests
import bs4

def get_all_links(frm):
    ret_links = []
    page_text = requests.get(frm).content
    soup = bs4.BeautifulSoup(page_text, features="html.parser")
    links = soup.find_all("a", {"class":"title hasvidtable"})
    for i in links:
        ret_links.append(i['href'])
    return ret_links

def get_lyrics(frm):
    ret = []
    page_text = requests.get(frm).content
    soup = bs4.BeautifulSoup(page_text, features="html.parser")
    lyrics = soup.find_all("p",{"class":"verse"})
    for i in lyrics:
        ret.append(i.get_text())
    return "\n".join(ret)

def get_filename(url):
    return url.split("/")[-1].replace(".html",".txt")


def main():
    url = "https://www.metrolyrics.com/abba-lyrics.html"
    for i in get_all_links(url):
        print(f"Downloading {i}")
        lyrics = get_lyrics(i)
        fname = get_filename(i)
        f = open(fname, "w")
        f.write(lyrics)
        f.close()
main()
