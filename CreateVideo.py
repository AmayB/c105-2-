import os
import cv2

path = "C:/Users/amabh/OneDrive/Desktop/c105(2)/Images"

images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
        file_name = path+"/"+file

        images.append(file_name)

count = len(images)

frame = cv2.imread(images[0])
height, width, channels = frame.shape
size = (width, height)

out = cv2.VideoWriter('project.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 5, size)

for i in range(count-1,0,-1):
    frame = cv2.imread(images[i])
    out.write(frame)

out.release()
print("Done")
