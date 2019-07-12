from flask import abort, redirect, render_template, request, url_for
from .. import db
from . import main
from .forms import CodeForm, CommentForm, QuizForm ,AnswerForm
from ..models import Code, Comment, Quiz, Answer
from flask_login import login_user, logout_user, login_required, current_user


@main.route('/')
def index():
    return render_template("index.html")


@main.route('/new', methods=['GET', 'POST'])
def new_blog():
    form = CodeForm()
    codes = Code.query.all()
    if form.validate_on_submit():
        code = Code(code=form.code.data, category=form.category.data, code_title=form.code_title.data, user_id=current_user.id,
                    code_upvotes=0, code_downvotes=0)

        code.save_code
        db.session.add(code)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('new.html', code_form=form, codes=codes)


@main.route('/js')
def js():
    codes = Code.query.all()
    return render_template("js.html", codes=codes)


@main.route('/git')
def py():
    return render_template("git.html")


@main.route('/py')
def git():
    return render_template("py.html")


@main.route('/new_comment/<int:id>', methods=['GET', 'POST'])
@login_required
def new_comment(id):
    form = CommentForm()
    code = Code.get_code(id)
    comments = Comment.get_comments(id)
    print(comments)
    if form.validate_on_submit():
        comment = Comment(comment=form.comment.data, code_id=code.id)
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('main.js'))
    return render_template('comment.html', comment_form=form, comments=comments)


@main.route('/quiz', methods=['GET', 'POST'])
def quiz():
    form = QuizForm()
    answers = Answer.query.all()
    questions = Quiz.query.all()
    if form.validate_on_submit():
        quiz = Quiz(question=form.Question.data, category=form.category.data,
                    user_id=current_user.id)

        quiz.save_quiz
        db.session.add(quiz)
        db.session.commit()
        return redirect(url_for('main.quiz'))
    return render_template('quiz.html', quiz_form=form, answers=answers, questions=questions)


@main.route('/new_answer/<int:id>', methods=['GET', 'POST'])
@login_required
def new_answer(id):
    form = AnswerForm()
    question = Quiz.get_quiz(id)
    answers = Answer.query.all()
    print(answers)
    if form.validate_on_submit():
        answer = Answer(answer=form.answer.data, quiz_id=question.id)
        db.session.add(answer)
        db.session.commit()
        return redirect(url_for('main.js'))
    return render_template('answer.html', form=form, answers = answers)
