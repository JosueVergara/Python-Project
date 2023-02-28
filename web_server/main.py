import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def get_list():
    return [5,2,645,23,12]


@app.get("/contact", response_class=HTMLResponse )
def get_list():
    return """
    <h1>This is a page</h1>
     <p>I'm testing this page</p>
    """


def run():
    store.categories()

if __name__ == '__main__':
    run()