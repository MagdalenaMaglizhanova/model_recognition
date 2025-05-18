import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Ако имаш custom функции/слоеве, ги добави тук, примерно:
# def my_custom_activation(x):
#     return tf.nn.relu(x)
# custom_objects = {"my_custom_activation": my_custom_activation}

custom_objects = {}  # <- ако нямаш custom, остави празен

# Зареждаме модела (compile=False предотвратява грешки при load)
model = tf.keras.models.load_model("converted_model.h5", custom_objects=custom_objects, compile=False)

st.title("Птици - Разпознаване на изображения 🐦")

uploaded_file = st.file_uploader("Качи снимка на птица", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Качено изображение", use_column_width=True)

    # Настрой размер според модела (примерно 224x224)
    img_size = (224, 224)
    img = image.resize(img_size)
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)  # Добавя batch размер

    if st.button("Разпознай"):
        prediction = model.predict(img_array)
        # Списък с класове - смени с твоите класове
        classes = ["parrot", "white stork", "other bird"]  

        predicted_class = classes[np.argmax(prediction)]
        st.write(f"Моделът разпознава: **{predicted_class}**")
