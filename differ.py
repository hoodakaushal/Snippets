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


del_same("D:\\Org_Mod", "C:\\Users\\hooda\\Music\\")
