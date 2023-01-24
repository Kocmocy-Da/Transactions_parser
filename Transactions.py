from json import load
import datetime


def last_operations(lst, n):
    for i in lst:
        i['date'] = datetime.datetime.strptime(i['date'], '%Y-%m-%dT%H:%M:%S.%f')
    lst.sort(key=lambda x: x['date'], reverse=True)
    return lst[0:n]


def hide_number(adress):
    adr_lst = adress.split()
    if adr_lst[0] == 'Счет':
        adr_lst[1] = f'**{adr_lst[1][-4:]}'
    else:
        num = adr_lst.index(min(adr_lst))
        adr_lst[num] = f'{adr_lst[num][0:4]} {adr_lst[num][4:6]}** **** {adr_lst[num][-4:]}'
    return ' '.join(adr_lst)


with open('operations.json') as file:
    data = [i for i in load(file) if i != {} and i['state'] == 'EXECUTED']

for i in last_operations(data, 5):
    print(i['date'].strftime('%d.%m.%Y'), i['description'])
    if i['description'] == 'Открытие вклада':
        print(hide_number(i['to']))
    else:
        print(f'{hide_number(i["from"])} -> {hide_number(i["to"])}')
    print(i['operationAmount']['amount'], i['operationAmount']['currency']['name'], end='\n\n')
