from fastapi import FastAPI
from pydantic import BaseModel
import wikipedia

app = FastAPI()

wikipedia.set_lang("ru")

class ArticleRequest(BaseModel):
    title: str

class ArticleResponse(BaseModel):
    title: str
    summary: str

class SearchRequest(BaseModel):
    query: str
    results_count: int = 5

class SearchResult(BaseModel):
    title: str


@app.get("/article/{title}", response_model=ArticleResponse)
def get_article(title: str):
    try:
        page = wikipedia.page(title)
        return {
            "title": page.title,
            "summary": page.summary
        }
    except wikipedia.exceptions.PageError:
        return {"error": "Страница не найдена"}

@app.get("/search", response_model=list[SearchResult])
def search_articles(query: str, limit: int = 5):
    results = wikipedia.search(query, results=limit)
    return [{"title": title} for title in results]

@app.post("/random", response_model=ArticleResponse)
def get_random_article(request: SearchRequest):
    try:
        random_title = wikipedia.random(pages=1)
        page = wikipedia.page(random_title)
        return {
            "title": page.title,
            "summary": page.summary
        }
    except wikipedia.exceptions.PageError:
        return {"error": "Не удалось найти случайную статью"}
