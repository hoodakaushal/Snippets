__author__ = 'hooda'

# Take input a folder path, and for each folder in that path, extract all the files that match a given extension
# Rename all the files as : Folder/FolderName/File.ext to FolderName - File.exe
# Put all the files in a seperate folder.

import os
import shutil


# Full path of every single file in the given folder. (ie, files in subdirectories, sub-subdirectories ...)
def listfiles(folder):
    if not folder[-1:] == "\\":
        folder += "\\"
    if not os.path.exists(folder):
        return []
    subdirs = []
    files = []
    for path in os.listdir(folder):
        path = folder + path
        if os.path.isdir(path):
            subdirs += [path]
        else:
            files += [path]
    for subdir in subdirs:
        files += listfiles(subdir)
    return files


# Take input a folder path (source), and for each folder in that path, extract all the files that match a given extension
# Rename all the files as : Folder/FolderName/File.ext to FolderName - File.exe
# Put all the files in a seperate folder (dest)
# *args is the list of extensions (without the leading .)
# Will not work for an entire partition (ie, source = "C:")
def flatten(source, dest, *args):
    if not dest[-1:] == "\\":
        dest += "\\"
    if not os.path.exists(dest):
        os.mkdir(dest)
    files = listfiles(source)
    for file in files:
        if (len(args) > 0 and extension(file) in args) or (len(args) == 0):
            newpath = dest + hyphenise(file)
            print(newpath)
            # print(file, newpath)
            shutil.copyfile(file, newpath)


def extension(file):
    return file.split(".")[-1]


def hyphenise(file):
    file = file.split("\\")
    filename = file[-1]
    foldername = file[-2]
    return foldername + "-" + filename


def listex(folder):
    files = listfiles(folder)
    exts = []
    for file in files:
        e = extension(file)
        if e not in exts:
            exts += [e]
    exts.sort()
    print(exts)


    # source = "D:\\Org\\"
    # d = "D:\\Org_Mod"
    # flatten(source, d, 'mp3', 'm4a')
    # #listex(source)