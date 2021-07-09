# import the necessary packages
import requests
import cv2
# define the URL to our face detection API
url = "http://localhost:8000/face_detection/detect/"
# use our face detection API to find faces in images via image URL
image = cv2.imread("marie.jpg")
payload = {"url": "https://www4.pictures.zimbio.com/gi/Marie+Claire+Fresh+Faces+Party+uqQZsLIbXDAx.jpg"}
r = requests.post(url, data=payload).json()
print("marie.jpg: {}".format(r))
# loop over the faces and draw them on the image
for (startX, startY, endX, endY) in r["faces"]:
	cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
# show the output image
cv2.imshow("obama.jpg", image)
cv2.waitKey(0)

# load our image and now use the face detection API to find faces in
# images by uploading an image directly
image = cv2.imread("boy.jpg")
payload = {"image": open("boy.jpg", "rb")}
r = requests.post(url, files=payload).json()
print("10faces.jpg: {}".format(r))
# loop over the faces and draw them on the image
for (startX, startY, endX, endY) in r["faces"]:
	cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
# show the output image
cv2.imshow("boy.jpg", image)
cv2.waitKey(0)

# load our image and now use the face detection API to find faces in
# images by uploading an image directly
image = cv2.imread("10faces.jpg")
payload = {"image": open("10faces.jpg", "rb")}
r = requests.post(url, files=payload).json()
print("10faces.jpg: {}".format(r))
# loop over the faces and draw them on the image
for (startX, startY, endX, endY) in r["faces"]:
	cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
# show the output image
cv2.imshow("12faces.jpg", image)
cv2.waitKey(0)

# load our image and now use the face detection API to find faces in
# images by uploading an image directly
image = cv2.imread("mfaces.jpg")
payload = {"image": open("mfaces.jpg", "rb")}
r = requests.post(url, files=payload).json()
print("mfaces.jpg: {}".format(r))
# loop over the faces and draw them on the image
for (startX, startY, endX, endY) in r["faces"]:
	cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
# show the output image
cv2.imshow("mfaces.jpg", image)
cv2.waitKey(0)
