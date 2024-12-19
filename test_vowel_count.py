import pytest
from vowel_counter import count_vowels

def test_count_vowels():
    # Тестовые случаи
    assert count_vowels("hello") == 2  # 'e', 'o'
    assert count_vowels("world") == 1  # 'o'
    assert count_vowels("Python") == 1  # 'o'
    assert count_vowels("aiueo") == 5  # 'a', 'i', 'u', 'e', 'o'
    assert count_vowels("xyz") == 0  # Нет гласных
    assert count_vowels("") == 0  # Пустая строка
    assert count_vowels("AeIoU") == 5  # Все гласные в верхнем регистре

# Если хотите запустить тесты через команду
if __name__ == "__main__":
    pytest.main()