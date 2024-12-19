def count_vowels(input_string):
    # Определяем гласные буквы
    vowels = "aeiouAEIOU"
    # Инициализируем счетчик
    count = 0

    # Проходим по каждому символу в строке
    for char in input_string:
        if char in vowels:  # Проверяем, является ли символ гласной
            count += 1

    return count