import requests
from flask import render_template, session
import json
from site_web import site_blueprint
from app import api_address
from site_web.site_login import require_type


@site_blueprint.route('/engineer')
@require_type(['ENGINEER', 'ADMIN'])
def engineer():
    """
    Load cars from api and pass to car list view
    Returns: view

    """
    # car_data1 = requests.get(f"{api_address}/api/engineer/car",
    #                         headers=session['auth'])
    # carLoc = json.loads(car_data1.json())
    # print(carLoc)

    car_data = requests.get(f"{api_address}/api/engineer/car",
                            headers=session['auth'])
    mycar=car_data.json()
    lengther = len(mycar)
    print(type(mycar))
    print(lengther)
    return render_template('engineer.html', cars=mycar, leng=lengther)