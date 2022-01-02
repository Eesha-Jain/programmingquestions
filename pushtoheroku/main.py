import firebase_admin
from firebase_admin import credentials, storage
import numpy as np
import cv2

cred = credentials.Certificate("./firebasestoragepython/key.json")
app = firebase_admin.initialize_app(cred, { 'storageBucket' : 'fir-storageproject-a0a7d.appspot.com' })

bucket = storage.bucket()
blob = bucket.get_blob("TheWhiz.png") #blob
arr = np.frombuffer(blob.download_as_string(), np.uint8) #array of bytes
img = cv2.imdecode(arr, cv2.COLOR_BGR2BGR555) #actual image

cv2.imshow('image', img)
cv2.waitKey(0)