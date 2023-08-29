
class ATM:
    def __init__(self):
        self.note_500 = 0
        self.note_200 = 0
        self.note_100 = 0
        self.note_50 = 0

    def calculate_notes(self, amount):
        self.note_500 = amount // 500
        remaining_amount = amount % 500
        self.note_200 = remaining_amount // 200
        remaining_amount = remaining_amount % 200
        # self.note_100 = remaining_amount // 100
        # remaining_amount = remaining_amount % 100
        self.note_50 = remaining_amount // 50

    def display_notes(self):
        print("500 notes:", self.note_500)
        print("200 notes:", self.note_200)
        # print("100 notes:", self.note_100)
        print("50 notes:", self.note_50)

amount = int(input("Enter the withdrawal amount: "))
atm = ATM()
atm.calculate_notes(amount)
atm.display_notes()
