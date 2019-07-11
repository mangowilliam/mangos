from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import Required


class QuizForm(FlaskForm):
    quiz_title = StringField('Title', validators=[Required()])
    category = SelectField(' Select Category', coerce=int,
                           choices=[(0, 'Please Select a category...'),
                                    (1, 'JS'), (2, 'CSS'), (3, 'GIT'), (4, 'PYTHON')],
                           validators=[Required()])
    Question = TextAreaField('qustion', validators=[Required()])
    submit = SubmitField('Submit')
