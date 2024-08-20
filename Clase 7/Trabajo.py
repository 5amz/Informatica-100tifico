import face_recognition as fr
import numpy as np
from time import sleep
import os 
import cv2



def get_encoded_faces():
    """
    Busca en la carpeta de rostros y 
    codifica todos los rastros 
    
    :return: dict de (nombre, imagen codificada)
    """
    encoded = {}
    
    for dirpath, dnames, fnames in os.walk('./faces'):
        for f in fnames:
            if f.endswith('.jpg') or f.endswith('.png') or f.endswith('.jpeg'):
                face = fr.load_image_file('faces/' + f)
                encoding = fr.face_encodings(face)[0]
                encoded[f.split('.')[0]] = encoding
    return encoded