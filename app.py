from flask import Flask, jsonify, request, render_template, redirect
import data.graphs_generator as graphs
from util import util_api
from data import stroke_model

app = Flask(__name__)


@app.route('/')
def index_page():
    return render_template("index.html")


@app.route('/probability/', methods=['POST', 'GET'])
def api_prob():
    try:
        information = request.json['information']
    except TypeError or UnboundLocalError:
        return redirect('/')

    # Check to see if the sent data is in the right format (Lists in a list)
    if any(isinstance(x, list) for x in information):
        try:
            prob = stroke_model.calc_prob(information)
            accuracy = stroke_model.model_accuracy()
            data = util_api.prob_api_response(prob, accuracy, None)
        # Check to see if the values of the sent data is the correct value or type
        except ValueError or TypeError:
            data = util_api.prob_api_response(None, None, 'Data sent by client contained incorrect values.')
    else:
        data = util_api.prob_api_response(None, None, 'Data sent by client was incorrectly formatted.')
    return jsonify(data)


@app.errorhandler(404)
def page_not_found(e):
    return redirect('/')


if __name__ == '__main__':
    graphs.generate_graphs()
    app.run(threaded=True, port=5000)
