from enum import Enum
from datetime import timedelta

class Money(Enum):
   brl = timedelta(days = 7)
   ust = timedelta(days = 30)
   bnb = timedelta(days = 180)
   pvu = timedelta(days = 360)