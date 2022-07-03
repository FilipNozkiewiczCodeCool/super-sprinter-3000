from flask import Flask, Response, render_template, request, redirect, url_for, Response
#from test.data_test import *

import data_handler as dh

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
    user_stories = dh.read_stats()

    return render_template('list.html', user_stories=user_stories)

@app.route('/story', methods = ["GET","POST"])
def story():
    data = request.form.to_dict()
    # list_of_dict.append(data)
    dh.write_data(data)
    return redirect("list")


@app.route('/update_story', methods = ["GET","POST"])
def update_story():
    data = request.form.to_dict()
    # list_of_dict.append(data)
    dh.update_story(data)
    return redirect("list")

@app.route("/add_story", methods=["GET"])
def method():
    return render_template('add_story.html')

@app.route("/add_story_to_update", methods=["GET"])
def add_story_to_update():
    user_stories = dh.read_stats()
    return render_template('update_data.html',user_stories=user_stories)


@app.route("/add_delete_story", methods=["GET"])
def add_delete_story():
    user_stories = dh.read_stats()
    return render_template('delete_story.html', user_stories=user_stories)

@app.route('/delete_story', methods = ["GET","POST"])
def delete_story():
    data = request.form.get("id")
    # list_of_dict.append(data)
    # print(data)
    dh.delete_story(data)
    return redirect("list")


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
