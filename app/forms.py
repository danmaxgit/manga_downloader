from flask_wtf          import FlaskForm
from wtforms            import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import InputRequired, DataRequired

class LoginForm(FlaskForm):
	username    = StringField  (u'Username'   , validators=[DataRequired(), InputRequired()])
	password    = PasswordField(u'Password'   , validators=[DataRequired(), InputRequired()])
	remember_me = BooleanField (u'Remember Me')
	submit 		= SubmitField('Sign In')


class RegisterForm(FlaskForm):	
	username    = StringField  (u'Username'  , validators=[DataRequired()])
	password    = PasswordField(u'Password'  , validators=[DataRequired()])