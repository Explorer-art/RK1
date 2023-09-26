# -*- coding:utf-8 -*-
#!usr/bin/python

import os
import sys

print("RK1 - Шифрование")
print("Автор: Truzme_")
print("")

key = input("Enter key:   ")
text = input("Enter text:  ")

key_string = []

for i in key:
	if i == "А":
		key_string.append(1)
	if i == "Б":
		key_string.append(2)
	if i == "В":
		key_string.append(3)
	if i == "Г":
		key_string.append(4)
	if i == "Д":
		key_string.append(5)
	if i == "Е":
		key_string.append(6)
	if i == "Ё":
		key_string.append(7)
	if i == "Ж":
		key_string.append(8)
	if i == "З":
		key_string.append(9)
	if i == "И":
		key_string.append(10)
	if i == "Й":
		key_string.append(11)
	if i == "К":
		key_string.append(12)
	if i == "Л":
		key_string.append(13)
	if i == "М":
		key_string.append(14)
	if i == "Н":
		key_string.append(15)
	if i == "О":
		key_string.append(16)
	if i == "П":
		key_string.append(17)
	if i == "Р":
		key_string.append(18)
	if i == "С":
		key_string.append(19)
	if i == "Т":
		key_string.append(20)
	if i == "У":
		key_string.append(21)
	if i == "Ф":
		key_string.append(22)
	if i == "Х":
		key_string.append(23)
	if i == "Ц":
		key_string.append(24)
	if i == "Ч":
		key_string.append(25)
	if i == "Ш":
		key_string.append(26)
	if i == "Щ":
		key_string.append(27)
	if i == "Ъ":
		key_string.append(28)
	if i == "Ы":
		key_string.append(29)
	if i == "Ь":
		key_string.append(30)
	if i == "Э":
		key_string.append(31)
	if i == "Ю":
		key_string.append(32)
	if i == "Я":
		key_string.append(33)
	if i == "а":
		key_string.append(34)
	if i == "б":
		key_string.append(35)
	if i == "в":
		key_string.append(36)
	if i == "г":
		key_string.append(37)
	if i == "д":
		key_string.append(38)
	if i == "е":
		key_string.append(39)
	if i == "ё":
		key_string.append(40)
	if i == "ж":
		key_string.append(41)
	if i == "з":
		key_string.append(42)
	if i == "и":
		key_string.append(43)
	if i == "й":
		key_string.append(44)
	if i == "к":
		key_string.append(45)
	if i == "л":
		key_string.append(46)
	if i == "м":
		key_string.append(47)
	if i == "н":
		key_string.append(48)
	if i == "о":
		key_string.append(49)
	if i == "п":
		key_string.append(50)
	if i == "р":
		key_string.append(51)
	if i == "с":
		key_string.append(52)
	if i == "т":
		key_string.append(53)
	if i == "у":
		key_string.append(54)
	if i == "ф":
		key_string.append(55)
	if i == "х":
		key_string.append(56)
	if i == "ц":
		key_string.append(57)
	if i == "ч":
		key_string.append(58)
	if i == "ш":
		key_string.append(59)
	if i == "щ":
		key_string.append(60)
	if i == "ъ":
		key_string.append(61)
	if i == "ы":
		key_string.append(62)
	if i == "ь":
		key_string.append(63)
	if i == "э":
		key_string.append(64)
	if i == "ю":
		key_string.append(65)
	if i == "я":
		key_string.append(66)
	if i == "0":
		key_string.append(67)
	if i == "1":
		key_string.append(68)
	if i == "2":
		key_string.append(69)
	if i == "3":
		key_string.append(70)
	if i == "4":
		key_string.append(71)
	if i == "5":
		key_string.append(72)
	if i == "6":
		key_string.append(73)
	if i == "7":
		key_string.append(74)
	if i == "8":
		key_string.append(75)
	if i == "9":
		key_string.append(76)
	if i == "!":
		key_string.append(77)
	if i == "?":
		key_string.append(78)
	if i == ",":
		key_string.append(79)
	if i == ".":
		key_string.append(80)
	if i == "%":
		key_string.append(81)
	if i == "$":
		key_string.append(82)
	if i == "+":
		key_string.append(83)
	if i == "-":
		key_string.append(84)
	if i == "(":
		key_string.append(85)
	if i == ")":
		key_string.append(86)
	if i == "/":
		key_string.append(87)
	if i == '"':
		key_string.append(88)
	if i == "'":
		key_string.append(89)
	if i == ":":
		key_string.append(90)
	if i == ";":
		key_string.append(91)
	if i == "=":
		key_string.append(92)
	if i == " ":
		key_string.append(93)

r = -1

for n in text:
	r += 1
	if n == "А":
		n = 1
	if n == "Б":
		n = 2
	if n == "В":
		n = 3
	if n == "Г":
		n = 4
	if n == "Д":
		n = 5
	if n == "Е":
		n = 6
	if n == "Ё":
		n = 7
	if n == "Ж":
		n = 8
	if n == "З":
		n = 9
	if n == "И":
		n = 10
	if n == "Й":
		n = 11
	if n == "К":
		n = 12
	if n == "Л":
		n = 13
	if n == "М":
		n = 14
	if n == "Н":
		n = 15
	if n == "О":
		n = 16
	if n == "П":
		n = 17
	if n == "Р":
		n = 18
	if n == "С":
		n = 19
	if n == "Т":
		n = 20
	if n == "У":
		n = 21
	if n == "Ф":
		n = 22
	if n == "Х":
		n = 23
	if n == "Ц":
		n = 24
	if n == "Ч":
		n = 25
	if n == "Ш":
		n = 26
	if n == "Щ":
		n = 27
	if n == "Ъ":
		n = 28
	if n == "Ы":
		n = 29
	if n == "Ь":
		n = 30
	if n == "Э":
		n = 31
	if n == "Ю":
		n = 32
	if n == "Я":
		n = 33
	if n == "а":
		n = 34
	if n == "б":
		n = 35
	if n == "в":
		n = 36
	if n == "г":
		n = 37
	if n == "д":
		n = 38
	if n == "е":
		n = 39
	if n == "ё":
		n = 40
	if n == "ж":
		n = 41
	if n == "з":
		n = 42
	if n == "и":
		n = 43
	if n == "й":
		n = 44
	if n == "к":
		n = 45
	if n == "л":
		n = 46
	if n == "м":
		n = 47
	if n == "н":
		n = 48
	if n == "о":
		n = 49
	if n == "п":
		n = 50
	if n == "р":
		n = 51
	if n == "с":
		n = 52
	if n == "т":
		n = 53
	if n == "у":
		n = 54
	if n == "ф":
		n = 55
	if n == "х":
		n = 56
	if n == "ц":
		n = 57
	if n == "ч":
		n = 58
	if n == "ш":
		n = 59
	if n == "щ":
		n = 60
	if n == "ъ":
		n = 61
	if n == "ы":
		n = 62
	if n == "ь":
		n = 63
	if n == "э":
		n = 64
	if n == "ю":
		n = 65
	if n == "я":
		n = 66
	if n == "0":
		n = 67
	if n == "1":
		n = 68
	if n == "2":
		n = 69
	if n == "3":
		n = 70
	if n == "4":
		n = 71
	if n == "5":
		n = 72
	if n == "6":
		n = 73
	if n == "7":
		n = 74
	if n == "8":
		n = 75
	if n == "9":
		n = 76
	if n == "!":
		n = 77
	if n == "?":
		n = 78
	if n == ",":
		n = 79
	if n == ".":
		n = 80
	if n == "%":
		n = 81
	if n == "$":
		n = 82
	if n == "+":
		n = 83
	if n == "-":
		n = 84
	if n == "(":
		n = 85
	if n == ")":
		n = 86
	if n == "/":
		n = 87
	if n == '"':
		n = 88
	if n == "'":
		n = 89
	if n == ":":
		n = 90
	if n == ";":
		n = 91
	if n == "=":
		n = 92
	if n == " ":
		n = 93

	key = key_string[r]
	value = int(n + key)

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
	if value == 94:
		print("A", end="")
	if value == 95:
		print("B", end="")
	if value == 96:
		print("C", end="")
	if value == 97:
		print("D", end="")
	if value == 98:
		print("E", end="")
	if value == 99:
		print("F", end="")
	if value == 100:
		print("G", end="")
	if value == 101:
		print("H", end="")
	if value == 102:
		print("I", end="")
	if value == 103:
		print("J", end="")
	if value == 104:
		print("K", end="")
	if value == 105:
		print("L", end="")
	if value == 106:
		print("M", end="")
	if value == 107:
		print("N", end="")
	if value == 108:
		print("O", end="")
	if value == 109:
		print("P", end="")
	if value == 110:
		print("Q", end="")
	if value == 111:
		print("R", end="")
	if value == 112:
		print("S", end="")
	if value == 113:
		print("T", end="")
	if value == 114:
		print("U", end="")
	if value == 115:
		print("V", end="")
	if value == 116:
		print("W", end="")
	if value == 117:
		print("X", end="")
	if value == 118:
		print("Y", end="")
	if value == 119:
		print("Z", end="")
	if value == 120:
		print("a", end="")
	if value == 121:
		print("b", end="")
	if value == 122:
		print("c", end="")
	if value == 123:
		print("d", end="")
	if value == 124:
		print("e", end="")
	if value == 125:
		print("f", end="")
	if value == 126:
		print("g", end="")
	if value == 127:
		print("h", end="")
	if value == 128:
		print("i", end="")
	if value == 129:
		print("j", end="")
	if value == 130:
		print("k", end="")
	if value == 131:
		print("l", end="")
	if value == 132:
		print("m", end="")
	if value == 133:
		print("n", end="")
	if value == 134:
		print("o", end="")
	if value == 135:
		print("p", end="")
	if value == 136:
		print("q", end="")
	if value == 137:
		print("r", end="")
	if value == 138:
		print("s", end="")
	if value == 139:
		print("t", end="")
	if value == 140:
		print("u", end="")
	if value == 141:
		print("v", end="")
	if value == 142:
		print("w", end="")
	if value == 143:
		print("x", end="")
	if value == 144:
		print("y", end="")
	if value == 145:
		print("z", end="")
	if value == 146:
		print("⁰", end="")
	if value == 147:
		print("¹", end="")
	if value == 148:
		print("²", end="")
	if value == 149:
		print("³", end="")
	if value == 150:
		print("⁴", end="")
	if value == 151:
		print("⁵", end="")
	if value == 152:
		print("⁶", end="")
	if value == 153:
		print("⁷", end="")
	if value == 154:
		print("⁸", end="")
	if value == 155:
		print("⁹", end="")
	if value == 156:
		print("¿", end="")
	if value == 157:
		print("⸮", end="")
	if value == 158:
		print("⅕", end="")
	if value == 159:
		print("⅙", end="")
	if value == 160:
		print("⅛", end="")
	if value == 161:
		print("₀", end="")
	if value == 162:
		print("₁", end="")
	if value == 163:
		print("₂", end="")
	if value == 164:
		print("₃", end="")
	if value == 165:
		print("₄", end="")
	if value == 166:
		print("₅", end="")
	if value == 167:
		print("₆", end="")
	if value == 168:
		print("₇", end="")
	if value == 169:
		print("₈", end="")
	if value == 170:
		print("₉", end="")
	if value == 171:
		print("Ⓐ", end="")
	if value == 172:
		print("Ⓑ", end="")
	if value == 173:
		print("Ⓒ", end="")
	if value == 174:
		print("Ⓓ", end="")
	if value == 175:
		print("Ⓔ", end="")
	if value == 176:
		print("Ⓕ", end="")
	if value == 177:
		print("Ⓖ", end="")
	if value == 178:
		print("Ⓗ", end="")
	if value == 179:
		print("Ⓘ", end="")
	if value == 180:
		print("Ⓙ", end="")
	if value == 181:
		print('Ⓚ', end="")
	if value == 182:
		print("Ⓛ", end="")
	if value == 183:
		print("Ⓜ", end="")
	if value == 184:
		print("Ⓝ", end="")
	if value == 185:
		print("Ⓞ", end="")
	if value == 186:
		print("Ⓟ", end="")