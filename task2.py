from trie import Trie

class LongestCommonWord(Trie):
    def find_longest_common_word(self, strings) -> str:
        # Перевірка типу та порожнього масиву
        if not isinstance(strings, list) or not all(isinstance(s, str) for s in strings):
            print("Вхідні дані мають бути списком рядків!")
            return ""
        if not strings:
            print("Список слів порожній!")
            return ""
        # Додаємо всі слова у Trie
        for i, word in enumerate(strings):
            self.put(word, i)
        # Знаходимо найдовший спільний префікс
        prefix = ""
        node = self.root
        while True:
            # Якщо у вузла більше одного нащадка або це кінець слова, зупиняємось
            if len(node.children) != 1 or node.value is not None:
                break
            # Беремо єдиного нащадка
            char = next(iter(node.children))
            prefix += char
            node = node.children[char]
        return prefix

if __name__ == "__main__":
    print("Тестування пошуку найдовшого спільного префікса (інтерфейс українською)...")
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    print(f"Cлова: {strings}")
    print("Найдовший спільний префікс:", trie.find_longest_common_word(strings))  # fl

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    print(f"Cлова: {strings}")
    print("Найдовший спільний префікс:", trie.find_longest_common_word(strings))  # inters

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    print(f"Cлова: {strings}")
    print("Найдовший спільний префікс:", trie.find_longest_common_word(strings))  # ''

    trie = LongestCommonWord()
    strings = []
    print(f"Cлова: {strings}")
    print("Найдовший спільний префікс:", trie.find_longest_common_word(strings))  # ''

    trie = LongestCommonWord()
    strings = ["oneword"]
    print(f"Cлова: {strings}")
    print("Найдовший спільний префікс:", trie.find_longest_common_word(strings))  # 'oneword' 