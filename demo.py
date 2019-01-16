import face_recognition
import os
from glob import glob


unknown_image = face_recognition.load_image_file("unknown.jpg")
encodings = face_recognition.face_encodings(unknown_image)
print(len(encodings),"faces found")

for encoding in encodings:
	found = False
	directory = 'demo'
	dirs = os.listdir(directory)
	for d in dirs:
		for file in glob(directory + '/' + d + '/*.png'):
			known_image = face_recognition.load_image_file(file)
			known_encoding = face_recognition.face_encodings(known_image)[0]
			results = face_recognition.compare_faces(encoding , [known_encoding])
			# print(results)
			if results[0] == True:
				print(d , "Found")
				found = True
			if found == True:
				break
		if found == True:
			break
# directory = 'demo'
# dirs = os.listdir(directory)
# for d in dirs:
# 	for file in glob(directory + '/' + d + '/*.txt'):
# 		print(file , d)