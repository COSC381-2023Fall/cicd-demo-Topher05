from fastapi import FastAPI
from typing import Union

from .course import courses
from .student import stdCourses, stds

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/courses/{prefix}")
def get_courses(prefix: str):
    # return all the courses under the prefix
    results = []
    #print(courses)
    for course in courses:
        if course.is_prefix(prefix):
            results.append(course)
    
    return results

@app.get("/stdCourses/{EID}")
def get_stdCourses(EID: str):
    if EID in stds:
        student = stds[EID]
    return student.stdCourses