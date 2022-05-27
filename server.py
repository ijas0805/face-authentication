import io
import settings
from settings import logger
from PIL import Image
from fastapi import FastAPI, File
import uvicorn
from utils import adduser, verifyuser

app = FastAPI()

@app.post('/api/adduser')
async def add_user(password: str, user_name: str, email: str, user_image: bytes = File(...)):
    if password == settings.ADD_USER_PASSWORD:
        user_name = user_name
        user_image = Image.open(io.BytesIO(user_image))
        logger.info(f'Request to add "{user_name}"')
        try:
            adduser(user_image, user_name)
            logger.info(f'User "{user_name}" added')
            resJson = {'result': f'User "{user_name}" added'}
            return resJson
        except Exception as Error:
            logger.error(f'User not added due to error: {Error}')
            resJson = {'result': f'User not added due to error'}
            return resJson
    else:
        logger.error(f"WRONG password {password}")
        return "WRONG password"

@app.post('/api/verify')
async def verify_user(password: str, user_name: str, user_image: bytes = File(...)):
    if password == settings.USER_VERIFICATION_PASSWORD:
        user_name = user_name
        user_image = Image.open(io.BytesIO(user_image))
        logger.info(f'Request to verify "{user_name}"')
        try:
            user_from_db = verifyuser(user_image, user_name)
            if user_from_db:
                result = 'User verified'
                logger.info(f'"{user_name}" verified')
            else:
                result = 'User not verified'
                logger.info(f'"{user_name}" not verified')
            resJson = {'result': f'Msg: {result}'}
            return resJson
        except Exception as Error:
            logger.error(f'User not verified due to error: {Error}')
            resJson = {'result': f'User not verified due to error'}
            return resJson
    else:
        logger.error(f"WRONG password {password}")
        return "WRONG password"


if __name__ == "__main__":
    uvicorn.run(app, port=settings.PORT_NO, host=settings.HOST)
