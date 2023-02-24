import store
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_list():
    return [5,2,645,23,12]


@app.get("/contact")
def get_list():
    return {"name": "Joshua",
            "lastName": "Jones",
            "age": 25}


def run():
    store.categories()

if __name__ == '__main__':
    run()