import sys
import math

def get_coef(index, prompt):
    try:
        coef_str = sys.argv[index]
    except:
        print(prompt)
        
        while (True):
            coef_str = input()
            try:
                coef = float(coef_str)
                break
            except:
                print("Неверный ввод данных")


    coef = float(coef_str)
    return coef

def solve_biquadratic(A, B, C):
    D = B**2 - 4 * A * C
    
    roots = []
    if D<0:
        return roots

    y1 = (-B + math.sqrt(D)) / (2 * A)
    y2 = (-B - math.sqrt(D)) / (2 * A)
    for y in (y1, y2):
        if y >= 0:  # Проверяем только неотрицательные значения
            roots.append(math.sqrt(y))
            roots.append(-math.sqrt(y))
    
    return roots

def main():
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')

    roots = solve_biquadratic(a, b, c)
    if len(roots) == 0:
        print("Нет корней")
    else:
        print("Корни биквадратного уравнения:", *roots)

if __name__ == "__main__":
    main()