from fastapi import FastAPI, Query
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import joblib
#import re
import os
#import uvicorn
import zipfile

zip_file_path = 'models.zip'

# Specify the directory where you want to extract the files
extract_to_directory = 'models'

# Create the directory if it doesn't exist
os.makedirs(extract_to_directory, exist_ok=True)

try:
    # Open the zip file
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        # Extract all the contents to the specified directory
        zip_ref.extractall(extract_to_directory)
    print(f"Files extracted to {extract_to_directory}")
except zipfile.BadZipFile:
    print("Error: The file is not a zip file or it is corrupted.")
except FileNotFoundError:
    print(f"Error: The file '{zip_file_path}' was not found.")
except PermissionError:
    print(f"Error: Permission denied while accessing '{zip_file_path}' or '{extract_to_directory}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

app = FastAPI(title="Movie genre Classification API",
    description="""An API that utilises a Machine Learning model that detects Movie genre by Description of the Movie""",
    version="1.0.0", debug=True)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get('/',response_class=HTMLResponse)
def Home():
    text='''
    <html>
    <head>
    <link rel="icon" type="image/x-icon" href="static/images/api.png">
    <title>Movie genre Classification API</title>
    </head>
    <body>
    <div>
    <h1>Movie genre Classification API</h1>
        <a href="https://github.com/Sibikrish3000/">Github repository</a>
    </div>
    </body>
    </html>
    '''
    return text

class Description(BaseModel):
    description: str


# Load pre-trained models
try:
    LOGISTIC_REGRESSION_MODEL = joblib.load('models/Logistic_Regression_piped.pkl')
    SVC_PIPED_MODEL = joblib.load('models/SVM_piped.pkl')
    BALANCED_RANDOM_FOREST_MODEL = joblib.load('models/balanced_random_forest.pkl')
except FileNotFoundError as e:
    raise RuntimeError("Model files not found. Ensure the 'models' directory contains the required files.") from e


"""
def preprocess_message(text):
    text = re.sub(r'/W', ' ', text)
    text = re.sub(r'http\+S', ' ', text)
    tokens = word_tokenize(text.lower())
    stemmed_words = [stemmer.stem(token) for token in tokens if token.isalpha() and token not in stopwords]
    return " ".join(stemmed_words)
"""
@app.post('/predict')
async def predict(Description: Description, model: str = Query(...)):

    if model == 'Logistic_Regression':
        prediction = LOGISTIC_REGRESSION_MODEL.predict([Description.description])[0]
    elif model == 'Support_Vector_Classifier':
        prediction = SVC_PIPED_MODEL.predict([Description.description])[0]
    elif model == 'Balanced_Random_Forest':
        prediction = BALANCED_RANDOM_FOREST_MODEL.predict([Description.description])[0]
    else:
        return {"error": "Invalid model selection"}

    return {"prediction": str(prediction)}


#if __name__ == '__main__':
  #  uvicorn.run(app, host='127.0.0.1', port=8000)
