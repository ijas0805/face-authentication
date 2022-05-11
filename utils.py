from settings import logger
from deepface import DeepFace
import shutil
import os
import settings

def adduser(img, username):
    if os.path.exists("db/img/'+username+'.png"):
        logger.info(f'"{username}" already exist. replacing image')

    # Coppy image to image folder as username file extention
    img.save('db/img/'+username+'.png')

    if os.path.exists("db/img/db/representations_vgg_face.pkl"):
        os.remove("db/img/db/representations_vgg_face.pkl")
    else:
        logger.info("The db does not exist") 

    # Create DB
    df = DeepFace.find(img_path = 'db/img/'+username+'.png', db_path = "db/img")

    # Move DB to DB file
    shutil.move('db/img/representations_vgg_face.pkl', 'db/img/db')

def verifyuser(img, username):

    img.save('call/img/'+username+'.png')
    df = DeepFace.find(img_path = 'call/img/'+username+'.png', db_path = "db/img/db", enforce_detection = False)
    logger.info(f'db matches{df}')
    try:
        for i in range(3):
            userpath = df['identity'][i]
            image_cosine = float(df['VGG-Face_cosine'][i])
            if userpath == 'db/img/'+username+'.png' and image_cosine<settings.MAX_COSIN:
                logger.info(f'Matched user "{userpath}"')
                return True
    except:
        logger.info(f'No user matched for "{username}"')
        return False
    return False

# img = Image.open('sample.jpg')
# adduser(img, 'myname')

