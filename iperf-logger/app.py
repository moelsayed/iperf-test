from flask import Flask, request
import logging
app = Flask(__name__)

f = logging.Formatter('%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
h = logging.FileHandler('static/containers.log')

h.setFormatter(f)

root = logging.getLogger()
root.setLevel(logging.DEBUG)
root.addHandler(h)

@app.route('/', methods = ['GET'])
def index():
    if request.args.has_key('cont'):
        root.info("%s %s" % (request.args.get('cont'), request.args.get('mps')) )
    return 'OK\n'


if __name__ == '__main__':
        app.run(host='0.0.0.0', port=80)
