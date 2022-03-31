import re
from icecream import ic
file = r"C:\Users\Administrator\Documents\全部消息记录.txt"
with open(file, 'r',encoding="utf-8") as f:
    for ff in  f.readlines():
        ic(re.match(r'[广西]',ff))
