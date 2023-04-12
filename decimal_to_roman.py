import unittest

def decimal_to_roman(decimal):
    resultado = ''
    if decimal >= 1000:
        resultado = 'M'
        decimal -= 1000
    if decimal >= 100:
        centenas = decimal // 100 # 108 -> centena 1
        decimal -= centenas * 100 # decimal = 1 * 100 - 108
        if centenas <= 3:
            resultado = 'C' * centenas
        elif centenas == 4:
            resultado += 'CD'
        elif centenas <= 8:
            resultado += 'D' + (centenas - 5) * 'C'
        elif centenas <= 9:
            resultado += 'CM'
    if decimal >= 10:
        decenas = decimal // 10
        if decenas <= 3:
            resultado += 'X' * decenas
        elif decenas == 4:
            resultado += 'XL'
        elif decenas <= 8:
            resultado += 'L' + (decenas - 5) * 'X'
        elif decenas == 9:
            resultado += 'XC'
        decimal = decimal % 10
    if decimal <= 3:
        resultado += 'I' * decimal
    elif decimal == 4:
        resultado += 'IV'
    elif decimal <= 8:
        resultado += 'V' + (decimal - 5) * 'I'
    elif decimal == 9:
        resultado += 'IX'
    return resultado
