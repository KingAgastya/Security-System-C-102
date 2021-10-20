import cv2, time, random, dropbox

start_time = time.time()

def takeSnapshot():
    number = random.randint(0, 100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True

    while(result):
        ret, frame = videoCaptureObject.read()
        image_name = 'img' + str(number) + '.png'
        cv2.imwrite(image_name, frame)
        start_time = time.time()
        result = False
    
    return image_name
    print('Snapshot taken')
        
    videoCaptureObject.release()
    cv2.destroyAllWindows()


def uploadFiles(image_name):
    accessToken = 'sl.A6tRlIkw4-0kjN9tlQuBy5YhWzQpFjzuMvCiEFgIyvY0PIOMG5w3jVW_hV7fA-D_MnDEf7dgjyO1sbOP3TWRdQzu1geqL-EMLITrYf1g6ftq6PhR2HqjWVBey7HJeSfrhJIhwoeM3ig'
    file = image_name
    file_from = file
    file_to = '/NewFolder1' + image_name
    dbx = dropbox.Dropbox(accessToken)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)
        print('File Uploaded')

def main():
    while(True):
        if((time.time() - start_time) >= 10):
            name = takeSnapshot()
            uploadFiles(name)


main()