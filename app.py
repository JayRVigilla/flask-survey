from flask import Flask, render_template, request, jsonify, redirect
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)

app.config['SECRET_KEY'] = "password"

debug = DebugToolbarExtension(app)

responses = []


@app.route("/")
def landing_page():
    """ Ask user to take a survey with instructions and title"""
    fn_title = satisfaction_survey.title
    fn_instructions = satisfaction_survey.instructions

    return render_template(
            '/home.html',
            survey_title=fn_title,
            survey_instructions=fn_instructions
                            )
