from h_h.capitalize import capitalize


if capitalize('hello') != 'Hello':
    raise Exception('Тесты не прошли!')

if capitalize('') != '':
    raise Exception('Тесты не прошли!')

print('Тесты прошли!')
