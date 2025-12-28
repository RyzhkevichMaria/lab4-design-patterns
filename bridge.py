from abc import ABC, abstractmethod


class Renderer(ABC):
    """Реализация — способ отрисовки."""
    
    @abstractmethod
    def render_circle(self, radius: float):
        pass

    @abstractmethod
    def render_square(self, side: float):
        pass


class VectorRenderer(Renderer):
    """Векторный рендерер."""
    
    def render_circle(self, radius: float):
        print(f"Рисую круг радиусом {radius} векторными линиями")

    def render_square(self, side: float):
        print(f"Рисую квадрат стороной {side} векторными линиями")


class RasterRenderer(Renderer):
    """Растровый рендерер (пиксели)."""
    
    def render_circle(self, radius: float):
        print(f"Рисую круг радиусом {radius} пикселями")

    def render_square(self, side: float):
        print(f"Рисую квадрат стороной {side} пикселями")


class Shape(ABC):
    """Абстракция — фигура."""
    
    def __init__(self, renderer: Renderer):
        self.renderer = renderer

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def resize(self, factor: float):
        pass


class Circle(Shape):
    """Конкретная абстракция — круг."""
    
    def __init__(self, renderer: Renderer, radius: float):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        self.renderer.render_circle(self.radius)

    def resize(self, factor: float):
        self.radius *= factor


class Square(Shape):
    """Конкретная абстракция — квадрат."""
    
    def __init__(self, renderer: Renderer, side: float):
        super().__init__(renderer)
        self.side = side

    def draw(self):
        self.renderer.render_square(self.side)

    def resize(self, factor: float):
        self.side *= factor


# Демонстрация
if __name__ == "__main__":
    vector = VectorRenderer()
    raster = RasterRenderer()

    circle = Circle(vector, 5)
    circle.draw()  # Векторный круг
    circle.resize(2)
    circle.draw()

    square = Square(raster, 10)
    square.draw()  # Растровый квадрат
    square.resize(0.5)
    square.draw()
