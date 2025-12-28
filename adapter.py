from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    """Новый целевой интерфейс."""
    
    @abstractmethod
    def pay(self, amount: int):
        pass


class OldPaymentSystem:
    """Старый несовместимый класс."""
    
    def make_payment(self, dollars: int):
        print(f"Оплата {dollars} долларов через старую систему")


class PaymentAdapter(PaymentProcessor):
    """Адаптер — делает старый класс совместимым с новым интерфейсом."""
    
    def __init__(self, old_system: OldPaymentSystem):
        self.old_system = old_system

    def pay(self, amount: int):
        # Преобразуем рубли в доллары (пример конвертации)
        dollars = amount // 90  # условный курс
        self.old_system.make_payment(dollars)


class NewPaymentSystem(PaymentProcessor):
    """Новый класс, уже совместимый."""
    
    def pay(self, amount: int):
        print(f"Оплата {amount} рублей через новую систему")


# Демонстрация
if __name__ == "__main__":
    # Новый класс работает напрямую
    new_processor = NewPaymentSystem()
    new_processor.pay(9000)  # Оплата 9000 рублей через новую систему

    # Старый класс через адаптер
    old_system = OldPaymentSystem()
    adapter = PaymentAdapter(old_system)
    adapter.pay(9000)  # Оплата 100 долларов через старую систему
