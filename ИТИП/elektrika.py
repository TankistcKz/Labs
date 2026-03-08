import numpy as np

def calculate_circuit(R1, R2, R3, E1, E3, J):
    print("ПОРЯДОК РАСЧЕТА МЕТОДОМ ДВУХ УЗЛОВ")

    print("\n1. Рассчитать все проводимости:")
    G1 = 1/R1
    G2 = 1/R2
    G3 = 1/R3
    
    print(f"   G1 = 1/R1 = 1/{R1} = {G1:.6f} См")
    print(f"   G2 = 1/R2 = 1/{R2} = {G2:.6f} См")
    print(f"   G3 = 1/R3 = 1/{R3} = {G3:.6f} См")

    print("\n2. Рассчитать напряжения между двумя узлами:")
    print("   Используем уравнения по законам Кирхгофа")
    
    # Для узла A (первый закон Кирхгофа):
    # I1 = I2 + I3 + J
    
    # Для контуров (второй закон Кирхгофа):
    # Контур с R1, E1, R2:
    #   E1 - I1*R1 - I2*R2 = 0
    # Контур с R2, R3, E3:
    #   I2*R2 - E3 - I3*R3 = 0
    
    # Составляем систему уравнений:
    # I1 - I2 - I3 = J
    # R1*I1 + R2*I2 = E1
    # R2*I2 - R3*I3 = E3
    
    # Матричная форма: A * I = B
    A = np.array([
        [1, -1, -1],      # I1 - I2 - I3 = J
        [R1, R2, 0],      # R1*I1 + R2*I2 = E1
        [0, R2, -R3]      # R2*I2 - R3*I3 = E3
    ])
    
    B = np.array([J, E1, E3])
    
    print("\n   Матрица коэффициентов A:")
    print(A)
    print("\n   Вектор правых частей B:")
    print(B)
    
    print("\n3. Найти токи по закону Ома:")
    try:
        currents = np.linalg.solve(A, B)
        I1, I2, I3 = currents
        
        print(f"   I1 = {I1:.6f} А")
        print(f"   I2 = {I2:.6f} А")
        print(f"   I3 = {I3:.6f} А")
        
        print("\n4. Сделать проверку по первому закону Кирхгофа:")
        check_node_A = I1 - I2 - I3 - J
        print(f"   Для узла A: I1 - I2 - I3 - J = {check_node_A:.10f}")
        
        if abs(check_node_A) < 1e-6:
            print("   ✓ Проверка пройдена!")
        else:
            print("   ✗ Ошибка в расчетах!")
        
        U_AB = I2 * R2
        print(f"\n   Напряжение U_AB = I2 * R2 = {U_AB:.6f} В")
        
        return I1, I2, I3, U_AB, G1, G2, G3
        
    except np.linalg.LinAlgError:
        print("   ✗ Ошибка: система уравнений не имеет решения!")
        return None, None, None, None, None, None, None


def print_results(R, E, J, I, U, G):
    """Вывод результатов выполнения"""
    print("РЕЗУЛЬТАТ ВЫПОЛНЕНИЯ")
    
    print("\nИсходные данные:")
    print(f"Rn = {R} См")
    print(f"En = {E} В")
    print(f"Jn = {J} А")
    
    print(f"\nGn = {G} См")
    print(f"U12 = {U:.2f} В")
    print(f"\nUn = {I} В")
    print(f"\nIn = {I} А")


if __name__ == "__main__":
    print("ИСХОДНЫЕ ДАННЫЕ")
    
    R1 = 1.2
    R2 = 1.0
    R3 = 1.5
    
    E1 = 48
    E3 = 45
    
    J = 0
    
    print(f"\nСопротивления:")
    print(f"  R1 = {R1} Ом")
    print(f"  R2 = {R2} Ом")
    print(f"  R3 = {R3} Ом")
    
    print(f"\nИсточники ЭДС:")
    print(f"  E1 = {E1} В")
    print(f"  E3 = {E3} В")
    
    print(f"\nИсточник тока:")
    print(f"  J = {J} А")
    
    I1, I2, I3, U_AB, G1, G2, G3 = calculate_circuit(R1, R2, R3, E1, E3, J)
    
    if I1 is not None:
        print("РЕЗУЛЬТАТЫ РАСЧЕТА")
        
        print(f"\nТоки в ветвях:")
        print(f"  I1 = {I1:.6f} А")
        print(f"  I2 = {I2:.6f} А")
        print(f"  I3 = {I3:.6f} А")
        
        print(f"\nПроводимости:")
        print(f"  G1 = {G1:.6f} См")
        print(f"  G2 = {G2:.6f} См")
        print(f"  G3 = {G3:.6f} См")
        
        print(f"\nНапряжение между узлами:")
        print(f"  U_AB = {U_AB:.6f} В")
        
        print("ПРОВЕРКА ПО ВТОРОМУ ЗАКОНУ КИРХГОФА")

        check1 = E1 - I1*R1 - I2*R2
        print(f"\nКонтур 1 (E1-R1-R2): E1 - I1*R1 - I2*R2 = {check1:.10f}")
        
        check2 = I2*R2 - E3 - I3*R3
        print(f"Контур 2 (R2-E3-R3): I2*R2 - E3 - I3*R3 = {check2:.10f}")
        
        if abs(check1) < 1e-6 and abs(check2) < 1e-6:
            print("\n✓ Все проверки пройдены успешно!")
        else:
            print("\n✗ Обнаружены расхождения в проверках!")