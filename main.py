from flask import Flask

app = FlaskApp = Flask(__name__)

@app.route("/home")
def dom():
    return "Я <b> знал </b> что ты придешь"


if __name__ == '__main__':
    app.run(
        port=8080,
        debug=True
    )