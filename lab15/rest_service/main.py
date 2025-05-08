from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel
import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError

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
    try:
        summary = wikipedia.summary(title, sentences=2)
    except DisambiguationError as e:
        raise HTTPException(status_code=400, detail=f"Запрос '{title}' неоднозначен, уточните запрос. Возможные варианты: {e.options}")
    except PageError:
        raise HTTPException(status_code=404, detail=f"Страница '{title}' не найдена")
    return WikiPage(title=title, summary=summary)

@app.get("/search/query", response_model=WikiSearch)
def wiki_search(query: str):
    search_list = wikipedia.search(query)
    return WikiSearch(query=query, search_list=search_list)

@app.post("/page", response_model=WikiPage)
def post_wiki_page(head: WikiPageInput):
    try:
        summary = wikipedia.summary(head.title, sentences=2)
    except DisambiguationError as e:
        raise HTTPException(status_code=400,
                            detail=f"Запрос '{head.title}' неоднозначен, уточните запрос. Возможные варианты: {e.options}")
    except PageError:
        raise HTTPException(status_code=404, detail=f"Страница '{head.title}' не найдена")
    return WikiPage(title=head.title, summary=summary)

































