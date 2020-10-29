import flask_wtf
from wtforms import StringField, SubmitField, TextAreaField, RadioField
from wtforms.validators import DataRequired

categories = [("recommended", "Recommended"), ("tovisit", "Places To Go"), ("visited", "Visited!!!")]


## Create Form Here
class AddLocationForm(flask_wtf.FlaskForm):
  name = StringField("Location Name", validators = [DataRequired()])
  description = TextAreaField("Location Description", validators = [DataRequired()])
  category = RadioField("Category", choices=[("recommended", "Recommended"), ("tovisit", "Places To Go"), ("visited", "Visited!!!")])
  submit = SubmitField("Add Location")