import time
import requests
import threading
import uvicorn
from app import app
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import re
import nltk
import streamlit as st
import base64
from PIL import Image
nltk.download('punkt')
nltk.download('stopwords')

icon =Image.open("static/images/icon.png")
about = open("about.md")
metrics = open("metrics.md")
st.set_page_config(
        page_title="Movie Genre Classification",
        page_icon=icon,
        layout='wide'
    )


def streamlit_bg(image_path):
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
    base64_image = base64.b64encode(image_data).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{base64_image}");
            background-attachment: fixed;
            background-repeat: no-repeat;
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

streamlit_bg("static\images\cover.jpg")

def close_port(port):
    for conn in psutil.net_connections(kind='inet'):
        if conn.laddr.port == port:
            print(f"Closing port {port} by terminating PID {conn.pid}")
            process = psutil.Process(conn.pid)
            process.terminate()
def run_fastapi():
    try:
        uvicorn.run(app, host="0.0.0.0", port=8000)
    except Exception as e:
        print(f'Error running fastapi:{e}')
        close_port(8000)

fastapi_thread = threading.Thread(target=run_fastapi)
fastapi_thread.daemon = True
fastapi_thread.start()
time.sleep(2)



stemmer = PorterStemmer()
# Attempt to load stopwords with error handling
try:
    stop_words = set(stopwords.words('english'))
except Exception as e:
    print(f"An error occurred while loading NLTK stopwords: {e}")
    stop_words = set()

def preprocess_description(text):
    text = re.sub(r'/W', ' ', text)
    text = re.sub(r'http\+S', ' ', text)
    tokens = word_tokenize(text.lower())
    stemmed_words = [stemmer.stem(token) for token in tokens if token.isalpha() and token not in stop_words]
    return " ".join(stemmed_words)

# Main Streamlit app
def main():
    #st-emotion-cache-1avcm0n
    st.title('Movie Genre Classification')
    #st.image('static/images/movie_genre.jpg',width=720)
    st.subheader('Movie Genre Classification Webapp Using FastAPI')


    description = st.text_area('Enter your Movie Description here:')
    model = st.selectbox('Select Model:', ['Logistic Regression','Support Vector Classifier','Balanced Random Forest'])
    model_map={'Logistic Regression':'Logistic_Regression','Support Vector Classifier':'Support_Vector_Classifier','Balanced Random Forest':'Balanced_Random_Forest'}

    processed_description = preprocess_description(description)
    payload = {"description": processed_description}

    if st.button('Predict'):

        if description:
            response = requests.post(f'http://127.0.0.1:8000/predict?model={model_map[model]}', json=payload)
            if response.status_code == 200:
                prediction = response.json().get("prediction", "Error")
                st.success(f'This Movie is Classified as {prediction}')
            else:
                st.error("Error in prediction. Please try again.")
        else:
            st.error("Please enter a message")

    with st.expander("About"):
        st.title("Movie Genre Classification Webapp")
        st.markdown(about.read(),unsafe_allow_html=True)
    with st.expander("Metrics"):
         st.title("Movie Genre Classification")
         st.markdown(metrics.read(), unsafe_allow_html=True)
    st.warning("Please press buttons after enter the messages")

    st.markdown('---')
    st.markdown('@Sibi krishnamoorthy')
if __name__ == "__main__":
    main()
    fastapi_thread.join()




