from Common.JsonFormatter.JsonContract import JsonContract


class StudentData(JsonContract):
    Id: int
    FirstName: str
    LastName: str
    MiddleName: str
    DateOfBirth: str
    Height: float
    Weight: float
    Citizenship: str
    KnowledgeOfLanguage: str
    FirstPhoto: bytearray
    SecondPhoto: bytearray
    GroupId: int

    @property
    def _json_fields(self) -> dict:
        return {
            "i": "Id",
            "f": "FirstName",
            "l": "LastName",
            "m": "MiddleName",
            "d": "DateOfBirth",
            "h": "Height",
            "w": "Weight",
            "c": "Citizenship",
            "k": "KnowledgeOfLanguage",
            "fp": "FirstPhoto",
            "sp": "SecondPhoto",
            "gi": "GroupId"
        }

    @staticmethod
    def get_test_student_data():
        student = StudentData()
        student.Id = 1
        student.FirstName = "Alex"
        student.LastName = "Torba"
        student.MiddleName = "Olegovich"
        student.DateOfBirth = "29.04.1998"
        student.Height = 180
        student.Weight = 68
        student.Citizenship = "Ukraine"
        student.KnowledgeOfLanguage = "Russian, Ukraine, English"
        student.GroupId = 1

        return student
