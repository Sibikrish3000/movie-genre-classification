
<p align="center">
<a href="https://github.com/Sibikrish3000/movie-genre-classification"><img src="https://github.com/Sibikrish3000/movie-genre-classification/blob/main/static/images/movie_genre.jpg?raw=true" alt="movie genre image" width="500" height="280"></a>
</p>
<h1 align="center">Movie Genre Classification API and Web App</h1>

<p align="center">
This application uses machine learning to classify movies into genres based on their descriptions.
</p>

<p align="center">
<a href="https://github.com/Sibikrish3000/movie-genre-classification/blob/main/LICENSE"><img src="https://img.shields.io/github/license/Sibikrish3000/movie-genre-classification" alt="GitHub license"></a>
<a href="https://github.com/Sibikrish3000/movie-genre-classification/stargazers"><img src="https://img.shields.io/github/stars/Sibikrish3000/movie-genre-classification?style=social" alt="GitHub stars"></a>
<a href="https://github.com/Sibikrish3000/movie-genre-classification/issues"><img src="https://img.shields.io/github/issues/Sibikrish3000/movie-genre-classification" alt="GitHub issues"></a>
</p>
<p align="center">
<a href="https://scikit-learn.org/"><img src="https://img.shields.io/badge/sklearn-darkorange.svg?style=flat&logo=scikit-learn&logoColor=white" alt="sklearn"></a>
<a href="https://www.python.org"><img src="https://img.shields.io/badge/Python-yellow.svg?style=flat&logo=python&logoColor=white" alt="language"></a>
<a href="https://fastapi.tiangolo.com/"><img src="https://img.shields.io/badge/FastAPI-darkgreen.svg?style=flat&logo=fastapi&logoColor=white" alt="fastapi"></a>
<a href="https://hub.docker.com/"><img src="https://img.shields.io/badge/Docker-blue?style=flat&logo=docker&logoColor=white" alt="docker"></a>
<a href="https://www.streamlit.io"><img src="https://img.shields.io/badge/Streamlit-e63946?style=flat&logo=streamlit&logoColor=white" alt="streamlit"></a>
</p>

This project includes a FastAPI-based API and a Streamlit web application for classifying movie genres based on their descriptions. The machine learning models used in this project include Logistic Regression, Support Vector Classifier, and Balanced Random Forest.

## Dataset

[Movie Genre Dataset](https://www.kaggle.com/datasets/hijest/genre-classification-dataset-imdb)

## Try on Streamlit

<p>
<a href="https://movie-genre-classification.streamlit.app/"><img src="https://img.shields.io/badge/Streamlit-e63946?style=flat&logo=streamlit" alt="streamlit" width="160" height="50"></a>
</p>

## Try on Huggingface Space

<p>
<a href="https://huggingface.co/spaces/Sibikrish3000/movie-genre-classification?theme=dark"><img src="https://img.shields.io/badge/Huggingface-white?style=flat&logo=huggingface&logoSize=amd" alt="huggingface" width="160" height="50"></a>
</p>



## Project Structure
```
project_root/
│
├── app.py
├── streamlit_app.py
├── models/
│   ├── Logistic_Regression_piped.pkl
│   ├── SVM_piped.pkl
│   └── balanced_random_forest.pkl
└── static/
    ├── images/
    │   ├── api.png
    │   ├── icon.png
    │   └── cover.jpg
    ├── about.md
    └── metrics.md
```
- `app.py`: Defines the FastAPI application.
- `streamlit_app.py`: Defines the streamlit webapp.
- `Dockerfile`: Dockerfile for building the Docker image.
- `docker-compose.yml`: Docker Compose file for orchestrating the services.
- `requirements.txt`: List of dependencies.
-  `models/`: Directory containing pre-trained machine learning models.
- `static/`: Directory containing static files such as images used in the interface.
## Setup

1. **Clone the repository**

```bash
git clone https://github.com/Sibikrish3000/movie-genre-classification.git
cd movie-genre-classification
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Download NLTK data**: 
```
python -m nltk.downloader punkt
python -m nltk.downloader stopwords
```

4. **Ensure the following directory structure and files are in place**

```
project_root/
│
├── app.py
├── streamlit_app.py
├── notebook/
├── models/
│   ├── Logistic_Regression_piped.pkl
│   ├── SVM_piped.pkl
│   └── balanced_random_forest.pkl
└── static/
    ├── images/
    │   ├── api.png
    │   ├── icon.png
    │   └── cover.jpg
    ├── about.md
    └── metrics.md
```

## Running the Application Locally

1. **Start the FastAPI server**

```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

2. **Run the Streamlit application**

```bash
streamlit run streamlit_app.py
```
### Using Docker Compose

1. Build and start the containers:
   ```sh
   docker network create AIservice
   ```
    ```sh
    docker-compose up --build
    ```

2. Access the streamlit webapp at [http://localhost:8501](http://localhost:8080).

## Development

### Running in a Gitpod Cloud Environment

**Click the button below to start a new development environment:**

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/Sibikrish3000/movie-genre-classification)

### Usage

- **Enter Movie Description**: Input the movie description you want to classify.
- **Predict**: Click the "Predict" button to see the classification result.
## API Endpoints

### Home

- **URL**: `/`
- **Method**: `GET`
- **Response**: HTML home page

### Predict

- **URL**: `/predict`
- **Method**: `POST`
- **Payload**: JSON object with movie description and model selection
- **Response**: JSON object with predicted genre

## Streamlit Web Application

The Streamlit web application provides a user-friendly interface for movie genre classification. Users can input a movie description, select a model, and receive a genre prediction. The app also includes an "About" section and a "Metrics" section with relevant information.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

Sibi Krishnamoorthy
