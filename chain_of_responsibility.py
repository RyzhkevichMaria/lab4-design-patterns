from abc import ABC, abstractmethod
from typing import Optional


class Request:
    """Запрос на одобрение расхода."""
    
    def __init__(self, amount: int, description: str):
        self.amount = amount
        self.description = description


class Handler(ABC):
    """Абстрактный обработчик."""
    
    def __init__(self):
        self.next_handler: Optional[Handler] = None

    def set_next(self, handler: 'Handler') -> 'Handler':
        self.next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Request):
        pass


class Manager(Handler):
    """Менеджер — одобряет до 1000."""
    
    def handle(self, request: Request):
        if request.amount <= 1000:
            print(f"Менеджер одобрил запрос на {request.amount} ({request.description})")
        elif self.next_handler:
            self.next_handler.handle(request)


class Director(Handler):
    """Директор — одобряет до 5000."""
    
    def handle(self, request: Request):
        if request.amount <= 5000:
            print(f"Директор одобрил запрос на {request.amount} ({request.description})")
        elif self.next_handler:
            self.next_handler.handle(request)


class CEO(Handler):
    """CEO — одобряет всё остальное."""
    
    def handle(self, request: Request):
        print(f"CEO одобрил запрос на {request.amount} ({request.description})")


# Демонстрация
if __name__ == "__main__":
    manager = Manager()
    director = Director()
    ceo = CEO()

    # Строим цепочку: менеджер → директор → CEO
    manager.set_next(director).set_next(ceo)

    print("Запрос на 500:")
    manager.handle(Request(500, "Офисные принадлежности"))

    print("\nЗапрос на 3000:")
    manager.handle(Request(3000, "Новый монитор"))

    print("\nЗапрос на 10000:")
    manager.handle(Request(10000, "Командировка"))
