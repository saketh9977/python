### Purpose
Provide REST API interface on top of a dataset 

### Dataset
1. Zomato Restaurants in India 🇮🇳: [link](https://www.kaggle.com/datasets/narsingraogoud/zomato-restaurants-dataset-for-metropolitan-areas)
2. 120k rows, total size: 11 MB

### Run it on local
1. Start `uvicorn` webserver 💻 -
    ```
    uvicorn main:app --reload
    ```
2. Find restaurants serving `fish` 🐠 in `Hyderabad` using [http://localhost:8000/search?dish=fish&city=hyderabad](http://localhost:8000/search?dish=fish&city=hyderabad)
3. Visit [http://localhost:8000/redoc](http://localhost:8000/redoc) for documentation 📜