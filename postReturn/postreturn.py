from flask import make_response, request, Flask

app = Flask(__name__)

cache = ""


@app.route('/', methods=['GET', 'POST'])
def page():
    global cache
    if request.method == "GET":
        return cache
    else:
        cache = request.data
        return "true"


app.run(port=3000)
