import math
import random


def generate_otp()-> int:
    otp = math.floor(100000 + random.random() * 900000)
    return otp