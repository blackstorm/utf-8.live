# 验证用户名是否正确，如果正确返回 true 否则 返回 false
from app import config
import bcrypt

def user_login(username,password):
    cf = config.get_confg()
    utf8 = "utf-8"
    cf_username_hashed = bytes(cf.get("admin","username"), encoding = utf8)
    cf_password_hashed = bytes(cf.get("admin","password"), encoding = utf8)
    form_usname_bytes = bytes(username, encoding = utf8)
    form_password_bytes = bytes(password, encoding = utf8)
    if bcrypt.hashpw(form_usname_bytes,cf_username_hashed) == \
            cf_username_hashed and bcrypt.hashpw(form_password_bytes, cf_password_hashed)\
            == cf_password_hashed:
        return True
    else:
        return False
