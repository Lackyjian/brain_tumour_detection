from tensorflow.keras.models import load_model
import tensorflow as tf 

model = load_model("TUMOR_FINAL_MODEL.h5")

converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

print("Model converted")

with open("model.tflite", "wb") as file:
    file.write(tflite_model)


    