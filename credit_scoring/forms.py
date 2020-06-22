from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FloatField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class CreditScoreForm(FlaskForm):
    RevolvingUtilizationOfUnsecuredLines = FloatField('Total balance on credit cards and personal lines of credit except real estate and no installment debt like car loans divided by the sum of credit limits', 
        validators=[DataRequired()])
    age = FloatField('Age of borrower in years', 
        validators=[DataRequired()])
    NumberOfTime30DaysPastDueNotWorse = FloatField('Number of times borrower has been 30-59 days past due but no worse in the last 2 years.', 
        validators=[DataRequired()])
    DebtRatio = FloatField('Monthly debt payments, alimony,living costs divided by monthy gross income', 
        validators=[DataRequired()])
    MonthlyIncome = FloatField('Monthly income', 
        validators=[DataRequired()])
    NumberOfOpenCreditLinesAndLoans = FloatField('Number of Open loans (installment like car loan or mortgage) and Lines of credit (e.g. credit cards)', 
        validators=[DataRequired()])
    NumberOfTimes90DaysLate = FloatField('Number of times borrower has been 90 days or more past due.', 
        validators=[DataRequired()])
    NumberRealEstateLoansOrLines = FloatField('Number of mortgage and real estate loans including home equity lines of credit', 
        validators=[DataRequired()])
    NumberOfTime60DaysPastDueNotWorse = FloatField('Number of times borrower has been 60-89 days past due but no worse in the last 2 years.', 
        validators=[DataRequired()])
    NumberOfDependents = FloatField('Number of dependents in family excluding themselves (spouse, children etc.)', 
        validators=[DataRequired()])
    submit = SubmitField('Проверить')