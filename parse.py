def parse(message):
    lst = message.split(', ')
    if len(lst) != 5:
        print(message)
        print(lst)
        print('Не правильный формат сообщения')
        return -1
    name = lst[0]
    group = lst[1]
    task = lst[2]
    variant = lst[3]
    git = lst[4]

    group_lst = ('212Б', '221Б', '214Б')
    if group not in group_lst:
        print('Неправильный номер группы')
        print('Список проверяемых групп: 212Б, 221Б, 214Б')
        return -2

    if int(task) < 1 or int(task) > 5:
        print('Неправильный номер задания')
        print('Возможный номер задания от 1 до 5')
        return -3

    if int(variant) < 1 or int(variant) > 5:
        print('Неправильный номер варианта')
        print('Возможный номер номер варианта от 1 до 5')
        return -4

    if 'github.com/' not in git:
        print('Некорркетная ссылка')
        return -5

    print('Задание принято, идет проверка...')
    return 1


file = open('message.txt', 'r', encoding='utf8')
message = file.readline()
parse(message)
