def PossibleAnswer(number):
    k=[]
    for i in range(10):
        k.append(number%4)
        number = number//4
    return k



def Correct(number):
    Answer = PossibleAnswer(number)
    Correct=list(range(10))
    #第1题
    Correct[0]=True
    #第2题
    if (Answer[1]+2)%4 == Answer[4]:
        Correct[1]=True
    else:
        Correct[1]=False
    #第3题
    if  Answer[2]==0 and Answer[2]!=Answer[5] and Answer[5]==Answer[1]==Answer[3]:
        Correct[2]=True
    elif  Answer[2]==1 and Answer[5]!=Answer[2] and Answer[2]==Answer[1]==Answer[3]:
        Correct[2]=True
    elif  Answer[2]==2 and Answer[1]!=Answer[5] and Answer[2]==Answer[5]==Answer[3]:
        Correct[2]=True
    elif  Answer[2]==3 and Answer[3]!=Answer[5] and Answer[2]==Answer[5]==Answer[1]:
        Correct[2]=True
    else:
        Correct[2]=False
    #第4题
    if  Answer[3]==0 and Answer[0]==Answer[4] and Answer[1]!=Answer[6] and Answer[0]!=Answer[8] and Answer[5]!=Answer[9]:
        Correct[3]=True
    elif  Answer[3]==1 and Answer[0]!=Answer[4] and Answer[1]==Answer[6] and Answer[0]!=Answer[8] and Answer[5]!=Answer[9]:
        Correct[3]=True
    elif  Answer[3]==2 and Answer[0]!=Answer[4] and Answer[1]!=Answer[6] and Answer[0]==Answer[8] and Answer[5]!=Answer[9]:
        Correct[3]=True
    elif  Answer[3]==3 and Answer[0]!=Answer[4] and Answer[1]!=Answer[6] and Answer[0]!=Answer[8] and Answer[5]==Answer[9]:
        Correct[3]=True
    else:
        Correct[3]=False
    #第5题
    if  Answer[4]==0 and Answer[4]==Answer[7] and Answer[4]!=Answer[3] and Answer[4]!=Answer[8] and Answer[4]!=Answer[6]:
        Correct[4]=True
    elif  Answer[4]==1 and Answer[4]!=Answer[7] and Answer[4]==Answer[3] and Answer[4]!=Answer[8] and Answer[4]!=Answer[6]:
        Correct[4]=True
    elif  Answer[4]==2 and Answer[4]!=Answer[7] and Answer[4]!=Answer[3] and Answer[4]==Answer[8] and Answer[4]!=Answer[6]:
        Correct[4]=True
    elif  Answer[4]==3 and Answer[4]!=Answer[7] and Answer[4]!=Answer[3] and Answer[4]!=Answer[8] and Answer[4]==Answer[6]:
        Correct[4]=True
    else:
        Correct[4]=False
    #第6题
    if  Answer[5]==0 and Answer[7]==Answer[1]==Answer[3] and (Answer[7]!=Answer[0] or Answer[7]!=Answer[5]) and (Answer[7]!=Answer[2] or Answer[7]!=Answer[9]) and (Answer[7]!=Answer[4] or Answer[7]!=Answer[8]):
        Correct[5]=True
    elif  Answer[5]==1 and (Answer[7]!=Answer[1] or Answer[7]!=Answer[3]) and Answer[7]==Answer[0]==Answer[5] and (Answer[7]!=Answer[2] or Answer[7]!=Answer[9]) and (Answer[7]!=Answer[4] or Answer[7]!=Answer[8]):
        Correct[5]=True
    elif  Answer[5]==2 and (Answer[7]!=Answer[1] or Answer[7]!=Answer[3]) and (Answer[7]!=Answer[0] or Answer[7]!=Answer[5]) and Answer[7]==Answer[2]==Answer[9] and (Answer[7]!=Answer[4] or Answer[7]!=Answer[8]):
        Correct[5]=True
    elif  Answer[5]==3 and (Answer[7]!=Answer[1] or Answer[7]!=Answer[3]) and (Answer[7]!=Answer[0] or Answer[7]!=Answer[5]) and (Answer[7]!=Answer[2] or Answer[7]!=Answer[9]) and Answer[7]==Answer[4]==Answer[8]:
        Correct[5]=True
    else:
        Correct[5]=False        
    #第7题
    if  Answer[6]==0 and Answer.count(2)<min(Answer.count(0),Answer.count(1),Answer.count(3)):
        Correct[6]=True
    elif  Answer[6]==1 and Answer.count(1)<min(Answer.count(0),Answer.count(2),Answer.count(3)):
        Correct[6]=True
    elif  Answer[6]==2 and Answer.count(0)<min(Answer.count(1),Answer.count(2),Answer.count(3)):
        Correct[6]=True
    elif  Answer[6]==3 and Answer.count(3)<min(Answer.count(0),Answer.count(1),Answer.count(2)):
        Correct[6]=True
    else:
        Correct[6]=False
    #第8题
    if  Answer[7]==0 and abs(Answer[6]-Answer[0])!=1 and abs(Answer[4]-Answer[0])==1 and abs(Answer[1]-Answer[0])==1 and abs(Answer[9]-Answer[0])==1:
        Correct[7]=True
    elif  Answer[7]==1 and abs(Answer[6]-Answer[0])==1 and abs(Answer[4]-Answer[0])!=1 and abs(Answer[1]-Answer[0])==1 and abs(Answer[9]-Answer[0])==1:
        Correct[7]=True
    elif  Answer[7]==2 and abs(Answer[6]-Answer[0])==1 and abs(Answer[4]-Answer[0])==1 and abs(Answer[1]-Answer[0])!=1 and abs(Answer[9]-Answer[0])==1:
        Correct[7]=True
    elif  Answer[7]==3 and abs(Answer[6]-Answer[0])==1 and abs(Answer[4]-Answer[0])==1 and abs(Answer[1]-Answer[0])==1 and abs(Answer[9]-Answer[0])!=1:
        Correct[7]=True
    else:
        Correct[7]=False
    #第9题
    if Answer[0]==Answer[5]:
        if  Answer[8]==0 and Answer[5]!=Answer[4] and Answer[9]==Answer[4] and Answer[1]==Answer[4] and Answer[8]==Answer[4]:
            Correct[8]=True
        elif  Answer[8]==1 and Answer[5]==Answer[4] and Answer[9]!=Answer[4] and Answer[1]==Answer[4] and Answer[8]==Answer[4]:
            Correct[8]=True
        elif  Answer[8]==2 and Answer[5]==Answer[4] and Answer[9]==Answer[4] and Answer[1]!=Answer[4] and Answer[8]==Answer[4]:
            Correct[8]=True
        elif  Answer[8]==3 and Answer[5]==Answer[4] and Answer[9]==Answer[4] and Answer[1]==Answer[4] and Answer[8]!=Answer[4]:
            Correct[8]=True
        else:
            Correct[8]=False
    else:
        if  Answer[8]==0 and Answer[5]==Answer[4] and Answer[9]!=Answer[4] and Answer[1]!=Answer[4] and Answer[8]!=Answer[4]:
            Correct[8]=True
        elif  Answer[8]==1 and Answer[5]!=Answer[4] and Answer[9]==Answer[4] and Answer[1]!=Answer[4] and Answer[8]!=Answer[4]:
            Correct[8]=True
        elif  Answer[8]==2 and Answer[5]!=Answer[4] and Answer[9]!=Answer[4] and Answer[1]==Answer[4] and Answer[8]!=Answer[4]:
            Correct[8]=True
        elif  Answer[8]==3 and Answer[5]!=Answer[4] and Answer[9]!=Answer[4] and Answer[1]!=Answer[4] and Answer[8]==Answer[4]:
            Correct[8]=True
        else:
            Correct[8]=False
    #第10题
    if  Answer[9]==0 and (max(Answer.count(0),Answer.count(1),Answer.count(2),Answer.count(3))-min(Answer.count(0),Answer.count(1),Answer.count(2),Answer.count(3)))==3:
        Correct[9]=True
    elif  Answer[9]==1 and (max(Answer.count(0),Answer.count(1),Answer.count(2),Answer.count(3))-min(Answer.count(0),Answer.count(1),Answer.count(2),Answer.count(3)))==2:
        Correct[9]=True
    elif  Answer[9]==2 and (max(Answer.count(0),Answer.count(1),Answer.count(2),Answer.count(3))-min(Answer.count(0),Answer.count(1),Answer.count(2),Answer.count(3)))==4:
        Correct[9]=True
    elif  Answer[9]==3 and (max(Answer.count(0),Answer.count(1),Answer.count(2),Answer.count(3))-min(Answer.count(0),Answer.count(1),Answer.count(2),Answer.count(3)))==1:
        Correct[9]=True
    else:
        Correct[9]=False        
    #返回结果
    return Correct    

number=4**10-1


for i in range(number):
    if Correct(i).count(True)==10:
       print(PossibleAnswer(i)) 
