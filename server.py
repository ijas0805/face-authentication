import io
import settings
from settings import logger
from PIL import Image
from fastapi import FastAPI, File
import uvicorn
import os
from utils import adduser, verifyuser

app = FastAPI()

@app.post('/api/adduser')
async def add_user(password: str, user_name: str, email: str, user_image: bytes = File(...)):
    if password == settings.ADD_USER_PASSWORD:
        user_name = user_name
        user_image = Image.open(io.BytesIO(user_image))
        if user_image == '': return {'result': 'Enter a username'}
        logger.info(f'Request to add "{user_name}"')
        try:
            result = adduser(user_image, user_name)
            resJson = {'result': result}
            return resJson
        except Exception as Error:
            logger.error(f'User not added due to error: {Error}')
            os.remove(f"db/img/{user_name}.png")
            resJson = {'result': f'Face not detected!!\nTry again'}
            return resJson
    else:
        logger.error(f"WRONG password {password}")
        return {'result': 'Access denied'}

@app.post('/api/verify')
async def verify_user(password: str, user_name: str, user_image: bytes = File(...)):
    if password == settings.USER_VERIFICATION_PASSWORD:
        user_name = user_name
        user_image = Image.open(io.BytesIO(user_image))
        logger.info(f'Request to verify "{user_name}"')
        try:
            user_from_db = verifyuser(user_image, user_name)
            if user_from_db:
                result = f"User '{user_name}' verified"
                logger.info(f'"{user_name}" verified')
            else:
                result = 'User not verified!!\nPlease try againe'
                logger.info(f'"{user_name}" not verified')
            resJson = {'result': f'{result}'}
            return resJson
        except Exception as Error:
            logger.error(f'User not verified due to error: {Error}')
            resJson = {'result': f'User not verified due to error'}
            return resJson
    else:
        logger.error(f"WRONG password {password}")
        return {'result': 'Access denied'}


if __name__ == "__main__":
    uvicorn.run(app, port=settings.PORT_NO, host=settings.HOST)
