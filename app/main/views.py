from flask import render_template, request, redirect, url_for,abort
from . import main
from .. import db
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

@main.route('/py')
def css():
    return render_template("css.html")

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
