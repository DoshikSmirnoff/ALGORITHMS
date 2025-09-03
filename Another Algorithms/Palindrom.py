"""
1. Массивы и строки

Легкие

1. Проверка палиндрома
   Дана строка, определить, является ли она палиндромом
   (игнорируя регистр и пробелы).

2. Слияние двух отсортированных массивов
   Даны два отсортированных массива, вернуть один объединённый
   отсортированный массив.

Средние

3. Подстрока с максимальной суммой (Kadane's Algorithm)
   Дан массив чисел, найти подмассив с максимальной суммой.

4. Поворот массива
   Дан массив, сдвинуть его вправо на k шагов (за O(n) времени и O(1) памяти).
"""

# 1 Вариант (требует больше памяти, так как используеся доп место под переменную)

def polindrom_1(str_1: str) -> bool:
    string_reversed = str_1[::-1]

    return str_1 == string_reversed

print(polindrom_1(input("Введите проверочную строку: ")))

# 2 Вариант (Оптимизированный - не понимаю, в таком случае все ли буквы проверены)

def palindrom_2(str_2: str) -> bool:

    if str_2 == str_2[::-1]:
        return True
    else:
        return False


print(palindrom_2("kok"))

# 3 Вариант (Сложные строки)

def palindrom_3(str_3: str) -> bool:

    filtered_string = "".join(filter(str.isalnum, str_3)).lower()

    return filtered_string == filtered_string[::-1]

print(palindrom_3("A man, a plan, a canal: Panama"))

# 4 Вариант (Сложный)

# Пропишем самостоятельно проверку на цифры и буквы

def isalfanumbers(s: str) -> bool:
    return (
            ord("0") <= ord(s) <= ord("9")
            or
            ord("a") <= ord(s) <= ord("z")
            or
            ord("A") <= ord(s) <= ord("Z")
    )

def palindrom_4(str_4: str) -> bool:

    left = 0
    right = len(str_4) - 1

    while left < right: # Почему тут меньше?
        while left < right and not isalfanumbers(str_4[left]):
            left += 1
        while left < right and not isalfanumbers(str_4[right]):
            right -= 1

        if str_4[left].lower() != str_4[right].lower():
            return False

        left += 1
        right -= 1
    return True

print(palindrom_4("A man, a plan, a canal: Panama"))
print(palindrom_4("aaoaa"))




