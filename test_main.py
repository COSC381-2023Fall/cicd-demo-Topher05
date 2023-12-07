from fastapi.testclient import TestClient
from main import app
from test_course import courseA
from test_student import studentA, courseB
from course import courses
from student import stds

client = TestClient(app)

def test_get_stdCourses(studentA):
    courses.append(courseA)
    courses.append(courseB)

    studentA.addCourse(courseB)
    stds [studentA._IED] = studentA
    response = client.get("/stdCourses/1")
    assert response.status_code == 200
    assert response.json() == [
            {
                '_prefix': 'COSC',
                '_course_number': '176',
                '_cap': 30,
                '_instructor': 'John Moe', 
                '_name': 'Programming II', 
                '_place': 'PH 503', 
                '_meeting_times': 'TH 12:00'
            }]
    courses.clear()

def test_get_courses(courseA):
    courses.append(courseA)
    print(courseA)
    response = client.get("/courses/COSC")
    assert response.status_code == 200
    assert response.json() == [
        {
            "_prefix":"COSC",
            "_course_number":"111",
            "_cap":30,
            "_instructor":"John Doe",
            "_name":"Programming I",
            "_place":"PH 503",
            "_meeting_times":"TH 9:00"
        }]

    courses.pop()

