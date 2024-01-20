import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Caption Craft - Image Caption Generator",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    #menu_items={
       # 'Get Help': 'https://www.extremelycoolapp.com/help',
       # 'Report a bug': "https://www.extremelycoolapp.com/bug",
       # 'About': "# This is a header. This is an *extremely* cool app!"
    #}
)

st.markdown("""
<style>

	.stTabs [data-baseweb="tab-list"] {
		gap: 4rem;
    }

	.stTabs [data-baseweb="tab"] {
		height: 50px;
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
    h1{
            text-align: center;
    }
</style>""", unsafe_allow_html=True)
st.title("Caption Craft")
tab1, tab2, tab3 = st.tabs(["Home", "About", "Help"])
with tab1:
    with st.container(height=700):
        #st.write("DEMO")
        video_url = "https://drive.google.com/file/d/1i8HJJoadjSFtlNmZxtcT1HXeTXoGLfy6/view?usp=sharing"
        st.video(video_url)
    st.markdown("<h1 style='text-align: center;'>Image Caption Generator</h1>",  unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Choose a PNG, JPG or JPEG image...", type=["png", "jpg", "jpeg"])
    col1, col2 = st.columns(2)
    # Display the uploaded image
    if uploaded_file is not None:
        # Open the image and resize it to the fixed size
        image = Image.open(uploaded_file)
        resized_image = image.resize((400, 400))
        with col1:
            st.image(resized_image, caption="Uploaded Image.", use_column_width=False)
        with col2:
            if st.button("Generate Caption"):
            # Generate and display the caption
                caption = generate_caption(resized_image)
                #st.subheader("Generated Caption:")
                #st.write(caption)
    

