
# 01
def get_lines(data):
    """
    Fayl matnini qatorlar ro'yxatiga aylantirib qaytaring.

    Argumentlar:
        data (str): fayldan o'qilgan matn

    Qaytaradi:
        list: qatorlar
    """
    pass


# 02
def count_chars(data):
    """
    Fayldagi belgilar sonini (bo'sh joy va yangi qator belgilari ham kiradi) qaytaring.

    Argumentlar:
        data (str): fayldan o'qilgan matn

    Qaytaradi:
        int: belgilar soni
    """
    pass


# 03
def get_digits(data):
    """
    Fayldagi barcha raqamlarni butun sonlar ro'yxati ko'rinishida qaytaring (har bir raqam alohida).

    Argumentlar:
        data (str): fayldan o'qilgan matn

    Qaytaradi:
        list: raqamlar
    """
    pass


# 04
def get_letters(data):
    """
    Fayldagi barcha harflarni ro'yxat ko'rinishida qaytaring.

    Argumentlar:
        data (str): fayldan o'qilgan matn

    Qaytaradi:
        list: harflar
    """
    pass


# 05
def count_digits_and_others(data):
    """
    Fayldagi raqamlar sonini va raqam bo'lmagan belgilar sonini [raqamlar, boshqalar] ro'yxati ko'rinishida qaytaring.

    Argumentlar:
        data (str): fayldan o'qilgan matn

    Qaytaradi:
        list: [raqamlar, boshqalar]
    """
    pass


# 06
def get_line_lengths(data):
    """
    Har bir qatorning uzunligini ro'yxat ko'rinishida qaytaring.

    Argumentlar:
        data (str): fayldan o'qilgan matn

    Qaytaradi:
        list: uzunliklar
    """
    pass


# 07
def sum_digits(data):
    """
    Fayldagi barcha raqamlar yig'indisini qaytaring (har bir raqam alohida).

    Argumentlar:
        data (str): fayldan o'qilgan matn

    Qaytaradi:
        int: yig'indi
    """
    pass


# 08
def max_digit(data):
    """
    Fayldagi eng katta raqamni qaytaring.

    Argumentlar:
        data (str): fayldan o'qilgan matn

    Qaytaradi:
        int: eng katta raqam
    """
    pass


# 09
def min_digit(data):
    """
    Fayldagi eng kichik raqamni qaytaring.

    Argumentlar:
        data (str): fayldan o'qilgan matn

    Qaytaradi:
        int: eng kichik raqam
    """
    pass


# 10
def longest_line(data):
    """
    Eng uzun qatorni qaytaring.

    Argumentlar:
        data (str): fayldan o'qilgan matn

    Qaytaradi:
        str: eng uzun qator
    """
    pass


# 11
def count_lines(data):
    """
    Fayldagi qatorlar sonini qaytaring.

    Argumentlar:
        data (str): fayldan o'qilgan matn

    Qaytaradi:
        int: qatorlar soni
    """
    pass


# 12
def count_words(data):
    """
    Fayldagi so'zlar sonini qaytaring (so'zlar bo'sh joy yoki yangi qator bilan ajratilgan).

    Argumentlar:
        data (str): fayldan o'qilgan matn

    Qaytaradi:
        int: so'zlar soni
    """
    pass


# 13
def get_numbers(data):
    """
    Fayldagi sonlarni (ketma-ket raqamlar bitta son hisoblanadi) butun sonlar ro'yxati ko'rinishida qaytaring.

    Argumentlar:
        data (str): fayldan o'qilgan matn

    Qaytaradi:
        list: sonlar
    """
    pass


# 14
def sum_numbers(data):
    """
    Fayldagi sonlar (ketma-ket raqamlar bitta son) yig'indisini qaytaring.

    Argumentlar:
        data (str): fayldan o'qilgan matn

    Qaytaradi:
        int: yig'indi
    """
    pass


# 15
def lines_with_word(data, soz):
    """
    So'z berilgan. Shu so'z uchraydigan qatorlarni ro'yxat ko'rinishida qaytaring (katta-kichik harf farqi yo'q).

    Argumentlar:
        data (str): fayldan o'qilgan matn
        soz (str): qidirilayotgan so'z

    Qaytaradi:
        list: qatorlar
    """
    pass


# 16
def line_numbers_with_word(data, soz):
    """
    So'z berilgan. Shu so'z uchraydigan qatorlar raqamlarini (1 dan boshlab) ro'yxat ko'rinishida qaytaring (katta-kichik harf farqi yo'q).

    Argumentlar:
        data (str): fayldan o'qilgan matn
        soz (str): qidirilayotgan so'z

    Qaytaradi:
        list: qator raqamlari
    """
    pass


# 17
def most_words_line(data):
    """
    Eng ko'p so'zdan iborat qatorni qaytaring. Teng bo'lsa, birinchisini qaytaring.

    Argumentlar:
        data (str): fayldan o'qilgan matn

    Qaytaradi:
        str: qator
    """
    pass


# 18
def numbered_lines(data):
    """
    Har bir qator oldiga uning raqamini qo'yib, "<raqam>. <qator>" ko'rinishidagi satrlar ro'yxatini qaytaring.

    Argumentlar:
        data (str): fayldan o'qilgan matn

    Qaytaradi:
        list: raqamlangan qatorlar
    """
    pass


# 19
def word_frequency(data, soz):
    """
    So'z berilgan. U fayl matnida necha marta alohida so'z sifatida uchrashini qaytaring (katta-kichik harf farqi yo'q).

    Argumentlar:
        data (str): fayldan o'qilgan matn
        soz (str): so'z

    Qaytaradi:
        int: soni
    """
    pass


# 20
def capitalized_words(data):
    """
    Bosh harf bilan boshlanadigan so'zlarni ro'yxat ko'rinishida qaytaring (vergul va nuqtalarsiz).

    Argumentlar:
        data (str): fayldan o'qilgan matn

    Qaytaradi:
        list: so'zlar
    """
    pass


# Fayldan ma'lumotni o'qish
f = open("data.txt", encoding="utf-8")
data = f.read()
f.close()

print(get_lines(data))
