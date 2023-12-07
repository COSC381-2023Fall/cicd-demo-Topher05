from fastapi import FastAPI
from course import courses
from student import stdCourses, stds

app = FastAPI()


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