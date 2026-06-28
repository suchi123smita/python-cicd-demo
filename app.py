from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "CI/CD Pipeline using Jenkins and Docker"

if __name__ == "__main__":
