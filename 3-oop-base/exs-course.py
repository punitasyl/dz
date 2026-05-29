
class CreditMixin:
    """Mixin class to calculate credits based on price and duration."""
    price: float
    duration: int

    def calculate_credits(self) -> float:
        return self.price / self.duration

class Course:

    def __init__(self, price: float, name: str, duration: int):
        self.price = price
        self.name = name
        self.duration = duration

    def get_info(self) -> str:
        return f"Course Name: {self.name}, Price: {self.price}, Duration: {self.duration} months"
    
    def get_price(self) -> float:
        return self.price

class AI_Training(Course, CreditMixin):

    pass

# курс с проектом с параметром название проекта
class ProjectCourse(Course, CreditMixin):

    def __init__(self, price: float, name: str, duration: int, project_name: str):
        super().__init__(price, name, duration)  # Call the constructor of the parent class
        self.project_name = project_name

    def get_project_info(self) -> str:
        return f"Project Name: {self.project_name}"

course = ProjectCourse(1000.0, "AI Training", 5, "AI Project")
print(course.get_info())
print(course.get_project_info())
print(f"Credits: {course.calculate_credits()}")
