import cv2
import dropbox
import time
import random

startTime = time.time()

def snapshot():
    number = random.randint(0,100)
    objectCapture = cv2.VideoCapture(0)
    result = True 

    while(result):
        ret,frame = objectCapture.read()
        img_name = 'img'+ str(number) + ".png"
        cv2.imwrite(img_name,frame)
        start_time = time.time
        result = False
    
    return img_name
    print("snapshot taken")
    objectCapture.release()
    cv2.destroyAllWindows()

def uploadImg(img_name):
    access_token = "soN3Fg8sAIgAAAAAAAAAAU_382seJyO9HzH-9qWD3WYYJ-MBWIlAwEbq1EyMrXXy"
    file = img_name
    file_from = file
    file_to = "/testFolder/"+(img_name)
    dbx = dropbox.Dropbox(access_token)
    with open(file_from,"rb") as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print("file uploaded")


def main():
    while(True):
        if((time.time()-startTime)>= 5):
            name = snapshot()
            uploadImg(name)

main()