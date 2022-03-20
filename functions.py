import os
import urllib.parse as urlparse
from urllib.parse import parse_qs
import re, bs4
import requests
from imdb import Cinemagoer
import pyperclip

ia = Cinemagoer()


def getIdFromUrl(link: str):
    if len(link) in [33, 19]:
        return link
    if "folders" in link or "file" in link:
        regex = r"https://drive\.google\.com/(drive)?/?u?/?\d?/?(mobile)?/?(file)?(folders)?/?d?/(?P<id>[-\w]+)[?+]?/?(w+)?"
        res = re.search(regex, link)
        if res is None:
            raise IndexError("GDrive ID not found.")
        return res.group("id")
    parsed = urlparse.urlparse(link)
    return parse_qs(parsed.query)["id"][0]


def size(id):
    os.chdir("D:\Games\Software\gclone")
    cmd = f"gclone size GC:{{{id}}}"

    output = os.popen(cmd).read()
    output = output.split()
    unit = output[6]
    if unit == "GiByte":
        unit = " GB"
    elif unit == "MiByte":
        unit = " MB"
    elif unit == "Byte":
        unit = " Byte"

    try:
        output = list(output[5])
    except:
        return "***ERROR CALC***"

    output = list(output[0:4])
    output = "".join(str(i) for i in output)
    if output == "0":
        output = "***ERROR CALC 0***"
    return output + unit


def make_request(url):
    return requests.get(url)


def name_of_file(url):
    if "uc?id=" in url:
        i_d = getIdFromUrl(url)
        url = "https://drive.google.com/file/d/" + i_d + "/view"
    req = make_request(url)
    soup = bs4.BeautifulSoup(req.text, "html.parser")
    name = str(soup.title).replace("<title>", "").replace("</title>", "")
    if name == "Meet Google Drive – One place for all your files":
        return "Error"
    name = name[:-15]
    return name.replace(".", " ")


def id_from_imdblink(url):
    pattern = re.compile(r"https?://(www\.)?imdb\.com/title/tt(\d+)/?")
    matches = pattern.finditer(url)
    for match in matches:
        return str(match.group(2))


def get_genre_list(imdb_movie_object):
    v = imdb_movie_object.get("genres")
    v = join = ", ".join(v)
    return v


# movie = ia.get_movie(id_from_imdblink("https://www.imdb.com/title/tt10872600/?ref_=hm_fanfav_tt_i_2_pd_fp1"))

# output = get_genre_list(movie)
# join = ', '.join(output)
# print(join)
