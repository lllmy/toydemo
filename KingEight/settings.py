import pymongo
import os

# 协议格式：
RET = {
    "code": 0,
    "msg": "",
    "data": {},
}

# 数据配置
mongo_client = pymongo.MongoClient(host="127.0.0.1", port=27017)
MONGO_DB = mongo_client["KingEight"]

# 资源目录配置
IMAGE_PATH = "Images"
MUSIC_PATH = "Music"
QRCODE_PATH = "QRcode"

# 数据采集配置
XPP_URL = "http://m.ximalaya.com/tracks/%s.json"


#创建二维码配置
QR_URL = "http://qr.liantu.com/api.php?text=%s"