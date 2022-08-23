#1046 - Game Time

start_time,end_time=map(int,input().split())
if(start_time<end_time):
    time=end_time-start_time
else:
    time=end_time+24-start_time
print("O JOGO DUROU %d HORA(S)"%time)