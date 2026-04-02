import json

def parse_time(t):
    return t[0] * 60 + t[1]

def greedy_schedule(events):
    # Преобразуем в удобный формат
    parsed = []
    for event in events:
        name, day, start, end, desc = event
        start_min = parse_time(start)
        end_min = parse_time(end)
        parsed.append((day, start_min, end_min, name, desc))
    
    # Сортируем по дню и времени окончания
    parsed.sort(key=lambda x: (x[0], x[2]))
    
    selected = []
    last_end = {}
    
    for day, start, end, name, desc in parsed:
        if day not in last_end or start >= last_end[day]:
            selected.append((day, start, end, name, desc))
            last_end[day] = end
    
    return selected

# Загрузка данных
with open('works.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    # Выполняем eval только для безопасной структуры
    events = eval(content.split('=')[1].strip())

schedule = greedy_schedule(events)

print(f"Всего выбрано мероприятий: {len(schedule)}")
print("\nРасписание по дням:")
current_day = None
for day, start, end, name, desc in schedule:
    if day != current_day:
        print(f"\n{day}:")
        current_day = day
    start_h = start // 60
    start_m = start % 60
    end_h = end // 60
    end_m = end % 60
    print(f"  {start_h:02d}:{start_m:02d}-{end_h:02d}:{end_m:02d} - {name}")
