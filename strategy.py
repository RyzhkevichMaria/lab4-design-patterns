from abc import ABC, abstractmethod
from typing import List


class SortStrategy(ABC):
    """Интерфейс стратегии."""
    
    @abstractmethod
    def sort(self, data: List[int]) -> List[int]:
        pass


class BubbleSortStrategy(SortStrategy):
    """Стратегия — сортировка пузырьком."""
    
    def sort(self, data: List[int]) -> List[int]:
        n = len(data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data


class QuickSortStrategy(SortStrategy):
    """Стратегия — быстрая сортировка."""
    
    def sort(self, data: List[int]) -> List[int]:
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return self.sort(left) + middle + self.sort(right)


class Sorter:
    """Контекст, использующий стратегию."""
    
    def __init__(self, strategy: SortStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: SortStrategy):
        self.strategy = strategy

    def sort_data(self, data: List[int]) -> List[int]:
        return self.strategy.sort(data.copy())  # копия, чтобы не менять оригинал


# Демонстрация
if __name__ == "__main__":
    data = [5, 2, 9, 1, 5, 6]

    sorter = Sorter(BubbleSortStrategy())
    print("Сортировка пузырьком:", sorter.sort_data(data))

    sorter.set_strategy(QuickSortStrategy())
    print("Быстрая сортировка:", sorter.sort_data(data))
