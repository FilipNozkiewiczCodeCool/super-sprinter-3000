import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story():
    return []


def write_data(data: dict):
    with open(DATA_FILE_PATH, 'a+') as f:
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
    user_stories = []
    with open(DATA_FILE_PATH, 'r') as data_file:
        rows = data_file.readlines()
        headers = rows[0].strip().split(",")
        # print(headers)
        for row in rows[1::]:
            splited_row = row.strip().split(",")
            story = {}
            for h,r in zip(headers, splited_row):
                story[h] = r
            user_stories.append(story)
        return user_stories


        #     data_file[0]
        #     splitted_row = i.strip().split(",")
        #     for j in splitted_row:
        #         counter[splitted_row[0]] = int(splitted_row[1])
        # return counter


ud ={"id": 2,
                 "title": "wyslij story title",
                 "user_story": "wyslij user story",
                 "acceptance_criteria": "wyslij cryteria",
                 "business_value": "wyslij business value",
                 "estimation": "wyslij estimation",
                 "status": "wyslij status"
                 }


def update_story(update_data):
    user_story = read_stats()
    # print(user_story)
    for i,value in enumerate(user_story):
        if int(value["id"]) == int(update_data["id"]):
            user_story[i] = update_data
    with open(DATA_FILE_PATH, 'w+') as f:
        header = list(user_story[0].keys())
        s = ""
        for i,v in enumerate(header):
            if i == len(header)-1:
                s += str(v)
            else:
                s += str(v) + ","
        f.write(s)
        for i,v in enumerate(user_story[0::]):
            tab = []
            for j,val in v.items():
                tab.append(val)
            s = ""
            for i,elem in enumerate(tab):
                if i == len(tab)-1:
                    s += str(elem)
                else:
                    s += str(elem) + ","
            f.write(f"\n{s}")




def delete_story(delete_id):
    user_story = read_stats()
    # print(user_story)
    for i,value in enumerate(user_story):
        if int(value["id"]) == int(delete_id):
            del user_story[i]
    with open(DATA_FILE_PATH, 'w+') as f:
        header = list(user_story[0].keys())
        s = ""
        for i, v in enumerate(header):
            if i == len(header) - 1:
                s += str(v)
            else:
                s += str(v) + ","
        f.write(s)
        for i,v in enumerate(user_story[0::]):
            tab = []
            for j,val in v.items():
                tab.append(val)
            s = ""
            for i, elem in enumerate(tab):
                if i == len(tab) - 1:
                    s += str(elem)
                else:
                    s += str(elem) + ","
            f.write(f"\n{s}")


