import sys
import bcrypt

print("\n----------generate_bcrypt_str-----------\n")
if len(sys.argv) == 1:
    print("您需要填写参数如：\n$ Python generate_bcrypt_str.py arg1 arg2 agr3 ...")
for i in range(1, len(sys.argv)):
    arg = sys.argv[i]
    arg_bytes = bytes(arg, encoding="utf-8")
    encrypt = bcrypt.hashpw(arg_bytes, bcrypt.gensalt())
    encrypt_str = str(encrypt,encoding="utf-8")
    print (i, arg,":",encrypt_str)
print("\n------------------end-------------------\n")