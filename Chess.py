import cv2
import numpy as np
import time
img=np.zeros((760,760,3),np.uint8)
Win1=0
Win2=0
def start():
    global chessboard
    global player
    global step
    chessboard=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    player=1
    step=0
    #file=open("AIplay.csv","w")
    cv2.rectangle(img,(0,0),(760,760),(0,255,255),-1)
    for x in range(18):
        for y in range (18):
            cv2.rectangle(img,(20+40*x,20+40*y),(60+40*x,60+40*y),(0,0,0),1)
    for x in range(3):
        for y in range(3):
            cv2.circle(img,(140+240*x,140+240*y),4,(0,0,0),-1)
start()
def getwinner():
    global chessboard
    for x in range(15):
        for y in range(19):
            WinnerInX1=0
            WinnerInX2=0
            WinnerInY1=0
            WinnerInY2=0
            for z in range(5):
                if chessboard[x+z][y]==1:
                    WinnerInX1+=1
                if chessboard[x+z][y]==2:
                    WinnerInX2+=1
                if chessboard[y][x+z]==1:
                    WinnerInY1+=1
                if chessboard[y][x+z]==2:
                    WinnerInY2+=1
            if WinnerInX1==5:
                return 1
            elif WinnerInX2==5:
                return 2
            if WinnerInY1==5:
                return 1
            elif WinnerInY2==5:
                return 2
    for x in range(15):
        for y in range(15):
            WinnerInA1=0
            WinnerInA2=0
            WinnerInB1=0
            WinnerInB2=0
            for z in range(5):
                if chessboard[x+z][y+z]==1:
                    WinnerInA1+=1
                if chessboard[x+z][y+z]==2:
                    WinnerInA2+=1
                if chessboard[x+4-z][y+z]==1:
                    WinnerInB1+=1
                if chessboard[x+4-z][y+z]==2:
                    WinnerInB2+=1
            if WinnerInA1==5:
                return 1
            elif WinnerInA2==5:
                return 2
            if WinnerInB1==5:
                return 1
            elif WinnerInB2==5:
                return 2
    return 0
def put_chess(event,x,y,flags,param):
    global player
    global step
    if event==cv2.EVENT_LBUTTONDOWN:
        for X in range(19):
            for Y in range(19):
                if x>40*X and x<40+40*X and y>40*Y and y<40+40*Y:
                    if chessboard[X][Y]==0:
                        if player==1:
                            cv2.circle(img,(20+40*X,20+40*Y),15,(0,0,0),-1)
                            chessboard[X][Y]=1
                            #place=str(X)+","+str(Y)+","
                            #file.write(place)
                            step+=1
                            player=2
                        elif player==2:
                            cv2.circle(img,(20+40*X,20+40*Y),15,(255,255,255),-1)
                            chessboard[X][Y]=2
                            #place=str(X)+","+str(Y)+","
                            #file.write(place)
                            step+=1
                            player=1
cv2.namedWindow('image')
cv2.setMouseCallback('image',put_chess)
while(1): 
    winner=getwinner()
    cv2.imshow('image',img)
    if cv2.waitKey(20)&0xFF==27:
        #file.write("\n")
        #file.close()
        break
    if winner!=0:
        print("winner is",winner)
        '''cv2.waitKey(1)
        if winner==1:
            Win1+=1
            cv2.putText(img,'BLACK WIN',(50,400),cv2.FONT_HERSHEY_SIMPLEX,4,(0,0,255),1)
        else:
            Win2+=1
            cv2.putText(img,'WHITE WIN',(50,400),cv2.FONT_HERSHEY_SIMPLEX,4,(0,0,255),1)
        #cv2.putText(img,'BLACK VS WHITE',(50,400),cv2.FONT_HERSHEY_SIMPLEX,3,(0,0,255),1)
        #cv2.putText(img,str(Win1)+"    "+str(Win2),(50,500),cv2.FONT_HERSHEY_SIMPLEX,5,(0,0,255),1)
        time.sleep(3)'''
        while(2):
            start()
            if cv2.waitKey(1) & 0xFF == ord(' '):
                break
        #file.write("\n")
        #file.close()
        #break
cv2.destroyAllWindows()
