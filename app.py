import streamlit as st
import streamlit.components.v1 as components

st. set_page_config(layout="wide")

st.sidebar.image("https://cdn.iconscout.com/icon/premium/png-256-thumb/manual-management-4849234-4030927.png", width=100)
st.sidebar.subheader("InstructPix2Pix:")
st.sidebar.markdown("###### Model for editing images from normal human instructions")
st.sidebar.markdown("###### Given an input image and a written instruction that tells the model what to do, the model follows these instructions to edit the image")
st.sidebar.markdown("###### To obtain training data for this, combination of the knowledge of two large pretrained models---a language model (GPT-3) and a text-to-image model (Stable Diffusion)---to generate a large dataset of image editing examples")
st.sidebar.markdown("###### The conditional diffusion model, InstructPix2Pix, is trained on the generated data, and generalizes to real images and user-written instructions at inference time")
st.sidebar.markdown("###### Since it performs edits in the forward pass and does not require per-example fine-tuning or inversion, the model edits images quickly, in a matter of seconds")
st.sidebar.markdown("###### Shows compelling editing results for a diverse collection of input images and written instructions")

st.sidebar.markdown("###### Model Credits- Tim Brooks, Aleksander Holynski, Alexei A. Efros")

st.sidebar.subheader("Model Results: ")
st.sidebar.image("Results.png", width=150)

st.sidebar.caption("Streamlit App by </Shahnab>")

# embed streamlit docs in a streamlit app
st.components.v1.iframe("https://timbrooks-instruct-pix2pix.hf.space", width=1100, height=650, scrolling=True)
