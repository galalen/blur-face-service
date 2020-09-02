import numpy as np
import cv2
import os


DIR = os.path.dirname(os.path.abspath(__file__))
classifier_config = os.path.join(DIR, 'haarcascade_frontalface_default.xml')

face_cascade = cv2.CascadeClassifier(classifier_config)

def blur_face(image, mask=None):
	"""
		Given an image with face 
		will return output image with face blured

		Args:
			image: source image to process
			mask: cover the face with mask, default None
	"""

	img_copy = np.copy(image)
	gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)

	h, w = img_copy.shape[:2]
	kernel_width = (w // 10) | 1
	kernel_height = (h // 10) | 1

	if mask:
		mask = cv2.imread('./masks/unknown.png')

	faces = face_cascade.detectMultiScale(gray, 1.3, 5)

	for (x, y, w, h) in faces:
		face = img_copy[y:y+h, x:x+w]
		
		if mask:
			mask = cv2.resize(mask, (face.shape[0], face.shape[1]))

		face = cv2.GaussianBlur(face, (kernel_width, kernel_height), 0)
		
		img_copy[y:y+h, x:x+w] = face

		if mask:
			img_copy[y:y+h, x:x+w] = mask
	
	return img_copy
