import logging

logging.basicConfig(filename="production.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

ADD_USER_PASSWORD = "pass"
USER_VERIFICATION_PASSWORD = "pass"
PORT_NO = 8000
HOST = '0.0.0.0'

MAX_COSIN = 2.4


