import matplotlib.pyplot as plt
# Данные задач: (название, старт, продолжительность)
tasks = [
    ("Анализ требований", 0, 3),
    ("Проектирование", 3, 3),
    ("Разработка интерфейса", 6, 3),
    ("Реализация логики", 9, 4),
    ("Тестирование", 13, 2)
]

# Построение графика
fig, ax = plt.subplots(figsize=(10, 6))

for i, (task, start, duration) in enumerate(tasks):
    ax.barh(i, duration, left=start, color="lightblue", edgecolor="black")

# Настройка осей и меток
ax.set_yticks(range(len(tasks)))
ax.set_yticklabels([task[0] for task in tasks])
ax.set_xlabel("Дни")
ax.set_title("Диаграмма Ганта для проекта (15 дней)")

# Ограничение по времени выполнения проекта
ax.set_xlim(0, 15)

# Добавление сетки
ax.grid(axis="x", linestyle="--", alpha=0.7)

plt.tight_layout()
plt.show()
