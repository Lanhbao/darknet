import numpy as np
import cv2
import os
import matplotlib.pyplot as plt

crop_label_dir = "./full_data/"
output_dir = "./full_data/"

for file in os.listdir(crop_label_dir):
	if ".txt" in file:
		file_name = file.replace(".txt", "")
		new_lines = []
		with open(crop_label_dir + file_name + ".txt") as label_file:
			lines = label_file.readlines()
			for line in lines:
				line = line.split(" ")
				line[1] = "{0:.6f}".format(round(float(line[1]), 6))
				line[2] = "{0:.6f}".format(round(float(line[2]), 6))
				line[3] = "{0:.6f}".format(round(float(line[3]), 6))
				line[4] = "{0:.6f}".format(round(float(line[4]), 6))
				line = " ".join(line) + "\n"
				new_lines.append(line)
		with open(output_dir + file_name + ".txt", "w") as new_label_file:
			new_label_file.writelines(new_lines)
