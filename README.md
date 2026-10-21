# Fayllar bilan ishlash

`data.txt` faylida Allamurodning kundaligidan parcha berilgan. Barcha funksiyalar `main.py` faylida: fayl matni `data` o'zgaruvchisiga o'qiladi va funksiyalarga beriladi.

## 01. get_lines

Fayl matnini qatorlar ro'yxatiga aylantirib qaytaring.

**Misol 1:**

```Python
Kirish: data (data.txt matni)
Chiqarish: ["Allamurod Xakimov", "Toshkent shahri, 2000-yil", "Bugun 8 soat ishladim", ..., "Ertaga 3 ta kitob olaman"]
```

---

## 02. count_chars

Fayldagi belgilar sonini (bo'sh joy va yangi qator belgilari ham kiradi) qaytaring.

**Misol 1:**

```Python
Kirish: data (data.txt matni)
Chiqarish: 151
```

---

## 03. get_digits

Fayldagi barcha raqamlarni butun sonlar ro'yxati ko'rinishida qaytaring (har bir raqam alohida).

**Misol 1:**

```Python
Kirish: data (data.txt matni)
Chiqarish: [2, 0, 0, 0, 8, 2, 5, 3]
```

---

## 04. get_letters

Fayldagi barcha harflarni ro'yxat ko'rinishida qaytaring.

**Misol 1:**

```Python
Kirish: data (data.txt matni)
Chiqarish: ["A", "l", "l", ..., "n"]
```

---

## 05. count_digits_and_others

Fayldagi raqamlar sonini va raqam bo'lmagan belgilar sonini `[raqamlar, boshqalar]` ro'yxati ko'rinishida qaytaring.

**Misol 1:**

```Python
Kirish: data (data.txt matni)
Chiqarish: [8, 143]
```

---

## 06. get_line_lengths

Har bir qatorning uzunligini ro'yxat ko'rinishida qaytaring.

**Misol 1:**

```Python
Kirish: data (data.txt matni)
Chiqarish: [17, 25, 21, 35, 23, 24]
```

---

## 07. sum_digits

Fayldagi barcha raqamlar yig'indisini qaytaring (har bir raqam alohida).

**Misol 1:**

```Python
Kirish: data (data.txt matni)
Chiqarish: 20
```

---

## 08. max_digit

Fayldagi eng katta raqamni qaytaring.

**Misol 1:**

```Python
Kirish: data (data.txt matni)
Chiqarish: 8
```

---

## 09. min_digit

Fayldagi eng kichik raqamni qaytaring.

**Misol 1:**

```Python
Kirish: data (data.txt matni)
Chiqarish: 0
```

---

## 10. longest_line

Eng uzun qatorni qaytaring.

**Misol 1:**

```Python
Kirish: data (data.txt matni)
Chiqarish: "Python darsiga 2 soat vaqt ajratdim"
```

---

## 11. count_lines

Fayldagi qatorlar sonini qaytaring.

**Misol 1:**

```Python
Kirish: data (data.txt matni)
Chiqarish: 6
```

---

## 12. count_words

Fayldagi so'zlar sonini qaytaring (so'zlar bo'sh joy yoki yangi qator bilan ajratilgan).

**Misol 1:**

```Python
Kirish: data (data.txt matni)
Chiqarish: 24
```

---

## 13. get_numbers

Fayldagi sonlarni (ketma-ket raqamlar bitta son hisoblanadi) butun sonlar ro'yxati ko'rinishida qaytaring.

**Misol 1:**

```Python
Kirish: data (data.txt matni)
Chiqarish: [2000, 8, 2, 5, 3]
```

---

## 14. sum_numbers

Fayldagi sonlar (ketma-ket raqamlar bitta son) yig'indisini qaytaring.

**Misol 1:**

```Python
Kirish: data (data.txt matni)
Chiqarish: 2018
```

---

## 15. lines_with_word

So'z berilgan. Shu so'z uchraydigan qatorlarni ro'yxat ko'rinishida qaytaring (katta-kichik harf farqi yo'q).

**Misol 1:**

```Python
Kirish: data (data.txt matni), soz="soat"
Chiqarish: ["Bugun 8 soat ishladim", "Python darsiga 2 soat vaqt ajratdim"]
```

**Misol 2:**

```Python
Kirish: data (data.txt matni), soz="python"
Chiqarish: ["Python darsiga 2 soat vaqt ajratdim"]
```

---

## 16. line_numbers_with_word

So'z berilgan. Shu so'z uchraydigan qatorlar raqamlarini (1 dan boshlab) ro'yxat ko'rinishida qaytaring (katta-kichik harf farqi yo'q).

**Misol 1:**

```Python
Kirish: data (data.txt matni), soz="soat"
Chiqarish: [3, 4]
```

**Misol 2:**

```Python
Kirish: data (data.txt matni), soz="Samarqand"
Chiqarish: []
```

---

## 17. most_words_line

Eng ko'p so'zdan iborat qatorni qaytaring. Teng bo'lsa, birinchisini qaytaring.

**Misol 1:**

```Python
Kirish: data (data.txt matni)
Chiqarish: "Python darsiga 2 soat vaqt ajratdim"
```

---

## 18. numbered_lines

Har bir qator oldiga uning raqamini qo'yib, "<raqam>. <qator>" ko'rinishidagi satrlar ro'yxatini qaytaring.

**Misol 1:**

```Python
Kirish: data (data.txt matni)
Chiqarish: ["1. Allamurod Xakimov", "2. Toshkent shahri, 2000-yil", "3. Bugun 8 soat ishladim", ..., "6. Ertaga 3 ta kitob olaman"]
```

---

## 19. word_frequency

So'z berilgan. U fayl matnida necha marta alohida so'z sifatida uchrashini qaytaring (katta-kichik harf farqi yo'q).

**Misol 1:**

```Python
Kirish: data (data.txt matni), soz="soat"
Chiqarish: 2
```

**Misol 2:**

```Python
Kirish: data (data.txt matni), soz="km"
Chiqarish: 1
```

---

## 20. capitalized_words

Bosh harf bilan boshlanadigan so'zlarni ro'yxat ko'rinishida qaytaring (vergul va nuqtalarsiz).

**Misol 1:**

```Python
Kirish: data (data.txt matni)
Chiqarish: ["Allamurod", "Xakimov", "Toshkent", "Bugun", "Python", "Kechqurun", "Ertaga"]
```

