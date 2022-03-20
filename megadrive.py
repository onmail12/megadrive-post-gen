from functions import *

while True:
    link = input("Link: ")
    while link == "" or not link.startswith("https://drive.google.com/"):
        link = input("Link: ")

    imdb = input("IMDb: ")
    while imdb == "" or not imdb.startswith("https://www.imdb.com/"):
        imdb = input("IMDb: ")
    try:
        id = getIdFromUrl(link)
    except:
        print("Drive ID not found")
        exit()
    imdbId = id_from_imdblink(imdb)
    movie = ia.get_movie(imdbId)
    genre = get_genre_list(movie)
    name = name_of_file(link)
    sizes = size(id)

    output = "`{}`\n:drive: {}\n\n **Size: {}**\n<{}>\n\n{}".format(
        genre, name, sizes, link, imdb
    )
    pyperclip.copy(output) #copies output to clipboard
    print("----------------------")
    print(output)
    print("----------------------")
