import bcrypt
username = "inf2"
usernamebyte = bytes(username,encoding = "utf-8")
print(usernamebyte)

usernamehashed = bcrypt.hashpw(usernamebyte, bcrypt.gensalt())
print(usernamehashed)

password = b"ai310613855"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
psstr = str(hashed,encoding = "utf-8") # byte转str
psbyte = bytes(psstr,encoding = "utf-8") #str转syte
print(psstr)
print(psbyte)

if bcrypt.hashpw(password,hashed) == hashed:
    print("It Matches!")
else:
    print("It Does not Match :(")