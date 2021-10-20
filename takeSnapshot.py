import cv2 

def snapshot():
    videoCaptureObject = cv2.VideoCapture(0) # starts the webcam, 0 stands for the camera of the system
    result = True
    while(result):
        ret, frame = videoCaptureObject.read() # read the frames while the camera is on
        print(ret)
        cv2.imwrite('1.png', frame) # cv2.imwrite() method is used to save an image to any storage device
        result = False
    videoCaptureObject.release() # releases the camera
    cv2.destroyAllWindows() #closes all the window that might be opened while this process

snapshot()