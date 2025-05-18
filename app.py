import streamlit as st
import tensorflow as tf
import numpy as np

# Зареждане на модела
model = tf.keras.models.load_model("converted_model.keras")

st.title("🧠 AI Модел за Предсказване")
st.write("Въведи входните стойности за модела по-долу:")

# Примерно: ако моделът очаква 4 входни стойности (можеш да коригираш според твоя)
input_1 = st.number_input("Вход 1", value=0.0)
input_2 = st.number_input("Вход 2", value=0.0)
input_3 = st.number_input("Вход 3", value=0.0)
input_4 = st.number_input("Вход 4", value=0.0)

if st.button("Предвиди"):
    inputs = np.array([[input_1, input_2, input_3, input_4]])
    prediction = model.predict(inputs)
    st.write("🔮 Предсказание:", prediction)
