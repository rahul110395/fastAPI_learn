from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List
from routers import users, courses, sections




app = FastAPI()

app.include_router(users.router)
app.include_router(sections.router)
app.include_router(courses.router)
