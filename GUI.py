import os
import sys	
import json
import tkinter
import imageio
import threading

# weird PIL.Image namimg collision
from PIL import ImageTk
import PIL.Image
from tkinter import *

totalFrames = 3598

#frameNum is the current frame of picture in the window
frameNum = 0

def sort(path, filenameList):
	# 排序資料夾中的圖片編號
	filenameNumberList = []
	for file in filenameList:
		if( os.path.isdir(os.path.join(path, file)) ):
			continue
		filename, extension = os.path.splitext(file)
		if( extension == '.jpg' or extension == '.txt' ):
			filenameNumberList.append(int(filename))
	filenameNumberList.sort()

	result = [str(x)+extension for x in filenameNumberList]

	return result

def getImagesPathList(path):
	# 取得所有要處理的圖片路徑
	# input: 目標資料夾, output: images list
	images = os.listdir(path)

	return sort(path, images)

def playVideo(label, video):
		for image in video.iter_data():
				frame_image = ImageTk.PhotoImage(Image.fromarray(image))
				label.config(image=frame_image)
				label.image = frame_image

def playFrame():
	global frameNum
	#print(frameNum)
	frameNum += 1
	if frameNum >= totalFrames:
		frameNum = 0
	
	img2 = ImageTk.PhotoImage(PIL.Image.open( frame_paths[frameNum]) )
	panel.configure(image=img2)
	panel.image = img2

	#the after() function will call the "playFrame" function in "frameInterval" time  
	root.after(frameInterval, playFrame)


root = tkinter.Tk()
root.geometry("1280x720")
root.title("test")

#frameInterval is the time interval to refresh the frame. unit in 1(ms)
frameInterval = 1
frame_paths = []

for x in range(totalFrames):
	x_str = str(x+1)
	
	#the zeros filling for the file name
	if len(x_str) < 4:
		zeros = "0" * (4 - len(x_str))
		x_str = zeros + x_str
	frame_path = "frame/demo_video " + x_str + ".jpg"

	frame_paths.append(frame_path)

#print(frame_paths)
img = ImageTk.PhotoImage(PIL.Image.open( frame_paths[frameNum] ) )
panel = tkinter.Label(root, image=img)
panel.pack(side="bottom", fill="both", expand="yes")

#the after() function will call the "playFrame" function in "frameInterval" time  
root.after(frameInterval, playFrame)
root.mainloop()







##if __name__ == "__GUI__":
##	# 輸入 givenID
##	try:
####		givenID = int(sys.argv[1])
##		main()
##	except IndexError:
##		print("請輸入起始ID!")
