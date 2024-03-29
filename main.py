# import "packages" from flask
from flask import render_template  # import render_template from "public" flask libraries
# import "packages" from "this" project
from __init__ import app  # Definitions initialization
from api.joke import joke_api # Blueprint import api definition
from api.covid import covid_api # Blueprint import api definition.
from api.SATquiz import SATquiz_api
from api.ranking import ranking_api
from api.generater import generater_api

from bp_projects.projects import app_projects # Blueprint directory import projects definition

app.register_blueprint(joke_api) # register api routes
app.register_blueprint(covid_api) # register api routes
app.register_blueprint(SATquiz_api)
app.register_blueprint(ranking_api)
app.register_blueprint(generater_api)
app.register_blueprint(app_projects) # register api routes

@app.errorhandler(404)  # catch for URL not found
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/')  # connects default URL to index() function
def index():
    return render_template("index.html")

@app.route('/quiz/')  # connects /stub/ URL to stub() function
def stub():
    return render_template("quiz.html")

@app.route('/test/')
def test():
    return render_template("test.html")

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/feedback/')
def feedback():
    return render_template("feedback.html")

# this runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
