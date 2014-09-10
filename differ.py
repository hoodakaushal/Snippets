__author__ = 'hooda'

import os

import flatten


# Delete files from folder1 that are also in folder2
def del_same(folder1, folder2):
    files1 = flatten.listfiles(folder1)
    files2 = flatten.listfiles(folder2)
    # print(files2)
    files2 = getnames(files2)
    print(files2)

    for file in files1:
        if (getname(file)) in files2:
            os.remove(file)


def getnames(files):
    names = []
    for file in files:
        names += [getname(file)]
    return names


def getname(file):
    return file.split("\\")[-1]


def acount(folder):
    files = getnames(flatten.listfiles(folder))
    artists = {}
    for file in files:
        artist = file.split("-")[0]
        if not artist in artists.keys():
            artists[artist] = 1
        else:
            artists[artist] += 1
    artist_counts = []
    for artist in artists.keys():
        artist_counts += [[artist, artists[artist]]]
    final = sorted(artist_counts, key=mykey)
    for entry in final:
        print(entry)
    
    
def mykey(pair):
    return -1 * pair[1]


acount("C:\\Users\\hooda\\Music\\")