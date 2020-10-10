import imutils
import cv2
# redlower(HueLower,SaturationLower,ValueLower)
redlower = (157, 93,203)# low scale of red color value
redupper = (179,255,255)# high scale of red color value
camera=cv2.VideoCapture(0)
while True:
    (grabbed, frame)=camera.read()
    frame=imutils.resize(frame,width=600)
    blur=cv2.GaussianBlur(frame,(11,11),0)
    hsv = cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)#converting image color to hsv and storing the value
    mask=cv2.inRange(hsv,redlower,redupper)#comaprng hsv value of image with the other parameters
    mask=cv2.erode(mask,None,iterations=2)# this filter is used to remove noise in the image
    mask=cv2.dilate(mask,None,iterations=2)#this filter is used to remove noise in the image
    cnts=cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
    center=None
    if len(cnts) > 0:
        c=max(cnts, key=cv2.contourArea)# find maximum contour area
        ((x,y),radius)=cv2.minEnclosingCircle(c)# used to create an minimum enclosing circle around the object absed on the coordinates ,radius
        M=cv2.moments(c)
        center=(int(M["m10"]/M["m00"]),int(M["m01"]/M["m00"]))# finding the center of the minimum enclosing circle(x,y)
        if radius > 10:
            cv2.circle(frame,(int(x),int(y)),int(radius),(0,255,255),2)# this functions specifier the coloe ,thickness boundary of minimum circle
            cv2.circle(frame,center,5,(0,0,255),-1)# this function specifies the center within the minimum circle along with its coordinates
            print(center[0],radius)
            if radius >250:
                print("stop")
            else:
                if(center[0]<150):
                    print("left")
                elif(center[0]>450):
                    print("right")
                elif(radius<250):
                    print("front")
                else:
                    print("stop")
    cv2.imshow("Frame",frame)
    key=cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
cam.release()
cv2.destroyAllWindows()
