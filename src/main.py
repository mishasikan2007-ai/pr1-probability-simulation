import random
import math
import matplotlib.pyplot as plt
import os

os.makedirs('../graphics', exist_ok=True)

def block1_lln():
    print("=== БЛОК 1: Закон великих чисел (ЗВЧ) ===")
    p_A_theoretical = 0.5  
    N_values = [10, 100, 1000, 10000, 100000, 1000000]
    frequencies = []

    for N in N_values:
        m = sum(1 for _ in range(N) if random.random() < p_A_theoretical)
        w_A = m / N
        error = abs(w_A - p_A_theoretical)
        frequencies.append(w_A)
        print(f"N = {N:<8} | Частота W(A) = {w_A:.6f} | Похибка = {error:.6f}")
    
    return N_values, frequencies, p_A_theoretical

def block3_pi():
    print("\n=== БЛОК 3: Метод Монте-Карло для числа Пі ===")
    N_values = [10, 100, 1000, 10000, 100000, 1000000]
    pi_estimates = []

    for N in N_values:
        m = 0
        for _ in range(N):
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)
            if x**2 + y**2 <= 1:
                m += 1
        pi_approx = 4 * m / N
        pi_estimates.append(pi_approx)
        print(f"N = {N:<8} | Оцінка Пі = {pi_approx:.6f} | Похибка = {abs(pi_approx - math.pi):.6f}")
        
    return N_values, pi_estimates

def plot_results(N_values_1, freq_1, p_A, N_values_3, pi_est):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    ax1.plot(N_values_1, freq_1, marker='o', label='Статистична частота')
    ax1.axhline(y=p_A, color='r', linestyle='--', label='Теоретична ймовірність (0.5)')
    ax1.set_xscale('log')
    ax1.set_xlabel('Кількість випробувань N (log)')
    ax1.set_ylabel('Частота / Ймовірність')
    ax1.set_title('Блок 1: Закон великих чисел')
    ax1.legend()
    ax1.grid(True)

    ax2.plot(N_values_3, pi_est, marker='o', color='g', label='Оцінка Пі (Монте-Карло)')
    ax2.axhline(y=math.pi, color='r', linestyle='--', label=f'Точне Пі ({math.pi:.5f})')
    ax2.set_xscale('log')
    ax2.set_xlabel('Кількість випробувань N (log)')
    ax2.set_ylabel('Значення Пі')
    ax2.set_title('Блок 3: Обчислення числа Пі')
    ax2.legend()
    ax2.grid(True)

    plt.savefig('../graphics/simulation_results.png')
    print("\nГрафік успішно збережено у ../graphics/simulation_results.png")

if __name__ == "__main__":
    N_v1, f1, p = block1_lln()
    N_v3, pi_e = block3_pi()
    plot_results(N_v1, f1, p, N_v3, pi_e)
