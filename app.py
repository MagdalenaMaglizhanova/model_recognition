import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Зареждаме модела (адаптирай името, ако е различно)
model = tf.keras.models.load_model("converted_model.keras")

st.title("Птици - Разпознаване на изображения 🐦")

uploaded_file = st.file_uploader("Качи снимка на птица", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Качено изображение", use_column_width=True)

    # Примерна подготовка на изображението - настрой според входния размер на твоя модел
    img_size = (224, 224)  # смени ако трябва
    img = image.resize(img_size)
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)  # batch dimension

    if st.button("Разпознай"):
        prediction = model.predict(img_array)
        # Тук трябва да обработиш output-a на модела според твоите класове
        # Например, ако имаш класове в списък:
        classes = ["parrot", "white stork"]  # смени с твоите класове
        predicted_class = classes[np.argmax(prediction)]

        st.write(f"Моделът разпознава: **{predicted_class}**")
