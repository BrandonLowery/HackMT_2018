import numpy as np
import cv2
import Car


cap = cv2.VideoCapture('cars134.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()

kernelOp = np.ones((3,3),np.uint8)
kernelCl = np.ones((11,11),np.uint8)

areaTH = 5000
##ret, frame3 = cap.read()
##fgbg.apply(frame3, None, 1.0)

font = cv2.FONT_HERSHEY_SIMPLEX
cars = []
cid = 1
count = 0

trak = []

prevcx = 0


while(cap.isOpened()):
    
                        
    
    try:
        ret, frame = cap.read()
        frame2 = frame
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        fgmask = fgbg.apply(gray)
        
        ret, thresh = cv2.threshold(fgmask,127,255,cv2.THRESH_BINARY)
        mask = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernelOp)
        mask = cv2.morphologyEx(mask , cv2.MORPH_CLOSE, kernelCl)


    
        frame, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        text = "Car count:" + str(count)
        cv2.putText(frame2, text, (100,100),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),1,cv2.LINE_AA)

        
        for cnt in contours:
            ##cv2.drawContours(frame2, contours, -1, (0,255,0), 3)
            area = cv2.contourArea(cnt)
            if area > areaTH:
                 M = cv2.moments(cnt)
                 cx = int(M['m10']/M['m00'])
                 cy = int(M['m01']/M['m00'])
                 x,y,w,h = cv2.boundingRect(cnt)

                 

                 #print w
                 #print cx

                 new = True
                 for i in cars:
                     if abs(x-i.getX()) <= w and abs(y-i.getY()) <=h:
                         new = False
                        #print cx
                         i.setX(cx)
                         break
                     
                
                 if new == True:
                     c = Car.Car(cid,cx,cy)
                     print 'New Car'
                     cars.append(c)
                     
                     ##print cid
                     cid += 1

                 
                 cv2.circle(frame2,(cx,cy), 5, (0,0,255), -1)            
                 img = cv2.rectangle(frame2,(x,y),(x+w,y+h),(0,255,0),2)
        for i in cars:
            if i.getStatus() == False:
                status = i.checkLine()
                if status == True:
                    count+=1
                

                
            
                 
        #line1 = np.array([[827,150],[827,470]], np.int32).reshape((-1,1,2))
        #frame2 = cv2.polylines(frame2,[line1],False,(255,0,0),thickness=2)

        line1 = np.array([[270,150],[270,470]], np.int32).reshape((-1,1,2))
        frame2 = cv2.polylines(frame2,[line1],False,(255,0,0),thickness=2)




        cv2.imshow('frame',frame2)
        ##cv2.imshow('frame3',frame3)
        
        k = cv2.waitKey(20) & 0xff
        if k == 27:
            break
    
    except:
        break
    
   ##line1 = np.array([[300,180],[700,180]], np.int32).reshape((-1,1,2))

    ##frame2 = cv2.polylines(frame2,[line1],False,(255,0,0),thickness=2)



    
    ##cv2.imshow('frame2',frame2)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break


for i in cars:
    print i.getX()
print 'count'
print count
    
cap.release()
cv2.destroyAllWindows()
