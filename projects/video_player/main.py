import cv2  #importing the library
capture =cv2.VideoCapture('test.mp4') #reading the file

if(capture.isOpened()==False): #check the file that is successfully read or not
    print("Error opening videos")

while(capture.isOpened()): #when file  read successfully

    ret,frame=capture.read() #reading by frame
    if ret==True:
        cv2.imshow("Frame",frame)
        if cv2.waitKey(100) and 0xFF==ord('q'): #waitKey will control the speed of the frame,it must be integer, 1 is fastest
            break
    else:
        break
capture.release()
cv2.destroyAllWindows()

# 1 is fastest speed , it is very fast
# check on 100
# it is very much slower
# customize the speed as per your choice
# here we are using cv2 module 
# check on speed 1
# it is very slow
# speed depends upon waitKey value
# thanks
