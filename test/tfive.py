import sys
print ("脚本名：", sys.argv[0])
if len(sys.argv) == 1:
  print ("你还没有输入参数")
for i in range(1, len(sys.argv)):
  print ("参数", i, sys.argv[i])
