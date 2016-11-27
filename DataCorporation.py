# -*- coding: utf-8 -*-

from __future__ import division
from DataCorporationInformation import *


def number_of_friends(user):
    return len(user['friends'])


for first_member, second_member in FRIENDSHIP:
    USERS[first_member]['friends'].append(USERS[second_member])
    USERS[second_member]['friends'].append(USERS[first_member])

total_connections = sum(number_of_friends(user) for user in USERS)

num_users = len(USERS)
avg_connections = total_connections / num_users  #친구수 평균

# (user_id, number_of_friends)로 구성된 list 생성
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in USERS]
# python3 lambda 문법 변경에 따른 소스 수정 -> lambda (x, y): x => lambda x_y: x_y[0]
num_friends_by_id = sorted(num_friends_by_id,
                           key=lambda user_id_num_friends: user_id_num_friends[1],
                           reverse=True)
print(num_friends_by_id)
