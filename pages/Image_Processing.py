import streamlit as st
from PIL import Image

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

st.sidebar.header('Select')

img = Image.open("image1.jpg")

selected_manipulation_img = st.sidebar.selectbox('Select Image Manipulation Technique', ['Resize', 'Grayscale', 'Crop', 'Rotate'])
selected_resize_resolution_x = st.sidebar.selectbox('Select Resize Dimension (width) : ', [0, 100, 200, 300, 400, 500])
selected_resize_resolution_y = st.sidebar.selectbox('Select Resize Dimension (height) : ', [0, 100, 200, 300, 400, 500])
selected_crop_resolution_left = st.sidebar.selectbox('Select Crop Region (Left) : ', [0, 100, 200, 300, 400, 500])
selected_crop_resolution_upper = st.sidebar.selectbox('Select Crop Region (Upper) : ', [0, 100, 200, 300, 400, 500])
selected_crop_resolution_right = st.sidebar.selectbox('Select Crop Region (Right) : ', [0, 100, 200, 300, 400, 500])
selected_crop_resolution_lower = st.sidebar.selectbox('Select Crop Region (Lower) : ', [0, 100, 200, 300, 400, 500])
# selected_rotation_angle = st.sidebar.selectbox('Select Angle of Rotation : ', [0, 90, 180, 270, 360])

st.header("Original Image : ")
st.image(img)

st.header("Grayscale Image : ")
grayimg=img.convert("L")
st.image(grayimg)

st.header("Rotated Images : ")
st.text("by 90 : ")
rot90=img.transpose(Image.Transpose.ROTATE_90)
rot180=img.transpose(Image.Transpose.ROTATE_180)
rot270=img.transpose(Image.Transpose.ROTATE_270)
st.image(rot90)
st.text("by 180 : ")
st.image(rot180)
st.text("by 270 : ")
st.image(rot270)

st.header("Resize : ")
resized=img.resize((selected_resize_resolution_x,selected_resize_resolution_y), Image.BILINEAR) 
# (width, height)
st.image(resized)

st.header("Crop : ")
selection = (selected_crop_resolution_left,selected_crop_resolution_upper,selected_crop_resolution_right,selected_crop_resolution_lower) 
#(left,upper,right,lower)
cropped = img.crop(selection)
st.image(cropped)

