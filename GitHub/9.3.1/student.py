class Student:
    def __init__(self, direction: str, required_credits: int, initial_money: int):
        self.direction = direction
        self.required_credits = required_credits
        self.money = initial_money
        self.credits = 0
        self.is_expelled = False

    def accept(self, visitor):
        visitor.visit(self)

    def has_graduated(self) -> bool:
        return not self.is_expelled and self.credits >= self.required_credits
