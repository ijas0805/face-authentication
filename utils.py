from settings import logger
from deepface import DeepFace
import shutil
import os
import settings
from hand_postures import hand_pose_verify

def adduser(img, username):
    if os.path.exists(f"db/img/{username}.png"):
        logger.info(f'"{username}" already exist')
        return f'Username already exists'

    # Coppy image to image folder as username file extention
    img.save('db/img/'+username+'.png')

    if os.path.exists("db/img/db/representations_vgg_face.pkl"):
        os.remove("db/img/db/representations_vgg_face.pkl")
        logger.info("Deleting db and creating new db") 
    else:
        logger.info("The db does not exist creating new db") 

    # Create DB
    df = DeepFace.find(img_path = 'db/img/'+username+'.png', db_path = "db/img")

    if os.path.exists(f"db/img/representations_vgg_face.pkl"):
        logger.info("representations_vgg_face created. Moving representations_vgg_face to db/img/db")
        # Move DB to DB file
        shutil.move('db/img/representations_vgg_face.pkl', 'db/img/db')
        logger.info(f'User "{username}" added')
        return f'User "{username}" added'
    else: 
        logger.error(f'representations_vgg_face not created. User "{username}" not added')
        return f'User "{username}" not added\nPlease try again'

def verifyuser(img, username, finger_count):

    pose_result = hand_pose_verify(img, finger_count)
    if not pose_result == True :
        logger.info(f"User '{username}' hand pose not verified")
        return pose_result

    img.save('call/img/'+username+'.png')
    df = DeepFace.find(img_path = 'call/img/'+username+'.png', db_path = "db/img/db", enforce_detection = False)
    logger.info(f'db matches{df}')
    try:
        for i in range(3):
            userpath = df['identity'][i]
            image_cosine = float(df['VGG-Face_cosine'][i])
            if userpath == 'db/img/'+username+'.png' and image_cosine<settings.MAX_COSIN:
                logger.info(f'Matched user "{userpath}"')
                return f"User '{username}' verified"
    except:
        logger.info(f'No user matched for "{username}"')
        logger.info(f'"{username}" not verified')
        return 'User not verified!!\nPlease try againe'
    logger.info(f'"{username}" not verified')
    return 'User not verified!!\nPlease try againe'

# img = Image.open('sample.jpg')
# adduser(img, 'myname')