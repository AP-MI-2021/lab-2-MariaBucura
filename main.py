'''
Transformarea unei temperaturi dintr-o scara data intr-o temperatura din alta scara data
'''
def get_temp(temp, frm, to):
    if frm == 'C' and to == 'F':
        conversion = 9 / 5 * temp + 32
        conversion = round(conversion, 3)
    elif frm == 'K' and to == 'F':
        conversion = (temp - 273.15) * 9/5 + 32
        conversion = round(conversion, 3)
    elif frm == 'F' and to == 'C':
        conversion = 5 / 9 * (temp - 32)
        conversion = round(conversion, 3)
    elif frm == 'C' and to == 'K':
        conversion = temp + 273.15
        conversion = round(conversion, 3)
    elif frm == 'K' and to == 'C':
        conversion  = temp - 273.15
        conversion = round(conversion, 3)
    else:
        conversion = 5 / 9 * (temp - 32) + 273.15
        conversion = round(conversion, 3)
    return conversion
'''
Functia test pentru functia get_temp
'''
def test_get_temp():
    assert get_temp(100, 'C', 'F') == 212
    assert get_temp(345, 'K', 'F') == 161.33
    assert get_temp(113, 'F', 'C') == 45
    assert get_temp(113, 'C', 'K') == 386.15
    assert get_temp(113, 'K', 'C') == -160.15
    assert get_temp(123, 'F', 'K') == 323.706
    assert get_temp(35, 'C', 'F') == 95

def main():
    while True:
        print('1. Transformarea unei temperaturi date intr-o alta temperatura.')
        print('2. Calcularea celui mai mic multiplu comun la n numere date.')
        print('x. Iesire din program')
        option = input('Alege optiunea: ')
        if option == '1':
            temp = float(input('Introduceti temperatura: '))
            frm = input('Din: ')
            to = input('In: ')
            c = get_temp(temp, frm, to)
            print(f'{temp} {frm} --> {c} {to}')
        elif option == 'x':
            break
        else:
            print('Optiune Invalida!')

test_get_temp()
main()
