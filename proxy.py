from abc import ABC, abstractmethod


class Image(ABC):
    """Интерфейс для изображения."""
    
    @abstractmethod
    def display(self):
        pass


class RealImage(Image):
    """Реальное изображение — загружает файл с диска."""
    
    def __init__(self, filename: str):
        self.filename = filename
        self.load_from_disk()

    def load_from_disk(self):
        print(f"Загрузка изображения {self.filename} с диска...")

    def display(self):
        print(f"Отображение изображения {self.filename}")


class ProxyImage(Image):
    """Прокси — контролирует доступ к реальному изображению."""
    
    def __init__(self, filename: str):
        self.filename = filename
        self.real_image = None
        self.is_authorized = False  # симуляция авторизации

    def authorize(self):
        print("Авторизация прошла успешно")
        self.is_authorized = True

    def display(self):
        if not self.is_authorized:
            print("Доступ запрещён: нужна авторизация")
            return

        if self.real_image is None:
            self.real_image = RealImage(self.filename)
        
        self.real_image.display()


# Демонстрация
if __name__ == "__main__":
    image = ProxyImage("photo.jpg")

    # Первая попытка — без авторизации
    image.display()  # Доступ запрещён

    # Авторизуемся
    image.authorize()

    # Теперь можно отобразить
    image.display()  # Загрузка + отображение

    # Повторный вызов — уже без повторной загрузки
    image.display()  # Только отображение
