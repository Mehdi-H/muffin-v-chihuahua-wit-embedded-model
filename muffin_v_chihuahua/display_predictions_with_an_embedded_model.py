import glob
import random
from importlib import resources as importlib_resources
from os.path import dirname, join

import streamlit as st
from PIL import Image

from muffin_v_chihuahua.classifier import predict_class_for


def a_random_image_of_a_muffin_or_a_chihuahua() -> str:
    with importlib_resources.path('data', 'muffin') as path_to_muffin_images:
        with importlib_resources.path('data', 'chihuahua') as path_to_chihuahua_images:
            return random.choice(
                glob.glob(join(path_to_muffin_images, '*.jpg')) +
                glob.glob(join(path_to_chihuahua_images, '*.jpg'))
            )


def display_an_image(image: bytes, path_to_img: str) -> None:
    st.header("🐶 chihuahua 👇" if dirname(path_to_img).endswith("chihuahua") else "🍪 muffin 👇")
    st.image(image, use_column_width=True)
    st.subheader("Predictions 👇")


def display_prediction(rank_starting_from_zero: int, labels_and_probas: list) -> None:
    st.write(
        f"{rank_starting_from_zero + 1}. ",
        "🏆" if "Chihuahua" in labels_and_probas[1] else "",
        predictions[1],
        float("{:.2f}".format(labels_and_probas[2]))
    )


st.set_page_config(layout="centered")
st.title('Muffin 🍪 or chihuahua 🐶')
cols = st.beta_columns(3)

for each_col in cols:
    with each_col:
        img_path = a_random_image_of_a_muffin_or_a_chihuahua()
        an_image = Image.open(img_path)
        display_an_image(an_image, img_path)
        for i, predictions in enumerate(predict_class_for(an_image.resize((299, 299)))):
            display_prediction(i, predictions)

_, button_column, _ = st.beta_columns(3)
with button_column:
    st.button("👉 Shuffle & predict 👈")
