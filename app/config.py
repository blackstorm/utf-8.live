import os
import configparser

POSTS_PER_PAGE = 10

# 初始化配置
config = configparser.ConfigParser()
dir = os.path.abspath(os.path.dirname(__file__))
config.read(os.path.join(dir,"ini/app.ini"))

def get_confg():
    return config