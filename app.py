import streamlit as st
from PIL import Image
import time

def generate_caption(image):
    # Simulate a time-consuming operation
    time.sleep(3)
    return "Generated caption for the image."
def main():
    st.set_page_config(
        page_title="Caption Craft - Image Caption Generator",
        page_icon="🧊",
        layout="wide",
        #initial_sidebar_state="expanded",
    )

    st.markdown("""
    <style>
    
	    .stTabs [data-baseweb="tab-list"] {
		    gap: 4rem;
        }

	    .stTabs [data-baseweb="tab"] {
		    height: 50px;
            font-size: 50px;
            white-space: pre-wrap;
		    background-color: transparent;
		    border-radius: 4px 4px 0px 0px;
		    gap: 1px;
		    padding-top: 10px;
		    padding-bottom: 10px;  
        }
        .stButton{
            color: green;
            height: 400px;
            width: 200px;
            display: flex;  
            justify-content: center;  
            align-items: center;  
        }
                
    </style>""", unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["Home", "About", "Help"])
    with tab1:
        st.markdown("<h1 style='text-align: center;'>Image Caption Generator</h1>",  unsafe_allow_html=True)
        uploaded_file = st.file_uploader("Choose a PNG, JPG or JPEG image...", type=["png", "jpg", "jpeg"])
        col1, col2 = st.columns(2)
        # Display the uploaded image
        if uploaded_file is not None:
        # Open the image and resize it to the fixed size
            image = Image.open(uploaded_file)
            resized_image = image.resize((400, 400))
            with col1:
                progress_text = "Image is being uploaded. Please wait..."
                my_bar = st.progress(3, text=progress_text)

                for percent_complete in range(100):
                    time.sleep(0.01)
                    my_bar.progress(percent_complete + 1, text=progress_text)
                time.sleep(1)
                my_bar.empty()
                st.image(resized_image, caption="Uploaded Image.", use_column_width=False)
            with col2:
                if st.button("Generate Caption"):
                    with st.spinner('Work in progress. Wait for it...'):
                        time.sleep(5)
                    st.success('Done!')
                    with st.spinner("Generating caption..."):
                # Generate and display the caption
                        caption = generate_caption(resized_image)
                        st.subheader("Generated Caption:")
                        st.write(caption)

if __name__ == "__main__":
    main()