# coding: utf-8

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import DecimalField, StringField, TextAreaField
from wtforms.validators import DataRequired

class MixtureForm(FlaskForm):
  pressure = DecimalField(u'Paine pullossa bar', validators=[DataRequired()])
  o2_bottle_percentage = DecimalField(u'O2-% pullossa', validators=[DataRequired()])
  fill_amount = DecimalField(u'Täytettävä määrä bar', validators=[DataRequired()])
  o2_fill_percentage = DecimalField(u'O2 täyttö-%', validators=[DataRequired()])
  used_po2 = DecimalField(u'Käytetty PO2', validators=[DataRequired()])

class Co2Form(FlaskForm):
  pressure = DecimalField(u'Paine pullossa bar', validators=[DataRequired()])
  o2_bottle_percentage = DecimalField(u'O2-% pullossa', validators=[DataRequired()])
  fill_amount = DecimalField(u'Täytettävä määrä bar', validators=[DataRequired()])
  o2_target = DecimalField(u'O2-% haluttu', validators=[DataRequired()])
  used_po2 = DecimalField(u'Käytetty PO2', validators=[DataRequired()])

class FeedbackForm(FlaskForm):
  name = StringField(u'Nimi')
  email = StringField(u'Sähköpostiosoite')
  message = TextAreaField(u'Viesti', validators=[DataRequired()])
