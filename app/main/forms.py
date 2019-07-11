from wtforms import StringField, TextAreaField, SubmitField, PasswordField , SelectField
from wtforms.validators import Required
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms import ValidationError
from wtforms.validators import Required,Email,EqualTo
from ..models import Code

class CodeForm(FlaskForm):
    code_title = StringField('Title',validators=[Required()])
    category = SelectField(' Select Category', coerce=int,
            choices=[(0, 'Please Select a category...'), (1, 'JS'),(2, 'CSS'),(3, 'GIT'),(4, 'PYTHON')],
            validators = [Required()])
    code = TextAreaField('Code',validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('comment',validators=[Required()])
    submit = SubmitField('Submit')
  class QuizForm(FlaskForm):
    quiz_title = StringField('Title', validators=[Required()])
    category = SelectField(' Select Category', coerce=int,
                           choices=[(0, 'Please Select a category...'),
                                    (1, 'JS'), (2, 'CSS'), (3, 'GIT'), (4, 'PYTHON')],
                           validators=[Required()])
    Question = TextAreaField('qustion', validators=[Required()])
    submit = SubmitField('Submit')


