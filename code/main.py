import enchant


class CaesarsCipher:
    dictionary = enchant.Dict("en_US")
    key = 0
    SYMBOL = list()
    SYMBOL.extend("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
                  "1234567890 !?.")

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
            if all([self.dictionary.check(word) for word in temp.split()]):
                self.key = i
                result = temp
                break
        return f"{self.key}: {result}"

    def encrypt(self, string):
        result = ""
        for c in string:
            result += self.SYMBOL[(self.SYMBOL.index(c) + self.key)
                                  % len(self.SYMBOL)]
        return f"{self.key}: {result}"


if __name__ == "__main__":
    ck = CaesarsCipher()
    print(ck.decrypt("Wkh.ydfdwlrq.zdv.d.vxffhvv"))

    ck1 = CaesarsCipher()
    ck1.changer_key(5)  # Изменяю атрибут класса - ключ
    print(ck1.encrypt("The vacation was a success"))