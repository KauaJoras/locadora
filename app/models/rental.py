from datetime import date

class Rental:
    def __init__(self, item, user, start_date, due_date):
        self.item = item
        self.user = user
        self.start_date = start_date
        self.due_date = due_date

    def __str__(self):
        return f"{self.item.title} — {self.user.name} | Devolução: {self.due_date.strftime('%d/%m/%Y')}"

    def __repr__(self):
        return self.__str__()

    def return_item(self):
        self.item.is_available = True

    def is_overdue(self):
        return date.today() > self.due_date

class Fine:
    def __init__(self, rental: Rental, amount: float):
        self.rental = rental
        self.amount = amount

    def pay(self):
        print(f'{self.rental.user.name} pagou R${self.amount:.2f}')