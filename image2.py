import cv2
import dropbox
import time
import random
starttime = time.time()

def take_photo():
    rand = random.randint(0,100)
    videoCaptureobject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureobject.read()
        img = "img" + str(rand) + ".png"
        cv2.imwrite(img,frame)
        starttime = time.time
        result = False
    return img
    videoCaptureobject.release()
    cv2.destroyAllWindows()

def upload_file(img): 
    access_token = "sl.A-fKV5993Oer9KWuJQPBW-Ubdp0TRmU-0zjRlz4vWMvbopnPRVAnDxWps0ykoi8vytM3G3j9Yfdg9_HYl0Ge5JzHVfcz43uwEMS6R7CHvXsjCKCv-Lnqzt2ImT9UXIZ2aUtUUMVBstFw" 
    file = img
    file_from = file 
    file_to= "/testFolder/" + (img) 
    dbx = dropbox.Dropbox(access_token) 
    with open(file_from, 'rb') as f: 
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite) 
        print("file uploaded")

def time_taken():
    while(True):
        if((time.time() - starttime) >= 5):
            photo = take_photo()
            upload_file(photo)
time_taken()