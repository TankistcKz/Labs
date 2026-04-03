def min_refuels(distance, max_range, stations):
    stations = [0] + stations + [distance]
    refuels = []
    current_index = 0
    
    while current_index < len(stations) - 1:
        # Ищем самую дальнюю станцию, до которой можем доехать
        next_index = current_index
        while (next_index + 1 < len(stations) and 
               stations[next_index + 1] - stations[current_index] <= max_range):
            next_index += 1
        
        # Если не можем сдвинуться с места
        if next_index == current_index:
            return None
        
        # Если доехали до финиша, не добавляем его в список заправок
        if next_index == len(stations) - 1:
            break
        
        # Добавляем заправку (не финиш)
        refuels.append(stations[next_index])
        current_index = next_index
    
    return refuels


distance = 10451
max_range = 500
stations = [120, 260, 410, 560, 730, 890, 1040, 1190, 1360, 1520, 1680, 1840, 2010, 2170, 2330, 2480, 2650, 2810, 2970, 3140, 3300, 3460, 3630, 3790, 3950, 4120, 4280, 4440, 4610, 4770, 4930, 5100, 5260, 5420, 5590, 5750, 5910, 6080, 6240, 6400, 6570, 6730, 6890, 7060, 7220, 7380, 7550, 7710, 7870, 8040, 8200, 8360, 8530, 8690, 8850, 9020, 9180, 9340, 9510, 9670, 9830, 10000, 10160, 10320]

refuel_stops = min_refuels(distance, max_range, stations)

if refuel_stops is None:
    print("Невозможно добраться")
else:
    print(f"Количество остановок: {len(refuel_stops)}")
    print(f"Заправки на расстояниях (км): {refuel_stops}")
    
    print("\nМаршрут:")
    prev = 0
    for i, stop in enumerate(refuel_stops, 1):
        print(f"  Участок {i}: {prev} → {stop} км (проехали {stop - prev} км)")
        prev = stop
    print(f"  Участок {len(refuel_stops)+1}: {prev} → {distance} км (проехали {distance - prev} км)")
