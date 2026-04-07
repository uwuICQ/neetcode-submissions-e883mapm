class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ''.join(char.lower() for char in s if char.isalnum())
        return clean == clean[::-1]
        # есть регистр, пропуски убрать, только цифры и буквы (английские)
        # 1. Структура данных? Строка
        # 2. ASCII?

    # 