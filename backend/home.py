from flask import Blueprint, render_template
from flask_login import LoginManager, login_required, current_user
import pandas as pd

from models import db, Users

home = Blueprint('home', __name__, template_folder='../frontend')
login_manager = LoginManager()
login_manager.init_app(home)

@home.route('/home', methods=['GET'])
@login_required
def show():
    data2021 = pd.read_csv('2021.csv')
    data_description2021 = data2021.describe()

    sorted_data2021 = data2021.drop('PŁEĆ', axis=1).sort_values(by='LICZBA_WYSTĄPIEŃ', ascending=False)
    stats2021 = {
        'median': data_description2021['LICZBA_WYSTĄPIEŃ']['mean'],
        'avg': data_description2021['LICZBA_WYSTĄPIEŃ']['std'],
        'names_count': data_description2021['LICZBA_WYSTĄPIEŃ']['count'],
        'max_val': data_description2021['LICZBA_WYSTĄPIEŃ']['max'],
        'min_val': data_description2021['LICZBA_WYSTĄPIEŃ']['min'],
        'sorted_names': sorted_data2021.values.tolist()[0:10],
        'sorted_names_names': [item[0] for item in sorted_data2021.values.tolist()[0:10]],
        'sorted_names_values': [item[1] for item in sorted_data2021.values.tolist()[0:10]],
    }

    data2022 = pd.read_csv('2022.csv')
    data_description2022 = data2022.describe()

    sorted_data2022 = data2022.drop('PŁEĆ', axis=1).sort_values(by='LICZBA_WYSTĄPIEŃ', ascending=False)
    stats2022 = {
        'median': data_description2022['LICZBA_WYSTĄPIEŃ']['mean'],
        'avg': data_description2022['LICZBA_WYSTĄPIEŃ']['std'],
        'names_count': data_description2022['LICZBA_WYSTĄPIEŃ']['count'],
        'max_val': data_description2022['LICZBA_WYSTĄPIEŃ']['max'],
        'min_val': data_description2022['LICZBA_WYSTĄPIEŃ']['min'],
        'sorted_names': sorted_data2022.values.tolist()[0:10],
        'sorted_names_names': [item[0] for item in sorted_data2022.values.tolist()[0:10]],
        'sorted_names_values': [item[1] for item in sorted_data2022.values.tolist()[0:10]],
    }

    data2023 = pd.read_csv('2023.csv')
    data_description2023 = data2023.describe()

    sorted_data2023 = data2023.drop('PŁEĆ', axis=1).sort_values(by='LICZBA_WYSTĄPIEŃ', ascending=False)
    stats2023 = {
        'median': data_description2023['LICZBA_WYSTĄPIEŃ']['mean'],
        'avg': data_description2023['LICZBA_WYSTĄPIEŃ']['std'],
        'names_count': data_description2023['LICZBA_WYSTĄPIEŃ']['count'],
        'max_val': data_description2023['LICZBA_WYSTĄPIEŃ']['max'],
        'min_val': data_description2023['LICZBA_WYSTĄPIEŃ']['min'],
        'sorted_names': sorted_data2023.values.tolist()[0:10],
        'sorted_names_names': [item[0] for item in sorted_data2023.values.tolist()[0:10]],
        'sorted_names_values': [item[1] for item in sorted_data2023.values.tolist()[0:10]],
    }

    return render_template('home.html', stats2021=stats2021, stats2022=stats2022, stats2023=stats2023)
