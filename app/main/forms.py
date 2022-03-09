from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField,RadioField
from wtforms.validators import DataRequired
from wtforms import ValidationError

class PitchForm(FlaskForm):
    title = StringField('Title',validators = [DataRequired()])
    description= TextAreaField('Add your Pitch!',validators= [DataRequired()])
    category = RadioField('Category', option = [('movtivational Pitch'),('pickup lines Pitch')])
    submit = SubmitField('Submit')

class UpvotesForm(FlaskForm):
    submit = SubmitField()

class DownvotesForm(FlaskForm):
    submit = SubmitField()

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us more about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')