import os
import urllib.request


from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash
import requests
import json

app = Flask(__name__)

# configure to use sqlite db
db = SQL("sqlite:///stats.db")

# set base headers
# parse key from json
with open("keys.json") as json_file:
    key = json.load(json_file)
    # print(key["TBA"][0]["key"])
tbaheads = {'X-TBA-Auth-Key':key,'User-Agent':'irefl@protonmail.com'}


@app.route("/")
# TODO: @login_required
def index():
    status = requests.get("https://www.thebluealliance.com/api/v3/status", params=tbaheads).json()
    # print(status["is_datafeed_down"])

    return render_template("index.html")


# {'android': {'latest_app_version': 6000199, 'min_app_version': 5000000}, 'contbuild_enabled': True, 'current_season': 2020, 'down_events': ['2020mijac'], 'ios': {'latest_app_version': -1, 'min_app_version': -1}, 'is_datafeed_down': False, 'max_season': 2020, 'web': {'commit_time': '2020-03-06 13:10:40 -0500', 'current_commit': '17a5ce6247883c6367eb515165b2eef0d251a790', 'deploy_time': 'Fri Mar  6 18:24:20 UTC 2020', 'endpoints_sha': '', 'tbaClient_endpoints_sha': '', 'travis_job': '659274785'}}