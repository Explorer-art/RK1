# -*- coding:utf-8 -*-
#!usr/bin/python

import os
import sys

print("RK1 - Расшифровка")
print("Автор: Truzme_")
print("")

text = input("Enter text:  ")
key = input("Enter key:   ")

text_string = []

for n in text:
    if n == "А":
        text_string.append(1)
    if n == "Б":
        text_string.append(2)
    if n == "В":
        text_string.append(3)
    if n == "Г":
        text_string.append(4)
    if n == "Д":
        text_string.append(5)
    if n == "Е":
        text_string.append(6)
    if n == "Ё":
        text_string.append(7)
    if n == "Ж":
        text_string.append(8)
    if n == "З":
        text_string.append(9)
    if n == "И":
        text_string.append(10)
    if n == "Й":
        text_string.append(11)
    if n == "К":
        text_string.append(12)
    if n == "Л":
        text_string.append(13)
    if n == "М":
        text_string.append(14)
    if n == "Н":
        text_string.append(15)
    if n == "О":
        text_string.append(16)
    if n == "П":
        text_string.append(17)
    if n == "Р":
        text_string.append(18)
    if n == "С":
        text_string.append(19)
    if n == "Т":
        text_string.append(20)
    if n == "У":
        text_string.append(21)
    if n == "Ф":
        text_string.append(22)
    if n == "Х":
        text_string.append(23)
    if n == "Ц":
        text_string.append(24)
    if n == "Ч":
        text_string.append(25)
    if n == "Ш":
        text_string.append(26)
    if n == "Щ":
        text_string.append(27)
    if n == "Ъ":
        text_string.append(28)
    if n == "Ы":
        text_string.append(29)
    if n == "Ь":
        text_string.append(30)
    if n == "Э":
        text_string.append(31)
    if n == "Ю":
        text_string.append(32)
    if n == "Я":
        text_string.append(33)
    if n == "а":
        text_string.append(34)
    if n == "б":
        text_string.append(35)
    if n == "в":
        text_string.append(36)
    if n == "г":
        text_string.append(37)
    if n == "д":
        text_string.append(38)
    if n == "е":
        text_string.append(39)
    if n == "ё":
        text_string.append(40)
    if n == "ж":
        text_string.append(41)
    if n == "з":
        text_string.append(42)
    if n == "и":
        text_string.append(43)
    if n == "й":
        text_string.append(44)
    if n == "к":
        text_string.append(45)
    if n == "л":
        text_string.append(46)
    if n == "м":
        text_string.append(47)
    if n == "н":
        text_string.append(48)
    if n == "о":
        text_string.append(49)
    if n == "п":
        text_string.append(50)
    if n == "р":
        text_string.append(51)
    if n == "с":
        text_string.append(52)
    if n == "т":
        text_string.append(53)
    if n == "у":
        text_string.append(54)
    if n == "ф":
        text_string.append(55)
    if n == "х":
        text_string.append(56)
    if n == "ц":
        text_string.append(57)
    if n == "ч":
        text_string.append(58)
    if n == "ш":
        text_string.append(59)
    if n == "щ":
        text_string.append(60)
    if n == "ъ":
        text_string.append(61)
    if n == "ы":
        text_string.append(62)
    if n == "ь":
        text_string.append(63)
    if n == "э":
        text_string.append(64)
    if n == "ю":
        text_string.append(65)
    if n == "я":
        text_string.append(66)
    if n == "0":
        text_string.append(67)
    if n == "1":
        text_string.append(68)
    if n == "2":
        text_string.append(69)
    if n == "3":
        text_string.append(70)
    if n == "4":
        text_string.append(71)
    if n == "5":
        text_string.append(72)
    if n == "6":
        text_string.append(73)
    if n == "7":
        text_string.append(74)
    if n == "8":
        text_string.append(75)
    if n == "9":
        text_string.append(76)
    if n == "!":
        text_string.append(77)
    if n == "?":
        text_string.append(78)
    if n == ",":
        text_string.append(79)
    if n == ".":
        text_string.append(80)
    if n == "%":
        text_string.append(81)
    if n == "$":
        text_string.append(82)
    if n == "+":
        text_string.append(83)
    if n == "-":
        text_string.append(84)
    if n == "(":
        text_string.append(85)
    if n == ")":
        text_string.append(86)
    if n == "/":
        text_string.append(87)
    if n == '"':
        text_string.append(88)
    if n == "'":
        text_string.append(89)
    if n == ":":
        text_string.append(90)
    if n == ";":
        text_string.append(91)
    if n == "=":
        text_string.append(92)
    if n == " ":
        text_string.append(93)
    if n == "A":
        text_string.append(94)
    if n == "B":
        text_string.append(95)
    if n == "C":
        text_string.append(96)
    if n == "D":
        text_string.append(97)
    if n == "E":
        text_string.append(98)
    if n == "F":
        text_string.append(99)
    if n == "G":
        text_string.append(100)
    if n == "H":
        text_string.append(101)
    if n == "I":
        text_string.append(102)
    if n == "J":
        text_string.append(103)
    if n == "K":
        text_string.append(104)
    if n == "L":
        text_string.append(105)
    if n == "M":
        text_string.append(106)
    if n == "N":
        text_string.append(107)
    if n == "O":
        text_string.append(108)
    if n == "P":
        text_string.append(109)
    if n == "Q":
        text_string.append(110)
    if n == "R":
        text_string.append(111)
    if n == "S":
        text_string.append(112)
    if n == "T":
        text_string.append(113)
    if n == "U":
        text_string.append(114)
    if n == "V":
        text_string.append(115)
    if n == "W":
        text_string.append(116)
    if n == "X":
        text_string.append(117)
    if n == "Y":
        text_string.append(118)
    if n == "Z":
        text_string.append(119)
    if n == "a":
        text_string.append(120)
    if n == "b":
        text_string.append(121)
    if n == "c":
        text_string.append(122)
    if n == "d":
        text_string.append(123)
    if n == "e":
        text_string.append(124)
    if n == "f":
        text_string.append(125)
    if n == "g":
        text_string.append(126)
    if n == "h":
        text_string.append(127)
    if n == "i":
        text_string.append(128)
    if n == "j":
        text_string.append(129)
    if n == "k":
        text_string.append(130)
    if n == "l":
        text_string.append(131)
    if n == "m":
        text_string.append(132)
    if n == "n":
        text_string.append(133)
    if n == "o":
        text_string.append(134)
    if n == "q":
        text_string.append(135)
    if n == "r":
        text_string.append(136)
    if n == "s":
        text_string.append(137)
    if n == "t":
        text_string.append(138)
    if n == "u":
        text_string.append(139)
    if n == "v":
        text_string.append(140)
    if n == "w":
        text_string.append(141)
    if n == "x":
        text_string.append(142)
    if n == "y":
        text_string.append(143)
    if n == "z":
        text_string.append(145)
    if n == "⁰":
        text_string.append(146)
    if n == "¹":
        text_string.append(147)
    if n == "²":
        text_string.append(148)
    if n == "³":
        text_string.append(149)
    if n == "⁴":
        text_string.append(150)
    if n == "⁵":
        text_string.append(151)
    if n == "⁶":
        text_string.append(152)
    if n == "⁷":
        text_string.append(153)
    if n == "⁸":
        text_string.append(154)
    if n == "⁹":
        text_string.append(155)
    if n == "¿":
        text_string.append(156)
    if n == "⸮":
        text_string.append(157)
    if n == "⅕":
        text_string.append(158)
    if n == "⅙":
        text_string.append(159)
    if n == "⅛":
        text_string.append(160)
    if n == "₀":
        text_string.append(161)
    if n == "₁":
        text_string.append(162)
    if n == "₂":
        text_string.append(163)
    if n == "₃":
        text_string.append(164)
    if n == "₄":
        text_string.append(165)
    if n == "₅":
        text_string.append(166)
    if n == "₆":
        text_string.append(167)
    if n == "₇":
        text_string.append(168)
    if n == "₈":
        text_string.append(169)
    if n == "₉":
        text_string.append(170)
    if n == "Ⓐ":
        text_string.append(171)
    if n == "Ⓑ":
        text_string.append(172)
    if n == "Ⓒ":
        text_string.append(173)
    if n == "Ⓓ":
        text_string.append(174)
    if n == "Ⓔ":
        text_string.append(175)
    if n == "Ⓕ":
        text_string.append(176)
    if n == "Ⓖ":
        text_string.append(177)
    if n == "Ⓗ":
        text_string.append(178)
    if n == "Ⓘ":
        text_string.append(179)
    if n == "Ⓙ":
        text_string.append(180)
    if n == "Ⓚ":
        text_string.append(181)
    if n == "Ⓛ":
        text_string.append(182)
    if n == "Ⓜ":
        text_string.append(183)
    if n == "Ⓝ":
        text_string.append(184)
    if n == "Ⓞ":
        text_string.append(185)
    if n == "Ⓟ":
        text_string.append(186)

r = -1

for i in key:
	r += 1
	if i == "А":
		i = 1
	if i == "Б":
		i = 2
	if i == "В":
		i = 3
	if i == "Г":
		i = 4
	if i == "Д":
		i = 5
	if i == "Е":
		i = 6
	if i == "Ё":
		i = 7
	if i == "Ж":
		i = 8
	if i == "З":
		i = 9
	if i == "И":
		i = 10
	if i == "Й":
		i = 11
	if i == "К":
		i = 12
	if i == "Л":
		i = 13
	if i == "М":
		i = 14
	if i == "Н":
		i = 15
	if i == "О":
		i = 16
	if i == "П":
		i = 17
	if i == "Р":
		i = 18
	if i == "С":
		i = 19
	if i == "Т":
		i = 20
	if i == "У":
		i = 21
	if i == "Ф":
		i = 22
	if i == "Х":
		i = 23
	if i == "Ц":
		i = 24
	if i == "Ч":
		i = 25
	if i == "Ш":
		i = 26
	if i == "Щ":
		i = 27
	if i == "Ъ":
		i = 28
	if i == "Ы":
		i = 29
	if i == "Ь":
		i = 30
	if i == "Э":
		i = 31
	if i == "Ю":
		i = 32
	if i == "Я":
		i = 33
	if i == "а":
		i = 34
	if i == "б":
		i = 35
	if i == "в":
		i = 36
	if i == "г":
		i = 37
	if i == "д":
		i = 38
	if i == "е":
		i = 39
	if i == "ё":
		i = 40
	if i == "ж":
		i = 41
	if i == "з":
		i = 42
	if i == "и":
		i = 43
	if i == "й":
		i = 44
	if i == "к":
		i = 45
	if i == "л":
		i = 46
	if i == "м":
		i = 47
	if i == "н":
		i = 48
	if i == "о":
		i = 49
	if i == "п":
		i = 50
	if i == "р":
		i = 51
	if i == "с":
		i = 52
	if i == "т":
		i = 53
	if i == "у":
		i = 54
	if i == "ф":
		i = 55
	if i == "х":
		i = 56
	if i == "ц":
		i = 57
	if i == "ч":
		i = 58
	if i == "ш":
		i = 59
	if i == "щ":
		i = 60
	if i == "ъ":
		i = 61
	if i == "ы":
		i = 62
	if i == "ь":
		i = 63
	if i == "э":
		i = 64
	if i == "ю":
		i = 65
	if i == "я":
		i = 66
	if i == "0":
		i = 67
	if i == "1":
		i = 68
	if i == "2":
		i = 69
	if i == "3":
		i = 70
	if i == "4":
		i = 71
	if i == "5":
		i = 72
	if i == "6":
		i = 73
	if i == "7":
		i = 74
	if i == "8":
		i = 75
	if i == "9":
		i = 76
	if i == "!":
		i = 77
	if i == "?":
		i = 78
	if i == ",":
		i = 79
	if i == ".":
		i = 80
	if i == "%":
		i = 81
	if i == "$":
		i = 82
	if i == "+":
		i = 83
	if i == "-":
		i = 84
	if i == "(":
		i = 85
	if i == ")":
		i = 86
	if i == "/":
		i = 87
	if i == '"':
		i = 88
	if i == "'":
		i = 89
	if i == ":":
		i = 90
	if i == ";":
		i = 91
	if i == "=":
		i = 92
	if i == " ":
		i = 93

	if i > text_string[r]:
		value = i - text_string[r]
	elif i < text_string[r]:
		value = text_string[r] - i
	elif i == text_string[r]:
		print("ОШИБКА!")

		sys.exit()
		
	if value == 1:
		print("А", end="")
	if value == 2:
		print("Б", end="")
	if value == 3:
		print("В", end="")
	if value == 4:
		print("Г", end="")
	if value == 5:
		print("Д", end="")
	if value == 6:
		print("Е", end="")
	if value == 7:
		print("Ё", end="")
	if value == 8:
		print("Ж", end="")
	if value == 9:
		print("З", end="")
	if value == 10:
		print("И", end="")
	if value == 11:
		print("Й", end="")
	if value == 12:
		print("К", end="")
	if value == 13:
		print("Л", end="")
	if value == 14:
		print("М", end="")
	if value == 15:
		print("Н", end="")
	if value == 16:
		print("О", end="")
	if value == 17:
		print("П", end="")
	if value == 18:
		print("Р", end="")
	if value == 19:
		print("С", end="")
	if value == 20:
		print("Т", end="")
	if value == 21:
		print("У", end="")
	if value == 22:
		print("Ф", end="")
	if value == 23:
		print("Х", end="")
	if value == 24:
		print("Ц", end="")
	if value == 25:
		print("Ч", end="")
	if value == 26:
		print("Ш", end="")
	if value == 27:
		print("Щ", end="")
	if value == 28:
		print("Ъ", end="")
	if value == 29:
		print("Ы", end="")
	if value == 30:
		print("Ь", end="")
	if value == 31:
		print("Э", end="")
	if value == 32:
		print("Ю", end="")
	if value == 33:
		print("Я", end="")
	if value == 34:
		print("а", end="")
	if value == 35:
		print("б", end="")
	if value == 36:
		print("в", end="")
	if value == 37:
		print("г", end="")
	if value == 38:
		print("д", end="")
	if value == 39:
		print("е", end="")
	if value == 40:
		print("ё", end="")
	if value == 41:
		print("ж", end="")
	if value == 42:
		print("з", end="")
	if value == 43:
		print("и", end="")
	if value == 44:
		print("й", end="")
	if value == 45:
		print("к", end="")
	if value == 46:
		print("л", end="")
	if value == 47:
		print("м", end="")
	if value == 48:
		print("н", end="")
	if value == 49:
		print("о", end="")
	if value == 50:
		print("п", end="")
	if value == 51:
		print("р", end="")
	if value == 52:
		print("с", end="")
	if value == 53:
		print("т", end="")
	if value == 54:
		print("у", end="")
	if value == 55:
		print("ф", end="")
	if value == 56:
		print("х", end="")
	if value == 57:
		print("ц", end="")
	if value == 58:
		print("ч", end="")
	if value == 59:
		print("ш", end="")
	if value == 60:
		print("щ", end="")
	if value == 61:
		print("ъ", end="")
	if value == 62:
		print("ы", end="")
	if value == 63:
		print("ь", end="")
	if value == 64:
		print("э", end="")
	if value == 65:
		print("ю", end="")
	if value == 66:
		print("я", end="")
	if value == 67:
		print("0", end="")
	if value == 68:
		print("1", end="")
	if value == 69:
		print("2", end="")
	if value == 70:
		print("3", end="")
	if value == 71:
		print("4", end="")
	if value == 72:
		print("5", end="")
	if value == 73:
		print("6", end="")
	if value == 74:
		print("7", end="")
	if value == 75:
		print("8", end="")
	if value == 76:
		print("9", end="")
	if value == 77:
		print("!", end="")
	if value == 78:
		print("?", end="")
	if value == 79:
		print(",", end="")
	if value == 80:
		print(".", end="")
	if value == 81:
		print("%", end="")
	if value == 82:
		print("$", end="")
	if value == 83:
		print("+", end="")
	if value == 84:
		print("-", end="")
	if value == 85:
		print("(", end="")
	if value == 86:
		print(")", end="")
	if value == 87:
		print("/", end="")
	if value == 88:
		print('"', end="")
	if value == 89:
		print("'", end="")
	if value == 90:
		print(":", end="")
	if value == 91:
		print(";", end="")
	if value == 92:
		print("=", end="")
	if value == 93:
		print(" ", end="")