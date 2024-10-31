import streamlit as st
import tensorflow as tf
import numpy as np


#Tensorflow Model Prediction
def model_prediction(test_image):
    model = tf.keras.models.load_model("C:/Users/chafl/OneDrive/Desktop/yash/Fruits and vegetable classifier/trained_model.h5")
    image = tf.keras.preprocessing.image.load_img(test_image,target_size=(64,64))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr]) #convert single image to batch
    predictions = model.predict(input_arr)
    return np.argmax(predictions) #return index of max element

#Sidebar
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select Page",["Home","About Project","Prediction"])

#Main Page
if(app_mode=="Home"):
    st.header("FRUITS & VEGETABLES RECOGNITION SYSTEM")
    image_path = "home_img.jpg"
    st.image(image_path)

#About Project
elif(app_mode=="About Project"):
    st.header("About Project")
    st.subheader("About Dataset")
    st.text("This dataset contains images of the following food items:")
    st.code("fruits- banana, apple, pear, grapes, orange,kiwi, watermelon, pomegranate, pineapple, mango.")
    st.code("vegetables- cucumber, carrot, capsicum, onion, potato, lemon, tomato, raddish, beetroot, cabbage, lettuce, spinach, soy bean, cauliflower, bell pepper, chilli pepper, turnip, corn, sweetcorn, sweet potato, paprika, jalepeño, ginger, garlic, peas, eggplant.")
    st.subheader("Content")
    st.text("This dataset contains three folders:")
    st.text("1. train (100 images each)")
    st.text("2. test (10 images each)")
    st.text("3. validation (10 images each)")

#Prediction Page
# Prediction Page
elif app_mode == "Prediction":
    st.header("Model Prediction")
    test_image = st.file_uploader("Choose an Image:")
    if test_image is not None:
        st.image(test_image, use_column_width=True)  # display uploaded image
    
        # Predict button
        if st.button("Predict"):
            st.snow()
            st.write("Our Prediction")
            result_index = model_prediction(test_image)
            
            # Reading Labels
            labels = []
            with open("labels.txt", "r") as f:
                labels = [line.strip() for line in f]
            
            # Make sure result_index is valid
            if result_index < len(labels):
                st.success(f"Model is predicting it's a {labels[result_index]}")
            else:
                st.error("Prediction result is out of label range.")
