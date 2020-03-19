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
            'home.html',
            survey_title=fn_title,
            survey_instructions=fn_instructions
                            )


@app.route('/questions/<int:length>')
def question(length):
    """ Adding a for to question page"""

    length = len(responses)
    question_list = satisfaction_survey.questions
    asking_question = question_list[length].question
    the_choices = question_list[length].choices

    return render_template(
            'questions_page.html',
            asking_question=asking_question,
            the_choices=the_choices
                            )



@app.route('/answer', methods=["post"])
def handle_answer():
    """redirects to next question, appends the responses"""
    
    extracted_answer = request.form.get('answers')
    responses.append(extracted_answer)

    length = len(responses)

    return redirect(f"/questions/{length}")


@app.route(f"/questions/{len(satisfaction_survey.questions)}")
def thank_you():
    """after survery is done landing on a thank page"""

    return redirect('/thankyou')


@app.route('/thankyou')
def add_thankyou():
    """renders thank you html to page"""

    final_thanks = "Thank you for taking our survey"

    return render_template(
        "thankyou.html",
        thanks=final_thanks
                            )
