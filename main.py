from fastapi import FastAPI
from typing import Optional

from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get('/blog')  # type: ignore
def blog(limit=10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'published {limit} blogs from the database'}
    else:
        return {'data': f'{limit} blogs return from database'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id: int):
    return {'data': id}

@app.get('/blog/{id}/comments')
def comments(id, limit: int =10):

    return {'limit': limit, 'data': {'1', '2', 'Okpo'}}

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def create_blog(request: Blog):
    return {'data': f'Blog is created with the title "{request.title}"'}



#if __name__ == "__main__":
#   uvicorn.run(app, host='0.0.0.0', port=8000)
