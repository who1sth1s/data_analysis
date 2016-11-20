# -*- coding: utf-8 -*-
def number_of_friends(user):
    return len(user['friends'])

# 회사 구성원
users = [
    {'id': 0, 'name': 'Hero', 'friends': list()},
    {'id': 1, 'name': 'Dunn', 'friends': list()},
    {'id': 2, 'name': 'Sue', 'friends': list()},
    {'id': 3, 'name': 'Chi', 'friends': list()},
    {'id': 4, 'name': 'Thor', 'friends': list()},
    {'id': 5, 'name': 'Clive', 'friends': list()},
    {'id': 6, 'name': 'Hicks', 'friends': list()},
    {'id': 7, 'name': 'Devin', 'friends': list()},
    {'id': 8, 'name': 'Kate', 'friends': list()},
    {'id': 9, 'name': 'Klein', 'friends': list()}
]

# 구성원끼리의 친구관계
friendship = [
    (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (2, 4),
    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)
]

for first_member, second_member in friendship:
    users[first_member]['friends'].append(users[second_member])
    users[second_member]['friends'].append(users[first_member])

total_connections = sum(number_of_friends(user) for user in users)
