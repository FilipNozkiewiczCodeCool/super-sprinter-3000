from flask import Flask, Response, render_template, request, redirect, url_for, Response
#from test.data_test import *
import data_handler

app = Flask(__name__)

list_of_dict = [{"id": 12,
                 "story_title": "wyslij story title",
                 "user_story": "wyslij user story",
                 "acceptance_criteria": "wyslij cryteria",
                 "business_value": "wyslij business value",
                 "estimation": "wyslij estimation",
                 "status": "wyslij status"
                 },
                {"id": 12,
                 "story_title": "wyslij story title",
                 "user_story": "wyslij user story",
                 "acceptance_criteria": "wyslij cryteria",
                 "business_value": "wyslij business value",
                 "estimation": "wyslij estimation",
                 "status": "wyslij status"
                 }]

@app.route('/')
@app.route('/list')
def route_list():
    user_stories = list_of_dict #data_handler.get_all_user_story()

    return render_template('list.html', user_stories=user_stories)

@app.route('/story', methods= ["GET", "POST"])
def send_data():
    data = request.request_form.to_dict()
    list_of_dict.append(data)
    return Response("Story created", status=201)

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
