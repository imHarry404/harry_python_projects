import pyautogui as p
import cv2 as c
import numpy as np

#Create resolution
rs = p.size()

#filename in which we store recording
path = "C:\\Users\\hario\\Desktop\\pythonCourse\\openCV11Hour\\projects\\"
fn = input("Enter the file name: ")

fn = path+fn+'.avi'

#Fix the frame rate
fps = 25.0
fourcc = c.VideoWriter_fourcc(*'XVID')
output = c.VideoWriter(fn, fourcc, fps, rs)

#create recording module
c.namedWindow("LIve_Recording", c.WINDOW_NORMAL)

#Resize the window
c.resizeWindow("LIve_Recording", (640, 480))

while True:
    img = p.screenshot()  # image
    f = np.array(img)  # convert image into array
    f = c.cvtColor(f, c.COLOR_BGR2RGB)
    output.write(f)
    c.imshow("LIve_Recording", f)
    if c.waitKey(1) == ord("q"):
        break

output.release()
c.destroyAllWindows()
