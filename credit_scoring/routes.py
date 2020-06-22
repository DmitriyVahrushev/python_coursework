from credit_scoring import app
from flask import render_template, url_for,flash,redirect
from credit_scoring.forms import CreditScoreForm
import pickle
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

filename = 'credit_scoring/rf_fitted_model.sav'
model = pickle.load(open(filename, 'rb'))

@app.route('/', methods = ['GET', 'POST'])
def homepage():
    form = CreditScoreForm()
    if form.validate_on_submit():
        print("hello")
        data_for_prediction  = np.array([
            form.RevolvingUtilizationOfUnsecuredLines.data ,
            form.age.data ,
            form.NumberOfTime30DaysPastDueNotWorse.data ,
            form.DebtRatio.data ,
            form.MonthlyIncome.data ,
            form.NumberOfOpenCreditLinesAndLoans.data ,
            form.NumberOfTimes90DaysLate.data ,
            form.NumberRealEstateLoansOrLines.data ,
            form.NumberOfTime60DaysPastDueNotWorse.data ,
            form.NumberOfDependents.data
        ])
        data_for_prediction = data_for_prediction.reshape(1,-1)
        pred = model.predict(data_for_prediction)
        print(pred)
        if pred[0] == 1:
            flash(f'Кредит не рекомендуется одобрять.', 'danger')
        else:
            flash(f'Кредит рекомендуется одобрить.', 'success')
        return redirect(url_for('homepage'))
    return render_template("index.html", form = form)