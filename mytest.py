import unittest

from decimal_to_roman import decimal_to_roman

from roman_to_decimal import roman_to_decimal

class TestDecimalToRoman(unittest.TestCase):
    def test_uno(self):
        # pre condicion
        ### NO HAY ###
        # proceso
        resultado = decimal_to_roman(1)
        # verificacion
        self.assertEqual(resultado, 'I')

    def test_diez(self):
        resultado = decimal_to_roman(10)
        self.assertEqual(resultado, 'X')

    def test_cinco(self):
        resultado = decimal_to_roman(5)
        self.assertEqual(resultado, 'V')

    def test_dos(self):
        resultado = decimal_to_roman(2)
        self.assertEqual(resultado, 'II')

    def test_tres(self):
        resultado = decimal_to_roman(3)
        self.assertEqual(resultado, 'III')

    def test_4(self):
        resultado = decimal_to_roman(4)
        self.assertEqual(resultado, 'IV')

    def test_6(self):
        resultado = decimal_to_roman(6)
        self.assertEqual(resultado, 'VI')

    def test_7(self):
        resultado = decimal_to_roman(7)
        self.assertEqual(resultado, 'VII')

    def test_8(self):
        resultado = decimal_to_roman(8)
        self.assertEqual(resultado, 'VIII')

    def test_9(self):
        resultado = decimal_to_roman(9)
        self.assertEqual(resultado, 'IX')

    def test_11(self):
        resultado = decimal_to_roman(11)
        self.assertEqual(resultado, 'XI')

    def test_13(self):
        resultado = decimal_to_roman(13)
        self.assertEqual(resultado, 'XIII')

    def test_16(self):
        resultado = decimal_to_roman(16)
        self.assertEqual(resultado, 'XVI')

    def test_24(self):
        resultado = decimal_to_roman(24)
        self.assertEqual(resultado, 'XXIV')

    def test_35(self):
        resultado = decimal_to_roman(35)
        self.assertEqual(resultado, 'XXXV')

    def test_46(self):
        resultado = decimal_to_roman(46)
        self.assertEqual(resultado, 'XLVI')

    def test_57(self):
        resultado = decimal_to_roman(57)
        self.assertEqual(resultado, 'LVII')

    def test_68(self):
        resultado = decimal_to_roman(68)
        self.assertEqual(resultado, 'LXVIII')

    def test_89(self):
        resultado = decimal_to_roman(89)
        self.assertEqual(resultado, 'LXXXIX')

    def test_99(self):
        resultado = decimal_to_roman(99)
        self.assertEqual(resultado, 'XCIX')

    def test_100(self):
        resultado = decimal_to_roman(100)
        self.assertEqual(resultado, 'C')

    def test_111(self):
        resultado = decimal_to_roman(111)
        self.assertEqual(resultado, 'CXI')

    def test_222(self):
        resultado = decimal_to_roman(222)
        self.assertEqual(resultado, 'CCXXII')

    def test_333(self):
        resultado = decimal_to_roman(333)
        self.assertEqual(resultado, 'CCCXXXIII')

    def test_444(self):
        resultado = decimal_to_roman(444)
        self.assertEqual(resultado, 'CDXLIV')

    def test_555(self):
        resultado = decimal_to_roman(555)
        self.assertEqual(resultado, 'DLV')

    def test_666(self):
        resultado = decimal_to_roman(666)
        self.assertEqual(resultado, 'DCLXVI')

    def test_999(self):
        resultado = decimal_to_roman(999)
        self.assertEqual(resultado, 'CMXCIX')

    def test_1999(self):
        resultado = decimal_to_roman(1999)
        self.assertEqual(resultado, 'MCMXCIX')

if __name__ == '__main__':
    unittest.main()




class TestRomanToDecimal(unittest.TestCase):
    def test_I(self):
        resultado = roman_to_decimal('I')
        self.assertEqual(resultado, 1)

    def test_II(self):
        resultado = roman_to_decimal('II')
        self.assertEqual(resultado, 2)

    def test_III(self):
        resultado = roman_to_decimal('III')
        self.assertEqual(resultado, 3)

    def test_V(self):
        resultado = roman_to_decimal('V')
        self.assertEqual(resultado, 5)

    def test_X(self):
        resultado = roman_to_decimal('X')
        self.assertEqual(resultado, 10)

    def test_VI(self):
        resultado = roman_to_decimal('VI')
        self.assertEqual(resultado, 6)

    def test_VII(self):
        resultado = roman_to_decimal('VII')
        self.assertEqual(resultado, 7)

    def test_IV(self):
        resultado = roman_to_decimal('IV')
        self.assertEqual(resultado, 4)

    def test_IX(self):
        resultado = roman_to_decimal('IX')
        self.assertEqual(resultado, 9)

if __name__ == '__main__':
    unittest.main()