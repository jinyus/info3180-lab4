import os
from os import walk
from app import app

def getPhotos():
    rootdir = os.getcwd()
    allphotos=[]
    for dirpath, dirname, filename in walk(app.config["UPLOAD_FOLDER"]):
        allphotos += filename
        allphotos.remove(".gitkeep")
    return allphotos