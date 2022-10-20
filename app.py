import streamlit as st
from img_classification2 import teachable_machine_classification
import keras
from PIL import Image, ImageOps
import numpy as np

st.title("Detector de Piezas LEGO")
st.sidebar.header("Proyecto de Machine Learning de la Facultad de Ciencias Quimicas de la Universidad Autonoma de Chihuahua")
st.sidebar.image("https://mario.wiki.gallery/images/thumb/4/42/NSMBU_Green_Yoshi_Egg_Artwork.png/400px-NSMBU_Green_Yoshi_Egg_Artwork.png?download")

uploaded_file = st.file_uploader("Carga una imagen ...", type=["jpg","jpeg","png"])
if uploaded_file is not None:
  image = Image.open(uploaded_file)
  label = teachable_machine_classification(image, 'keras_model.h5') 
  if label == 0:
    texto = "Brick 1x"
  if label == 1:
    texto = "Brick Bow"
  if label == 2:
    texto = "Brick 2x"
  if label == 3:
    texto = "Flat Tile"
  if label == 4:
    texto = "Tile"
  st.image(image, caption=texto)
  #st.write(label)
