import cv2
import os
import numpy as np
import tensorflow
from tensorflow.keras.models import load_model
import pandas as pd

image_height , image_width = 112, 112
seq_len = 49

def FIDDetection_3D_CNN_DiffLayer(flist):
    diff_frames_list = []

    for i in range(len(flist)-1):
        diff_fr = cv2.absdiff(flist[i], flist[i+1])
        diff_frames_list.append(diff_fr)

    return diff_frames_list


    
def frames_extraction(video_path):
    frames_list = []
    video_reader = cv2.VideoCapture(video_path)
    while True:
        success, frame = video_reader.read()
        if not success:
            #print("VideoFile Frame Extraction Done")
            break
        resized_frame = cv2.resize(frame, (image_height, image_width))
        frames_list.append(resized_frame)
    video_reader.release()
    return frames_list


def classify_videos(input_dir):
    model = load_model("./vid_frame_ins_del_forg.keras")
    files_list = os.listdir(input_dir)
    # print(files_list)
    files = []
    preds = []
    for f in files_list:
        path = os.path.join(input_dir, f)
        frames = frames_extraction(path)
        print(len(frames))
        fic=len(frames)//seq_len
        print(fic)
        pred = None
        au = True
        for i in range(fic):
            tmpl=frames[(seq_len*i):(seq_len*i+seq_len)]
            flst=FIDDetection_3D_CNN_DiffLayer(tmpl)
            pred = model.predict(np.expand_dims(flst, axis=0))
            pred = (pred>0.5)*1
            pred = pred[0]
            if(pred[2]!=1):
                files.append(path)
                preds.append(pred)
                au = False
                break
        if(au):
            files.append(path)
            preds.append(pred)
    return np.array(files), np.array(preds)

def write_to_excel(files, preds):
    data = {
        "Path" : files,
        "Insertion Forgery" : preds[:, 1],
        "Deletion Forgery" : preds[:, 2]
    }

    df = pd.DataFrame(data)

    output_file = "./mock_data.xlsx"

    df.to_excel(output_file, index = False)

x, y = classify_videos("C:/Users/Sagar/OneDrive/Desktop/vid")
print(x.shape)
print(y.shape)
write_to_excel(x,y)