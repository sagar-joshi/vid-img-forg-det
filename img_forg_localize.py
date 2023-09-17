from tensorflow.keras.models import load_model
import cv2
import numpy as np;
import os

def getLocalizedImg(path):
    output_path = './tinted_img.png'
    os.remove(output_path)
    img = cv2.imread(path)
    model = load_model('./img-forg-loc_copy_move_e200.keras')
    pred = model.predict(np.expand_dims(img, axis=0))
    threshold = pred[0].min() + ((pred[0].max() - pred[0].min())/2)
    pred = (pred > threshold) * 255
    for i in range(len(pred[0])):
        for j in range(len(pred[0][0])):
            if(pred[0][i][j]==255):
                img[i][j][0] = 0    #blue
                img[i][j][1] = 0    #green
    cv2.imwrite(output_path,img)
    return output_path


