#five chess CvC
import cv2
import numpy as np
import time
import random
img=np.zeros((760,760,3),np.uint8)
chessboard=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
player=1
step=0
file=open("AIplay.csv","w")
cv2.rectangle(img,(0,0),(760,760),(0,255,255),-1)
for x in range(18):
    for y in range (18):
        cv2.rectangle(img,(20+40*x,20+40*y),(60+40*x,60+40*y),(0,0,0),1)
for x in range(3):
    for y in range(3):
        cv2.circle(img,(140+240*x,140+240*y),4,(0,0,0),-1)
def getwinner():
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
def putchess(x,y,a):
    global player
    global step
    if a==1:
        b=2
    if a==2:
        b=1
    if chessboard[x][y]==0 and player==a:
        cv2.circle(img,(20+40*x,20+40*y),15,((b-1)*255,(b-1)*255,(b-1)*255),-1)
        chessboard[x][y]=a
        place=str(x)+","+str(y)+","
        file.write(place)
        print(place)
        step+=1
        player=b
def AIplay(p):
    if p==1:
        q=2
    if p==2:
        q=1
    global player
    global step
    #win4
    for x in range(15):
        for y in range(19):
            WinnerInX=0
            WinnerInY=0
            for z in range(5):
                if chessboard[x+z][y]==p:
                    WinnerInX+=1
                if chessboard[x+z][y]==q:
                    WinnerInX-=1
                if chessboard[y][x+z]==p:
                    WinnerInY+=1
                if chessboard[y][x+z]==q:
                    WinnerInY-=1
            if WinnerInX==4:
                for z in range(5):
                    putchess(x+z,y,p)
            elif WinnerInY==4:
                for z in range(5):
                    putchess(y,x+z,p)
    for x in range(15):
        for y in range(15):
            WinnerInA=0
            WinnerInB=0
            for z in range(5):
                if chessboard[x+z][y+z]==p:
                    WinnerInA+=1
                if chessboard[x+z][y+z]==q:
                    WinnerInA-=1
                if chessboard[x+4-z][y+z]==p:
                    WinnerInB+=1
                if chessboard[x+4-z][y+z]==q:
                    WinnerInB-=1
            if WinnerInA==4:
                for z in range(5):
                    putchess(x+z,y+z,p)
            elif WinnerInB==4:
                for z in range(5):
                    putchess(x+4-z,y+z,p)
    #lose4
    for x in range(15):
        for y in range(19):
            WinnerInX=0
            WinnerInY=0
            for z in range(5):
                if chessboard[x+z][y]==q:
                    WinnerInX+=1
                if chessboard[x+z][y]==p:
                    WinnerInX-=1
                if chessboard[y][x+z]==q:
                    WinnerInY+=1
                if chessboard[y][x+z]==p:
                    WinnerInY-=1
            if WinnerInX==4:
                for z in range(5):
                    putchess(x+z,y,p)
            elif WinnerInY==4:
                for z in range(5):
                    putchess(y,x+z,p)
    for x in range(15):
        for y in range(15):
            WinnerInA=0
            WinnerInB=0
            for z in range(5):
                if chessboard[x+z][y+z]==q:
                    WinnerInA+=1
                if chessboard[x+z][y+z]==p:
                    WinnerInA-=1
                if chessboard[x+4-z][y+z]==q:
                    WinnerInB+=1
                if chessboard[x+4-z][y+z]==p:
                    WinnerInB-=1
            if WinnerInA==4:
                for z in range(5):
                    putchess(x+z,y+z,p)
            elif WinnerInB==4:
                for z in range(5):
                    putchess(x+4-z,y+z,p)
    #win3
    for x in range(14):
        for y in range(19):
            if chessboard[x][y]!=q and chessboard[x+5][y]!=q:
                WinnerInX=0
                for z in range(4):
                    if chessboard[x+z+1][y]==p:
                        WinnerInX+=1
                    if chessboard[x+z+1][y]==q:
                        WinnerInX-=1
                if WinnerInX==3:
                    for z in range(4):
                        putchess(x+z+1,y,p)
            if chessboard[y][x]!=q and chessboard[y][x+5]!=q:
                WinnerInY=0
                for z in range(4):
                    if chessboard[y][x+z+1]==p:
                        WinnerInY+=1
                    if chessboard[y][x+z+1]==q:
                        WinnerInY-=1
                if WinnerInY==3:
                    for z in range(4):
                        putchess(y,x+z+1,p)
    for x in range(14):
        for y in range(14):
            if chessboard[x][y]!=q and chessboard[x+5][y+5]!=q:
                WinnerInA=0
                for z in range(4):
                    if chessboard[x+z+1][y+z+1]==p:
                        WinnerInA+=1
                    if chessboard[x+z+1][y+z+1]==q:
                        WinnerInA-=1
                if WinnerInA==3:
                    for z in range(4):
                        putchess(x+z+1,y+z+1,p)
            if chessboard[x+5][y]!=q and chessboard[x][y+5]!=q:
                WinnerInB=0
                for z in range(4):
                    if chessboard[x-z+4][y+z+1]==p:
                        WinnerInB+=1
                    if chessboard[x-z+4][y+z+1]==q:
                        WinnerInB-=1
                if WinnerInB==3:
                    for z in range(4):
                        putchess(x-z+4,y+z+1,p)
    #lose3
    for x in range(14):
        for y in range(19):
            if chessboard[x][y]!=p and chessboard[x+5][y]!=p:
                WinnerInX=0
                for z in range(4):
                    if chessboard[x+z+1][y]==q:
                        WinnerInX+=1
                    if chessboard[x+z+1][y]==p:
                        WinnerInX-=1
                if WinnerInX==3:
                    if chessboard[x+2][y]==q and chessboard[x+3][y]==q:
                        if random.randint(0,1)==1:
                            if chessboard[x+1][y]==q:
                                putchess(x,y,p)
                            else:
                                putchess(x+1,y,p)
                        else:
                            if chessboard[x+4][y]==q:
                                putchess(x+5,y,p)
                            else:
                                putchess(x+4,y,p)
                    else:
                        if random.randint(0,1)==1:
                            for z in range(2):
                                putchess(x+z+2,y,p)
                        else:
                            if random.randint(0,1)==1:
                                putchess(x,y,p)
                            else:
                                putchess(x+5,y,p)
            if chessboard[y][x]!=p and chessboard[y][x+5]!=p:
                WinnerInY=0
                for z in range(4):
                    if chessboard[y][x+z+1]==q:
                        WinnerInY+=1
                    if chessboard[y][x+z+1]==p:
                        WinnerInY-=1
                    if WinnerInY==3:
                        if chessboard[y][x+2]==q and chessboard[y][x+3]==q:
                            if random.randint(0,1)==1:
                                if chessboard[y][x+1]==q:
                                    putchess(y,x,p)
                                else:
                                    putchess(y,x+1,p)
                            else:
                                if chessboard[y][x+4]==q:
                                    putchess(y,x+5,p)
                                else:
                                    putchess(y,x+4,p)
                        else:
                            if random.randint(0,1)==1:
                                for z in range(2):
                                    putchess(y,x+z+2,p)
                            else:
                                if random.randint(0,1)==1:
                                    putchess(y,x,p)
                                else:
                                    putchess(y,x+5,p)
    for x in range(14):
        for y in range(14):
            if chessboard[x][y]!=p and chessboard[x+5][y+5]!=p:
                WinnerInA=0
                for z in range(4):
                    if chessboard[x+z+1][y+z+1]==q:
                        WinnerInA+=1
                    if chessboard[x+z+1][y+z+1]==p:
                        WinnerInA-=1
                if WinnerInA==3:
                    if chessboard[x+2][y+2]==q and chessboard[x+3][y+3]==q:
                        if random.randint(0,1)==1:
                            if chessboard[x+1][y+1]==q:
                                putchess(x,y,p)
                            else:
                                putchess(x+1,y+1,p)
                        else:
                            if chessboard[x+4][y+4]==q:
                                putchess(x+5,y+5,p)
                            else:
                                putchess(x+4,y+4,p)
                    else:
                        if random.randint(0,1)==1:
                            for z in range(2):
                                putchess(x+z+2,y+z+2,p)
                        else:
                            if random.randint(0,1)==1:
                                putchess(x,y,p)
                            else:
                                putchess(x+5,y+5,p)
            if chessboard[x+5][y]!=p and chessboard[x][y+5]!=p:
                WinnerInB=0
                for z in range(4):
                    if chessboard[x-z+4][y+z+1]==q:
                        WinnerInB+=1
                    if chessboard[x-z+4][y+z+1]==p:
                        WinnerInB-=1
                if WinnerInB==3:
                    if chessboard[x+2][y+3]==q and chessboard[x+3][y+2]==q:
                        if random.randint(0,1)==1:
                            if chessboard[x+1][y+4]==q:
                                putchess(x,y+5,p)
                            else:
                                putchess(x+1,y+4,p)
                        else:
                            if chessboard[x+4][y+1]==q:
                                putchess(x+5,y,p)
                            else:
                                putchess(x+4,y+1,p)
                    else:
                        if random.randint(0,1)==1:
                            for z in range(2):
                                putchess(x+z+2,y-z+3,p)
                        else:
                            if random.randint(0,1)==1:
                                putchess(x,y+5,p)
                            else:
                                putchess(x+5,y,p)
    #random
    while player==p:
        x=random.randint(0,18)
        y=random.randint(0,18)
        putchess(x,y,p)
cv2.namedWindow('image')
while(1): 
    winner=getwinner()
    cv2.imshow('image',img)
    if winner==0 and player==1:
        AIplay(1)
        for a in range(19):
            print(chessboard[a])
    if winner==1:
        print("winner is",winner)
        file.write(str(winner))
        file.write(",")
        file.write("\n")
        chessboard=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        player=1
        step=0
        cv2.rectangle(img,(0,0),(760,760),(0,255,255),-1)
        for x in range(18):
            for y in range (18):
                cv2.rectangle(img,(20+40*x,20+40*y),(60+40*x,60+40*y),(0,0,0),1)
        for x in range(3):
            for y in range(3):
                cv2.circle(img,(140+240*x,140+240*y),4,(0,0,0),-1)
    else:
        if winner==0 and player==2:
            AIplay(2)
            for a in range(19):
                print(chessboard[a])
    if winner==2:
        print("winner is",winner)
        file.write(str(winner))
        file.write(",")
        file.write("\n")
        chessboard=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        player=1
        step=0
        cv2.rectangle(img,(0,0),(760,760),(0,255,255),-1)
        for x in range(18):
            for y in range (18):
                cv2.rectangle(img,(20+40*x,20+40*y),(60+40*x,60+40*y),(0,0,0),1)
        for x in range(3):
            for y in range(3):
                cv2.circle(img,(140+240*x,140+240*y),4,(0,0,0),-1)
    if cv2.waitKey(1)&0xFF==27:
        file.write("\n")
        file.close()
        break
cv2.destroyAllWindows()
