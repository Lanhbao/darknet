import os
import cv2
import matplotlib.pyplot as plt
import numpy as np
import argparse

from detection import plate_detection
from detection_character import character_detection
# from detection_character_classification import predict

ap = argparse.ArgumentParser()
ap.add_argument('-p', '--path', 
               help = 'path to text file containing class names',default="./../video_plate/")
ap.add_argument('-f', '--file', 
               help = 'path to text file containing class names',default="20190904_151126.mp4")
args = ap.parse_args()

#input_directory = "./../data/Bike_back/images/"
input_video_directory = args.path

# window_title= "License plate Detector"   
# cv2.namedWindow(window_title, cv2.WINDOW_NORMAL)

# for file in os.listdir(input_video_directory):
files = args.file
files = files.split(",")
for file in files:
	file_name = file.replace(".mp4", "")
	file_name = file + "_plate.mp4"
	cap = cv2.VideoCapture(input_video_directory + file)
	if cap.isOpened(): 
	    # get cap property 
	    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)   # float
	    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) # float
	    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
	    video_writer = cv2.VideoWriter(args.path + file_name, fourcc, 20, (int(width), int(height)))

	def sort_character_bounding_boxes(character_bounding_boxes):
		character_bounding_boxes = np.array(character_bounding_boxes)
		print(character_bounding_boxes)
		mean_x = np.mean(character_bounding_boxes[:, 0].astype(np.float64))
		mean_y = np.mean(character_bounding_boxes[:, 1].astype(np.float64))
		top_line = []
		bottom_line = []
		for bounding_box in character_bounding_boxes:
			y = float(bounding_box[1])
			if y >= mean_y:
				bottom_line.append(bounding_box)
			else:
				top_line.append(bounding_box)
		top_line = sorted(top_line, key= lambda bounding_box: float(bounding_box[0]))
		bottom_line = sorted(bottom_line, key= lambda bounding_box: float(bounding_box[0]))
		# for bouding_box in character_bounding_boxes:
		# 	print(bouding_box[4], bouding_box[0], bouding_box[1])
		# print()
		# character_bounding_boxes = sorted(character_bounding_boxes, key= lambda bouding_box: bouding_box[1])
		# for bouding_box in character_bounding_boxes:
		# 	print(bouding_box[4], bouding_box[0], bouding_box[1])
		return top_line, bottom_line
		# return character_bounding_boxes

	# for file in os.listdir(input_directory):
	while cv2.waitKey(1) < 0:
		has_frame, image = cap.read()
		# image = cv2.imread(input_directory + file)
		if has_frame == True: 
			plate_bouding_boxes = plate_detection(image)
			image_copied = image.copy()
			print(len(plate_bouding_boxes))
			for x,y,w,h in plate_bouding_boxes:
				x = round(x)
				y = round(y)
				w = round(w)
				h = round(h)
				temp = image[y:y+h+1, x:x+w+1].copy()
				character_bounding_boxes = character_detection(temp)
				print(character_bounding_boxes)
				if character_bounding_boxes is None or len(character_bounding_boxes) == 0:
					continue
				# print("bounding box", character_bounding_boxes)
				top_line, bottom_line= sort_character_bounding_boxes(character_bounding_boxes)
				top_line_string = ""
				for character in top_line:
					top_line_string += character[4]
				bottom_line_string = ""
				for character in bottom_line:
					bottom_line_string += character[4]
				print(top_line_string)
				print(bottom_line_string)
				cv2.rectangle(image_copied, (round(x),round(y)), (round(x +w), round(y +h)), (0,255,0), 2)
				cv2.putText(image_copied, top_line_string + "-" + bottom_line_string, (x-10, y-10),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
				
				# plt.imshow(image_copied[:, :, ::-1])
				# plt.show()
			video_writer.write(image_copied)
			# cv2.imshow(window_title, image_copied)
		else: 
			break
