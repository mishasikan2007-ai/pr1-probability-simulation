import random

def block2_variant2(N=100000):
    print(f"=== БЛОК 2: Варіант 2 (3-бітове слово), N = {N} ===")
    
    count_A = 0
    count_B = 0
    count_A_and_B = 0
    count_A_or_B = 0
    count_not_A = 0

    for _ in range(N):
        word = random.randint(0, 7)
        
        bits_count = bin(word).count('1')

        is_A = (bits_count == 2)
        is_B = (word >= 4)

        if is_A: count_A += 1
        if is_B: count_B += 1
        if is_A and is_B: count_A_and_B += 1
        if is_A or is_B: count_A_or_B += 1
        if not is_A: count_not_A += 1

    p_A_stat = count_A / N
    p_B_stat = count_B / N
    p_A_and_B_stat = count_A_and_B / N
    p_A_or_B_stat = count_A_or_B / N
    p_not_A_stat = count_not_A / N

    exact_A = 3/8
    exact_B = 4/8
    exact_A_and_B = 2/8
    exact_A_or_B = 5/8
    exact_not_A = 5/8

    print(f"P(A)        | Стат = {p_A_stat:.5f} | Точна = {exact_A:.5f} | Похибка = {abs(p_A_stat - exact_A):.5f}")
    print(f"P(B)        | Стат = {p_B_stat:.5f} | Точна = {exact_B:.5f} | Похибка = {abs(p_B_stat - exact_B):.5f}")
    print(f"P(A ∩ B)    | Стат = {p_A_and_B_stat:.5f} | Точна = {exact_A_and_B:.5f} | Похибка = {abs(p_A_and_B_stat - exact_A_and_B):.5f}")
    print(f"P(A U B)    | Стат = {p_A_or_B_stat:.5f} | Точна = {exact_A_or_B:.5f} | Похибка = {abs(p_A_or_B_stat - exact_A_or_B):.5f}")
    print(f"P(not A)    | Стат = {p_not_A_stat:.5f} | Точна = {exact_not_A:.5f} | Похибка = {abs(p_not_A_stat - exact_not_A):.5f}")

    print(f"\n--- Перевірка властивості P(not A) = 1 - P(A) ---")
    print(f"1 - P(A) статистична = {1 - p_A_stat:.5f}")
    print(f"P(not A) статистична = {p_not_A_stat:.5f}")
    if abs((1 - p_A_stat) - p_not_A_stat) < 1e-9:
        print("Висновок: Властивість успішно виконується!")

if __name__ == "__main__":
    block2_variant2(100000)
