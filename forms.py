from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField
from wtforms.validators import DataRequired, NumberRange

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class TransferForm(FlaskForm):
    from_account = StringField('From', validators=[DataRequired()])
    to_account = StringField('To', validators=[DataRequired()])
    amount = IntegerField('Amount', validators=[DataRequired(), NumberRange(min=1, max=1000)])
