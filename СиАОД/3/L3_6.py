def min_refuels(distance, max_range, stations):
    stations = [0] + stations + [distance]
    refuels = []
    current = 0
    while current < distance:
        next_station = current
        while next_station < len(stations)-1 and stations[next_station+1] - stations[current] <= max_range:
            next_station += 1
        if next_station == current:
            return None
        refuels.append(stations[next_station])
        current = next_station
    return refuels

distance = 10451
max_range = 500
stations = [120, 260, 410, 560, 730, 890, 1040, 1190, 1360, 1520, 1680, 1840, 2010, 2170, 2330, 2480, 2650, 2810, 2970, 3140, 3300, 3460, 3630, 3790, 3950, 4120, 4280, 4440, 4610, 4770, 4930, 5100, 5260, 5420, 5590, 5750, 5910, 6080, 6240, 6400, 6570, 6730, 6890, 7060, 7220, 7380, 7550, 7710, 7870, 8040, 8200, 8360, 8530, 8690, 8850, 9020, 9180, 9340, 9510, 9670, 9830, 10000, 10160, 10320]

refuel_stops = min_refuels(distance, max_range, stations)
if refuel_stops is None:
    print("Невозможно добраться")
else:
    print(f"Остановок: {len(refuel_stops)}")
    print(f"Заправки на: {refuel_stops}")
