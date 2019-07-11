from flask import abort, redirect, render_template, request, url_for
from .. import db
from . import main
from .forms import CodeForm,CommentForm
from ..models import Code,Comment
from flask_login import login_user, logout_user, login_required, current_user


@main.route('/')
def index():
    return render_template("index.html")


@main.route('/new', methods=['GET', 'POST'])
def new_blog():
    form = CodeForm()
    if form.validate_on_submit():
        code = Code(code=form.code.data, category = form.category.data, code_title=form.code_title.data, user_id = current_user.id,
                    code_upvotes=0, code_downvotes=0)
                
        code.save_blog
        db.session.add(code)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('new.html', code_form=form)

@main.route('/js')
def js():
    codes = Code.query.all()
    return render_template("js.html" ,codes = codes)

@main.route('/git')
def git():
    return render_template("git.html")

@main.route('/new_comment/<int:id>', methods=['GET', 'POST'])
@login_required
def new_comment(id):
    form = CommentForm()
    code = Code.get_blog(id)
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
    form = quizForm()
    if form.validate_on_submit():
        quiz = Quiz(question=form.question.data, category=form.category.data,
                    quiz_title=form.code_title.data, user_id=current_user.id)

        quiz.save_quiz
        db.session.add(quiz)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('quiz.html', quiz_form=form)

