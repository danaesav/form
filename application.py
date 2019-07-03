import cs50
import csv
import re

from flask import Flask, jsonify, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def register():
    return render_template("form.html")

@app.route("/", methods=["GET"])
def get_index():
    return redirect("/form")


@app.route("/form", methods=["GET"])
def get_form():
    return render_template("form.html")


@app.route("/form", methods=["POST"])
def post_form():
    file = open("survey.csv", "a")
    writer = csv.writer(file)
    print(request.form.get("email"))
    x = request.form.get("dorm")
    if x != "select":
        writer.writerow((request.form.get("email"), request.form.get("password"), request.form.get("dorm"), request.form.get("gender")))
        file.close()
        return redirect("/sheet")
    else:
        return redirect("/form")
        
@app.route("/sheet", methods=["GET"])
def get_sheet():
    file = open("survey.csv", "r")
    reader = csv.reader(file)
    students = list(reader)
    file.close()
    return render_template("table.html", students=students)
