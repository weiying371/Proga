from visitor_base import Visitor


class Professor(Visitor):
    def __init__(self, profile: str, credits_to_give: int):
        self.profile = profile
        self.credits_to_give = credits_to_give

    def visit(self, student):
        if student.is_expelled:
            return

        if self.profile == "humanitarian" and student.direction == "natural":
            return
        if self.profile == "natural" and student.direction == "humanitarian":
            return

        student.credits += self.credits_to_give


class Accounting(Visitor):
    def __init__(self, amount: int):
        self.amount = amount

    def visit(self, student):
        if not student.is_expelled:
            student.money += self.amount


class Parents(Visitor):
    def __init__(self, amount: int):
        self.amount = amount

    def visit(self, student):
        if not student.is_expelled:
            student.money += self.amount


class Canteen(Visitor):
    def __init__(self, cost: int):
        self.cost = cost

    def visit(self, student):
        if student.is_expelled:
            return
        student.money -= self.cost
        if student.money < 0:
            student.is_expelled = True


class Dormitory(Visitor):
    def __init__(self, cost: int):
        self.cost = cost

    def visit(self, student):
        if student.is_expelled:
            return
        student.money -= self.cost
        if student.money < 0:
            student.is_expelled = True
