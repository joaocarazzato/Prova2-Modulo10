from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
from models.logging_config import LoggerSetup
import logging

# Cria um logger raiz
logger_setup = LoggerSetup()

# Adiciona o logger para o módulo
LOGGER = logging.getLogger(__name__)

blog_posts = []

class BlogPost(BaseModel):
    blog_id: int
    blog_title: str
    blog_content: str

class BlogData(BaseModel):
    blog_title: str
    blog_content: str

app = FastAPI()

@app.post("/blog")
async def create_blog(blog_post: BlogPost):
    try:
        if blog_post:
            print("BLOG POST: ", blog_post)
            blog_posts.append(blog_post)
            return {
                "status": "Blog created",
                "id": blog_post.blog_id
            }
        else:
            LOGGER.warning("Wrong Request")
            raise HTTPException(status_code=404, detail="Wrong request")
    except Exception as e:
        LOGGER.error(e)
        return HTTPException(status_code=404, detail= f"Error: {str(e)}")

@app.get("/blog")
async def get_all_blogs():
    try:
        return blog_posts
    except Exception as e:
        LOGGER.error(e)
        return HTTPException(status_code=404, detail= f"Error: {str(e)}")

@app.get("/blog/{id}")
async def get_blog_by_id(id: int):
    print("ID ", id)
    if len(blog_posts) != 0:
        for post in blog_posts:
            if post.blog_id == id:
                return post
    LOGGER.warning(f"No blog found with id {id}")
    return HTTPException(status_code=404, detail= f"No Blog post found with id {id}")
        
@app.put("/blog/{id}")
async def edit_blog_by_id(id:int, blog_data: BlogData):
        if len(blog_posts) != 0:
            for post in blog_posts:
                if post.blog_id == id:
                    post.blog_title = blog_data.blog_title
                    post.blog_content = blog_data.blog_content
                    return post
        LOGGER.warning(f"No blog found with id {id}")
        return HTTPException(status_code=404, detail=f"No Blog post found with id {id}")

@app.delete("/blog/{id}")
async def delete_blog_by_id(id: int):
    if len(blog_posts) != 0:
        for post in blog_posts:
            if post.blog_id == id:
                blog_posts.remove(post)
                return {
                    "status": "Blog removed with success"
                }
    LOGGER.warning(f"No blog found with id {id}")
    return HTTPException(status_code=404, detail=f"No Blog post found with id {id}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)