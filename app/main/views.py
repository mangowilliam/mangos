from flask import abort, redirect, render_template, request, url_for

from .. import db
from . import main


@main.route('/')
def index():
    return render_template("index.html")


@main.route('/js')
def js():
    return render_template("js.html")


@main.route('/quiz', methods=['GET', 'POST'])
def quiz():
    form = quizForm()
    if form.validate_on_submit():
        quiz = Quiz(question=form.question.data, category=form.category.data,
                    quiz_title=form.code_title.data, user_id=current_user.id)

        quiz.save_quiz
        db.session.add(quiz)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('quiz.html', quiz_form=form)
