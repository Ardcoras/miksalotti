# coding: utf-8

from flask import render_template, request, Response, redirect
from app import app
from app.forms import *

from email.mime.text import MIMEText
import smtplib

import sys, os

import datetime

@app.route('/', methods=['GET', 'POST'])
def mixture():
  form = MixtureForm()
  if form.validate_on_submit():
#    print(form.file.data.filename, file=sys.stderr)

    pressure_after = form.pressure.data + form.fill_amount.data
    end_mixture = (form.pressure.data / pressure_after * form.o2_bottle_percentage.data) + (form.fill_amount.data / pressure_after * form.o2_fill_percentage.data)
    mod = (form.used_po2.data - (end_mixture / 100)) / (end_mixture / 1000)

    return render_template('result.html', pressure_after=pressure_after, end_mixture=end_mixture, mod=mod)

  return render_template('form.html', form=form)

@app.route('/co2', methods=['GET', 'POST'])
def o2view():
  form = Co2Form()
  if form.validate_on_submit():
#    print(form.file.data.filename, file=sys.stderr)

    pressure_after = form.pressure.data + form.fill_amount.data
    o2_percentage = ((pressure_after * form.o2_target.data) - (form.pressure.data * form.o2_bottle_percentage.data)) / form.fill_amount.data
    mod = (form.used_po2.data - (form.o2_target.data / 100)) / (form.o2_target.data / 1000)

    return render_template('co2_result.html', pressure_after=pressure_after, o2_percentage=o2_percentage, mod=mod)

  return render_template('form.html', form=form)
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
  form = FeedbackForm()
  if form.validate_on_submit():
    body = u"""Viitemuuntimen palautelomakkeella tullut viesti:

Nimi: %s
Sahkopostiosoite: %s
Viesti:
%s""" % (form.name.data, form.email.data, form.message.data)
    msg = MIMEText(body)
    msg['From'] = app.config['EMAIL_FROM']
    msg['To'] = app.config['FEEDBACK_TO']
    msg['Subject'] = "Viitemuunninpalaute"

    server = smtplib.SMTP(app.config['SMTP_SERVER'])
    server.send_message(msg)
    return redirect('/success')

  return render_template('feedback.html', form=form)

@app.route('/success')
def success():
  return render_template('success.html')
