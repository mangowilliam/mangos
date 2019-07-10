from flask import render_template, request, redirect, url_for,abort
from . import main
from .. import db
from .forms import CodeForm
from ..models import Code
from flask_login import login_user, logout_user, login_required, current_user


@main.route('/')
def index():
    return render_template("index.html")


@main.route('/new', methods=['GET', 'POST'])
def new_blog():
    form = CodeForm()
    if form.validate_on_submit():
        code = Code(code=form.blog.data, category = form.category.data, code_title=form.blog_title.data, user_id = current_user.id,
                    code_upvotes=0, code_downvotes=0)
                
        code.save_blog
        db.session.add(code)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('new.html', code_form=form)

@main.route('/js')
def js():
    return render_template("js.html")
