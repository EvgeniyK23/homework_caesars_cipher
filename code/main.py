import enchant


class CaesarsCipher:
    dictionary = enchant.Dict("en_US")
    key = 0
    SYMBOL = list()
    SYMBOL.extend(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."
    )

    @classmethod
    def changer_key(cls, new: int):
        """Изменяет атрибут класса.

        Args:
            new: Новый ключ.

        Returns: Возвращает новый ключ - атрибут класса
        """
        cls.key = new
        return cls.key

    def decrypt(self, string):
        result = ""
        for i in range(len(self.SYMBOL)):
            temp = ""
            for c in string:
                temp += self.SYMBOL[(self.SYMBOL.index(c) - i)]
            if any([self.dictionary.check(word) for word in temp.split()]):
                self.key = i
                result = temp
                break
        if result == '':
            raise Exception("Such words haven't in english")
        else:
            return f"{self.key}: {result}"

    def encrypt(self, string):
        result = ""
        for c in string:
            result += self.SYMBOL[(self.SYMBOL.index(c) + self.key)
                                  % len(self.SYMBOL)]
        return f"{self.key}: {result}"


if __name__ == "__main__":
    ck = CaesarsCipher()
    strings = "o3zR v..D0?yRA0R8FR8v47w0ER4.R1WdC!sLF5D"

    input_path = input("Введите путь к файлу\n")

    with open(input_path, "w", encoding="utf-8") as f:
        print(ck.decrypt(strings), file=f)
