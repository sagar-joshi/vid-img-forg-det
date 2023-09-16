from skimage.metrics import structural_similarity
import statistics as st
import cv2
import os
import numpy as np

image_height = 112
image_width = 112

def framesExtraction(video_path):
    frames_list = []
    video_reader = cv2.VideoCapture(video_path)
    while True:
        success, frame = video_reader.read()
        if not success:
            break
        resized_frame = cv2.resize(frame, (image_height, image_width))
        frames_list.append(resized_frame)
        # frames_list.append(frame)
    video_reader.release()
    return frames_list

def vidForgeryDurationDet(frlst):
  score_vid_list = []
  for i in range(len(frlst)-1):
    frameA = frlst[i]
    frameB = frlst[i+1]
    #(score, diff) = structural_similarity(frameA, frameB, full=True, multichannel=True)
    (score, diff) = structural_similarity(frameA, frameB, full=True, channel_axis = 2)
    diff = (diff * 255).astype("uint8")
    score_vid_list.append(score)
  return score_vid_list

def getSimScores(path):
    return vidForgeryDurationDet(framesExtraction(path))



def getKeyFrames(path, forgType, threshold=0.3):
    scores = getSimScores(path)
    keyFrames=[]
    evenKeyFrames = []
    for i in range(len(scores)-1):
        change = abs(scores[i+1] - scores[i])
        #print(f"{scores[i+1]} - {scores[i]} = {change}")
        if(change > threshold):
            keyFrames.append(i)
        # key frames will be like [10, 11, 44, 45, 67, 68] so we will take only one of every consecutive pairs   
    if forgType == "Deletion":
        print(keyFrames)
        return keyFrames
        
    for i in range(len(keyFrames)):
            if(i%2==0):
                evenKeyFrames.append(keyFrames[i])
    print(keyFrames)
    print(evenKeyFrames)
    return evenKeyFrames


def apply_red_tint(video_path, frame_numbers, output_path='./tinted_video.mp4'):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error opening video file.")
        return

    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Define the codec and create a VideoWriter object for the output video
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    sel = 0
    i = 0
    while (i < total_frames) and ((sel+1) < len(frame_numbers)):
        ret, frame = cap.read()
        a = frame_numbers[sel]
        b = frame_numbers[sel+1]
        if(i > b and (sel+2) < len(frame_numbers)):
            sel = sel + 2
        if(i>=a and i<=b):
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert to RGB
            frame[:, :, 1:3] = 0  # Set green and blue channels to 0 (red tint)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)  # Convert back to BGR
        i += 1
        out.write(frame)


    # Release resources
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    return output_path


def get_localized_video(video_path, forgType):
    frame_numbers = getKeyFrames(video_path, forgType)  
    return apply_red_tint(video_path, frame_numbers)
