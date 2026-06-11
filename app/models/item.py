from abc import ABC, abstractmethod
from datetime import date, timedelta

class Item(ABC):
    def __init__(self, item_id: int, title: str):
        self.item_id = item_id
        self.title = title
        self.is_available = True
        self.image = None
        self.front_image = None
        self.side_image = None
        self.back_image = None

    @abstractmethod
    def rent(self, user) -> "Rental":
        pass

    def _create_rental(self, user, days):
        from app.models.rental import Rental  # import local evita circular
        if not self.is_available:
            raise ValueError(f'"{self.title}" não está disponível.')
        self.is_available = False
        return Rental(
            item=self,
            user=user,
            start_date=date.today(),
            due_date=date.today() + timedelta(days=days),
        )

class Movie(Item):
    RENTAL_DAYS = 1
    def __init__(self, item_id, title, director):
        super().__init__(item_id, title)
        self.director = director
    def rent(self, user):
        return self._create_rental(user, self.RENTAL_DAYS)

class Game(Item):
    RENTAL_DAYS = 2
    def __init__(self, item_id, title, platform):
        super().__init__(item_id, title)
        self.platform = platform
    def rent(self, user):
        return self._create_rental(user, self.RENTAL_DAYS)