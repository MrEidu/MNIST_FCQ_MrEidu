import streamlit as st
st.title("Mi Aplicacion")
st.sidebar.header("Esta Aplicacion es una demo")
st.sidebar.image("https://mario.wiki.gallery/images/thumb/4/42/NSMBU_Green_Yoshi_Egg_Artwork.png/400px-NSMBU_Green_Yoshi_Egg_Artwork.png?download")
boton = st.button("Launch a globo")
if boton:
  st.balloons()
picture = st.sidebar.camera_input("Take a picture")
if picture:
    st.sidebar.text("The guy above is ugly!")
