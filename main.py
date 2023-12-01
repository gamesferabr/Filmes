from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import requests
import random
import uvicorn
from fastapi.staticfiles import StaticFiles


app = FastAPI()
templates = Jinja2Templates(directory="templates")
repetidos =[]
app.mount("/static",StaticFiles(directory="static"),name="static")
app.mount("/assets",StaticFiles(directory="assets"),name="assets")

@app.get("/")
def movies(request: Request):    
    return templates.TemplateResponse("index.html",{"request":request})

@app.get("/movie/")
def read_movie():
    response = requests.get("https://api.themoviedb.org/3/movie/popular?api_key=78db1cc7888c8d61d40c531a165168f4")
    all_movies = response.json()["results"]
    
    remaining_movies = [movie for movie in all_movies if movie not in repetidos]
    
    if len(remaining_movies) == 2:
         repetidos.clear()
         remaining_movies = all_movies.copy()
         print("limpou")
    
    sample_size = min(len(remaining_movies), 3)

    selected_movies = random.sample(remaining_movies, sample_size)
    
    repetidos.extend(selected_movies)

    return {"movies": selected_movies}


if __name__ == '__main__':
    uvicorn.run(app)
