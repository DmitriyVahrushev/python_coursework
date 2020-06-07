from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FloatField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class PollutionForm(FlaskForm):
    pollution_rate = FloatField('pollution_rate', 
        validators=[DataRequired()])
    city = StringField('City', 
        validators=[DataRequired()])
    region = StringField('Region', validators=[DataRequired()])
    submit = SubmitField('Submit measurement')