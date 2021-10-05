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

'''
Calcularea CMMMC pentru n numere date
'''
def get_cmmmc(numbers):
    n = len(numbers)
    for i in range(0, n - 1):
        a = numbers[i]
        b = numbers[i + 1]
        while numbers[i] != numbers[i + 1]:
            if numbers[i] < numbers[i + 1]:
                numbers[i] = numbers[i] + a
                m = numbers[i]
            else:
                numbers[i + 1] = numbers[i + 1] + b
                m = numbers[i + 1]
    return m

'''
Functia test pentru get_cmmdc
'''
def test_get_cmmmc():
    lst = [2, 69, 40, 50, 6, 8, 4, 35]
    assert get_cmmmc(lst) == 96600
    lst_1 = [14, 9, 35, 78]
    assert get_cmmmc(lst_1) == 8190
    lst_2 = [14, 9, 35, 69]
    assert get_cmmmc(lst_2) == 14490

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
        elif option == '2':
            n = int(input('Alegeti numarul de elemente: '))
            lst = []
            print('Introduceti elementele: ')
            for i in range(0, n):
                e = int(input())
                lst.append(e)
            m = get_cmmmc(lst)
            print(f'CMMMC pentru lista data este {m}')
        elif option == 'x':
            break
        else:
            print('Optiune Invalida!')

test_get_temp()
test_get_cmmmc()
main()


