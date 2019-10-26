from tensorflow import keras
from tensorflow.keras import layers, models, optimizers, losses
# from tensorflow.keras.datasets import mnist
import numpy as np

labels = "0123456789"

def predict(images):
	images = np.array(images)
	print(images.shape)
	if images.ndim == 3:
		image = image[np.newaxis,...]
	model = models.Sequential()
	model.add(layers.Conv2D(24, (3,3), input_shape=(56,28,3)))
	model.add(layers.ReLU())
	model.add(layers.MaxPooling2D())
	model.add(layers.Flatten())
	model.add(layers.Dense(128))
	model.add(layers.Dense(10))
	model.add(layers.Softmax())
	# model.summary()
	# model.compile(optimizer=optimizers.SGD(learning_rate=0.01),
	# 				loss=losses.SparseCategoricalCrossentropy(),
	# 				metrics=['accuracy'])

	model.load_weights("weights.h5")
	pred = model.predict(images)
	pred = np.argmax(pred, axis=-1)
	
	return pred