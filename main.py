from fastapi import FastAPI


app = FastAPI()
app.title = "Cinepy"
app.summary = "Resumen"
app.description = "Descripción"
app.version = "0.0.1"
app.contact = {
    "name": "Cinepy",
    "url": "https://www.cinepy.com.co",
    "email": "contact@cinepy.com.co"
}
app.license_info = {
    "name": "The MIT License",
    "url": "https://opensource.org/license/mit/"
}


@app.get("/", tags=["home"])
def index():
    return "Hola Mundo"


@app.get("/movies", tags=["movies"])
def get_movies():
    return "Movies"


@app.get("/movies/{id}", tags=["movies"])
def get_movie(id: int):
    return f"Movie {id}"


if __name__ == "__main__":
    pass
