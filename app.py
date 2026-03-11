from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

industries = ["Education", "Healthcare", "Finance", "Fitness", "Food", "Travel"]

problems = [
"helps students learn faster",
"connects people with experts",
"makes daily tasks easier",
"improves productivity",
"helps people stay healthy"
]

technologies = ["AI", "mobile app", "website", "smart assistant", "automation"]


def generate_idea():
    return random.choice(technologies) + " for " + random.choice(industries) + " that " + random.choice(problems)


@app.route("/")
def home():
    return render_template("index.html", idea=generate_idea())


@app.route("/new_idea")
def new_idea():
    return jsonify({"idea": generate_idea()})


app.run(debug=True)