#coding: UTF-8

f = open('sample3.txt')
f2 = open("extract4.txt","w")
line = 'aaa'
count = 1
flag = 0
while line:
  line = f.readline()
  if '@' in line:
    line = f.readline()
    if '@' in line:
      while not u'件のリツイート'.encode('utf-8') in line:
        line = f.readline()
        flag = 1
      if flag == 1:
        flag = 0
        continue
    print '[%d]' %count
    f2.write('[%d]' %count)
    while not u'件のリツイート'.encode('utf-8') in line:
      #if not line.startswith(" \r\n") or line.startswith("\r\n"):
      if not line.strip() == '':
        print line
        f2.write(line)
      line = f.readline()
    count=count+1
f.close
f2.close
