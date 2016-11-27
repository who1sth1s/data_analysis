# 회사 구성원
USERS = [
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

# 흥미있는 분야
INTERESTS = [
    (0, 'Hadoop'), (0, 'Big Data'), (0, 'HBase'), (0, 'Java'),
    (0, 'Spark'), (0, 'Storm'), (0, 'Cassandra'), (1, 'NoSQL'),
    (1, 'MongoDB'), (1, 'Cassandra'), (1, 'HBase'), (1, 'Postgres'),
    (2, 'Python'), (2, 'scikit-learn'), (2, 'scipy'), (2, 'numpy'), (2, 'statsmodels')
]

# 친구관계
FRIENDSHIP = [
    (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (2, 4),
    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)
]
