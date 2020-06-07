from airpollutionmetr import app, db
from flask import render_template, url_for,flash,redirect
from airpollutionmetr.forms import PollutionForm
from airpollutionmetr.models import Pollution

@app.route('/', methods = ['GET', 'POST'])
def homepage():
    form = PollutionForm()
    if form.validate_on_submit():
        polution_rate = form.pollution_rate.data
        city  = form.city.data
        region = form.region.data
        user = Pollution(pollution_rate = polution_rate, city = city, region = region)
        db.session.add(user)
        db.session.commit()
        flash(f'Mesurement recorded! Thanks', 'success')
        return redirect(url_for('homepage'))
    return render_template("index.html", form = form)

@app.route('/results')
def results():
    city_counts = {} 
    db_res = Pollution.query.all()
    for measure in db_res:
        if measure.city not in  city_counts:
            city_counts[measure.city] = 1
        else:
            city_counts[measure.city] += 1 
    return render_template("results.html", city_counts = city_counts)