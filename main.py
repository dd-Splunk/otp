import os
from dotenv import load_dotenv
from time import sleep
import pyotp

"""
See: https://github.com/pyauth/pyotp
"""

load_dotenv()
SEED = os.getenv("SEED")
if SEED is None:
    raise Exception("No SEED specified. Aborting.")

totp = pyotp.TOTP(SEED)
try:
    totp.now()
except:
    print("Invalid SEED: not a base32 string")
    exit(1)

while True:
    print("Current OTP:", totp.now())
    sleep(10)
