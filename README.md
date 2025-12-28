# lab4-design-patterns

# Лабораторная работа №4 — Структурные и поведенческие паттерны проектирования

Реализация шести паттернов на Python:

### Поведенческие паттерны
- **Strategy** — заменяемая стратегия (сортировка)
- **Chain of Responsibility** — цепочка обработчиков (одобрение расходов)
- **Iterator** — итератор по коллекции (библиотека книг)

### Структурные паттерны
- **Proxy** — контроль доступа (ленивая загрузка изображения)
- **Bridge** — разделение абстракции и реализации (рендеринг фигур)
- **Adapter** — адаптация несовместимого интерфейса (старая система оплаты)

## Файлы

- `strategy.py` — Стратегия
- `chain_of_responsibility.py` — Цепочка обязанностей
- `iterator.py` — Итератор
- `proxy.py` — Прокси
- `bridge.py` — Мост
- `adapter.py` — Адаптер

## Запуск примеров

Каждый файл можно запустить отдельно:

```bash
python strategy.py
python chain_of_responsibility.py
python iterator.py
python proxy.py
python bridge.py
python adapter.py
