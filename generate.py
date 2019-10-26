import glob, os
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-p', '--path', 
                help = 'path to yolo config file', default='/data')
ap.add_argument('-t', '--train', 
                help = 'path to yolo config file', default='custom/train.txt')
ap.add_argument('-s', '--test', 
                help = 'path to yolo config file', default='custom/test.txt')
args = ap.parse_args()


dataset_path = args.path

# Percentage of images to be used for the test set
percentage_test = 10;

# Create and/or truncate train.txt and test.txt
file_train = open(args.train, 'w')  
file_test = open(args.test, 'w')

# Populate train.txt and test.txt
counter = 1  
index_test = round(100 / percentage_test)  
# for pathAndFilename in glob.iglob(os.path.join(dataset_path + "/images", "*.txt")):
for pathAndFilename in glob.iglob(os.path.join(dataset_path , "*.txt")):  
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    print(title)
    if counter == index_test+1:
        counter = 1
        file_test.write(dataset_path + "/" + title + '.jpg' + "\n")
    else:
        file_train.write(dataset_path + "/" + title + '.jpg' + "\n")
        counter = counter + 1
