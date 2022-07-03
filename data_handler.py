import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story():
    return []


def write_data(data: dict):
    with open('test.csv', 'a+') as f:
        #f.write()
        f.write(f"\n{data['id']},{data['title']},{data['user_story']},{data['acceptance_criteria']},{data['business_value']},{data['estimation']},{data['status']}")
        #print(f"{data['id']},{data['title']},{data['user_story']},{data['acceptance_criteria']},{data['business_value']},{data['estimation']},{data['status']}")


d ={"id": 12,
                 "title": "wyslij story title",
                 "user_story": "wyslij user story",
                 "acceptance_criteria": "wyslij cryteria",
                 "business_value": "wyslij business value",
                 "estimation": "wyslij estimation",
                 "status": "wyslij status"
                 }


def read_stats():
    counter = {}
    with open('test.csv', 'r') as data_file:
        for i in data_file.readlines():
            data_file[0]
            splitted_row = i.strip().split(",")
            for j in splitted_row:
                counter[splitted_row[0]] = int(splitted_row[1])
        return counter


print(read_stats())

