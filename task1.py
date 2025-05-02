from trie import Trie

class Homework(Trie):
    def count_words_with_suffix(self, pattern) -> int:
        # Перевірка типу вхідного параметра
        if not isinstance(pattern, str):
            raise TypeError("Параметр pattern повинен бути рядком")
        if not pattern:
            return 0
        # Рекурсивний обхід дерева для пошуку слів із суфіксом
        def dfs(node, path, count):
            if node.value is not None and path.endswith(pattern):
                count[0] += 1
            for char, child in node.children.items():
                dfs(child, path + char, count)
        count = [0]
        dfs(self.root, '', count)
        return count[0]

    def has_prefix(self, prefix) -> bool:
        # Перевірка типу вхідного параметра
        if not isinstance(prefix, str):
            raise TypeError("Параметр prefix повинен бути рядком")
        if not prefix:
            return False
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        # Якщо є хоча б одне слово з цим префіксом
        def has_word(n):
            if n.value is not None:
                return True
            for child in n.children.values():
                if has_word(child):
                    return True
            return False
        return has_word(node)

if __name__ == "__main__":
    print("Тестування функціоналу Homework...")
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)

    # Перевірка кількості слів, що закінчуються на заданий суфікс
    print("Перевірка count_words_with_suffix:")
    print("'e':", trie.count_words_with_suffix("e"))  # 1
    print("'ion':", trie.count_words_with_suffix("ion"))  # 1
    print("'a':", trie.count_words_with_suffix("a"))  # 1
    print("'at':", trie.count_words_with_suffix("at"))  # 1

    # Перевірка наявності префікса
    print("Перевірка has_prefix:")
    print("'app':", trie.has_prefix("app"))  # True
    print("'bat':", trie.has_prefix("bat"))  # False
    print("'ban':", trie.has_prefix("ban"))  # True
    print("'ca':", trie.has_prefix("ca"))  # True
    print("Усі перевірки завершено.") 