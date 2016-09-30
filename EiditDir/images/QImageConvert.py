from PyQt4 import QtCore,QtGui
import os

files = []

path = "./"
i = 0
for file in os.listdir(path):
	if file[-3:] == "png":
		files.append(file)

for file in files:
	image = QtGui.QImage(file)
	image.save(file)




