import os
import shutil
directory = os.getcwd()

classes = ''
train = ''
val = ''

limit = 80

# get folder directory
for subdir in os.listdir(directory):
	if subdir == 'classes' :
		classes = os.path.join(directory, subdir)
	if subdir == 'train' :
		train = os.path.join(directory, subdir)
	if subdir == 'val' :
		val = os.path.join(directory, subdir)

# iterate each subfolder in classes and copy/append each image to train folder

# iterate through subfolder
# for subdir in os.listdir(classes):
# 	# class directory
# 	folder = os.path.join(classes, subdir)
# 	# init counter
# 	i = 0
# 	print(" i init : ", i)
# 	# iterate file in class directory
# 	for subfile in os.listdir(folder):
# 		i = i + 1
# 		print(i)
# 		source = os.path.join(folder,subfile)
# 		dest = ''
# 		if i > limit :
# 			print("val : ")
# 			th_file = len(os.listdir(val)) + 1
# 			filename = str(th_file)+".jpg"
# 			for i in range(0,(4 - (len(filename) - 4))):
# 				filename = "0"+filename
			
# 			dest = os.path.join(val, filename)
# 		else:
# 			print("train : ")
# 			th_file = len(os.listdir(train)) + 1
# 			filename = str(th_file)+".jpg"
# 			for i in range(0,(4 - (len(filename) - 4))):
# 				filename = "0"+filename
			
# 			dest = os.path.join(train, filename)
# 		print(" | ", dest)
# 		# shutil.copy(source, dest)
# 		

for subdir in os.listdir(classes):
	folder = os.path.join(classes, subdir)

	i = 0
	print("reset : ", i)
	for subfile in os.listdir(folder):
		i = i + 1
		source = os.path.join(folder,subfile)
		dest = ''
		print("i ",i)
		if i > limit: 
			print("limit")
			th_file = len(os.listdir(val)) + 1
			print(th_file, "th")
			filename = str(th_file)+".jpg"
			for j in range(0,(4 - (len(filename) - 4))):
				filename = "0"+filename
			
			dest = os.path.join(val, filename)	
		else : 
			th_file = len(os.listdir(train)) + 1
			print(th_file, "th")
			filename = str(th_file)+".jpg"
			for j in range(0,(4 - (len(filename) - 4))):
				filename = "0"+filename
			
			dest = os.path.join(train, filename)	
		print(dest)
		shutil.copy(source, dest)