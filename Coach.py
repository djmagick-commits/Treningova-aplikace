class Coach:
    def __init__(self, name,):
        self.name = name
    def exercise(self):
        print(f"cvic podle planu")
coach1 = Coach("Martin")
coach1.exercise()
print(Coach.exercise)