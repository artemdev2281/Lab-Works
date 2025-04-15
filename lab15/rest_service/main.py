from fastapi import FastAPI
from pydantic import BaseModel
import wikipedia

app = FastAPI()

class WikiPage(BaseModel):
    title: str
    summary: str

class WikiSearch(BaseModel):
    query: str
    search_list: list[str]

class WikiPageInput(BaseModel):
    title: str

@app.get("/page/{title}", response_model=WikiPage)
def get_wiki_page(title: str):
    summary = wikipedia.summary(title, sentences=2)
    return WikiPage(title=title, summary=summary)

@app.get("/search/query", response_model=WikiSearch)
def wiki_search(query: str):
    search_list = wikipedia.search(query)
    return WikiSearch(query=query, search_list=search_list)

@app.post("/page", response_model=WikiPage)
def post_wiki_page(head: WikiPageInput):
    summary = wikipedia.summary(head.title, sentences=2)
    return WikiPage(title=head.title, summary=summary)

































