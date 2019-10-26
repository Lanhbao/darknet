import numpy as np
import cv2
import os
import matplotlib.pyplot as plt

label_dir = "./full_data/"
output_dir = "./full_data/"


for file in os.listdir(label_dir):
	if ".txt" in file:
		file_name = file.replace(".txt", "")
		new_lines = []
		with open(label_dir + file_name + ".txt") as label_file:
			lines = label_file.readlines()
			for line in lines:
				line_split = line.split(" ")
				line_split[0] = "0"
				line = " ".join(line_split)
				new_lines.append(line)
		with open(output_dir + file_name + ".txt", "w") as new_label_file:
			new_label_file.writelines(new_lines)
