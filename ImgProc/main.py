import cv2
import numpy as np

camera = cv2.VideoCapture(1)
if not camera.isOpened():
	camera = cv2.VideoCapture(0)
	if not camera.isOpened():
		exit()

while True:
	_, img = camera.read()
	height = img.shape[0]
	width = img.shape[1]

	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	_, _, v = cv2.split(hsv)

	cv2.imshow("V", v)

	_, threshV = cv2.threshold(v, 64, 255, cv2.THRESH_BINARY_INV)
	threshV = cv2.morphologyEx(threshV, cv2.MORPH_OPEN, np.ones((10, 10), np.uint8))
	threshV = cv2.morphologyEx(threshV, cv2.MORPH_CLOSE, np.ones((10, 10), np.uint8))

	startV = 0
	endV = 0
	started = False

	# Left
	for i in range(0, height):
		if threshV[i, width / 4]:
			if not started:
				started = True
				startV = i
			endV = i
		elif started:
			endV = i
			break

	leftGotSize = endV - startV
	started = False

	startV = 0
	endV = 0
	for i in range(0, height):
		if threshV[i, 3 * width / 4]:
			if not started:
				started = True
				startV = i
			endV = i
		elif started:
			endV = i
			break

	rightGotSize = endV - startV
	started = False

	startV = 0
	endV = 0
	for i in range(0, width):
		if threshV[height / 4, i]:
			if not started:
				started = True
				startV = i
			endV = i
		elif started:
			endV = i
			break

	topGotSize = endV - startV
	topStart, topEnd = startV, endV
	started = False

	startV = 0
	endV = 0
	for i in range(0, width):
		if threshV[3 * height / 4, i]:
			if not started:
				started = True
				startV = i
			endV = i
		elif started:
			endV = i
			break

	bottomGotSize = endV - startV
	bottomStart, bottomEnd = startV, endV
	started = False

	gotLeft, gotRight, gotTop, gotBottom = False, False, False, False

	if leftGotSize > 16:
		gotLeft = True
	if rightGotSize > 16:
		gotRight = True
	if topGotSize > 16:
		gotTop = True
	if bottomGotSize > 16:
		gotBottom = True

	print("Left: (%r, %d) | Right: (%r, %d) | Bottom: (%r, %d) | Top: (%r, %d)" % (
		gotLeft, leftGotSize, gotRight, rightGotSize, gotBottom, bottomGotSize, gotTop, topGotSize
	))
	posTopMean = (bottomStart + bottomEnd) / 2.
	posBottomMean = (bottomStart + bottomEnd) / 2.
	posTopMeanRel = posTopMean - (width / 2)
	posBottomMeanRel = posBottomMean - (width / 2)

	out = Dict()
	out["left"] = gotLeft
	out["right"] = gotRight
	out["bottom"] = gotBottom
	out["top"] = gotTop
	out["widthLeft"] = leftGotSize
	out["widthRight"] = rightGotSize
	out["widthTop"] = topGotSize
	out["widthBottom"] = bottomGotSize
	out["headingTop"] = posTopMean
	out["headingBottom"] = posBottomMean
	out["headingTopRel"] = posTopMeanRel
	out["headingBottomRel"] = posBottomMeanRel

'''
	if gotRight:
		cv2.line(threshV, (3 * width / 4, 0), (3 * width / 4, height), (255), 1)
	else:
		cv2.line(threshV, (3 * width / 4, 0), (3 * width / 4, height), (127), 1)

	if gotLeft:
		cv2.line(threshV, (width / 4, 0), (width / 4, height), (255), 1)
	else:
		cv2.line(threshV, (width / 4, 0), (width / 4, height), (127), 1)
		
	if gotBottom:
		cv2.line(threshV, (0, 3 * height / 4), (width, 3 * height / 4), (255), 1)
	else:
		cv2.line(threshV, (0, 3 * height / 4), (width, 3 * height / 4), (127), 1)

	if gotTop:
		cv2.line(threshV, (0, height / 4), (width, height / 4), (255), 1)
	else:
		cv2.line(threshV, (0, height / 4), (width, height / 4), (127), 1)

	cv2.imshow("V_THRESHOLDED", threshV)

	cv2.waitKey(1)
'''
