import configparser
import os

config = configparser.ConfigParser()
dir = os.path.abspath(os.path.dirname(__file__))
print(os.path.join(dir,"../ini/app.ini"))
config.read(os.path.join(dir,"../ini/app.ini"))
section = config.sections()
print(section)

