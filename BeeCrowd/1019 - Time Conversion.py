value=int(input())
hours=value//3600
minutes=value%3600//60
seconds=(value%3600)%60
print("%d:%d:%d"%(hours,minutes,seconds))
