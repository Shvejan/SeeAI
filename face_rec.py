import cv2
from deepface import DeepFace
import os
import shutil

def register_new_face(name):

    shutil.move("./curr_img.png",f'./db/{name}.png')

    if os.path.exists("./db/representations_vgg_face.pkl"):
        os.remove("./db/representations_vgg_face.pkl")
    identify()



def identify():

    results = DeepFace.find(img_path="./curr_img.png", db_path="./db", enforce_detection=False)
    if(len(results[0])==0):
        print("unknoqn face detected")
        return "unknown"
    face_name=results[0]['identity'][0].split("/")[-1].split(".")[0]

    return(face_name)





