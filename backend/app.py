from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return {
      "isWorking": True,
    }

@app.route("/api")
def hello_world2():
    return {
      "isWorking2": True,
    }

if __name__ == "__main__":
    app.run(host='0.0.0.0')
