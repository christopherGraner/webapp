import json
from flask import Flask, url_for, render_template

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

with open('data.json') as data:
        States = json.load(data)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/p1")
def render_page1():

    for State in data:
            options += Markup("<option value=\"" + State + "\">" + State + "</option>") #Use Markup so <, >, " are not escaped lt, gt, etc.


    for Year in data:
            options2 += Markup("<option value=\"" + Year + "\">" + Year + "</option>") #Use Markup so <, >, " are not escaped lt, gt, etc.


    return render_template('page1.html', options = options, options2 = options2 )



@app.route("/p2")
def render_page2():
    return render_template('page2.html')

if __name__=="__main__":
    app.run(debug=True)
