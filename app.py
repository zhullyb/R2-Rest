from flask import Flask, send_file, abort
import botocore

from r2 import R2
from vars import info

app = Flask(__name__)
r2 = R2(info)

# Cache for 1 month
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 60 * 60 * 24 * 30


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET'])
def index(path):
    if path == '':
        abort(404)
    try:
        r2_object = r2.get_object(path)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchKey':
            abort(404)
    return send_file(r2_object.get('Body'), mimetype=r2_object.get('ContentType'), download_name=path)


@app.errorhandler(404)
def not_found(e):
    return send_file('assets/404.jpg', mimetype='image/jpg'), 404


@app.errorhandler(500)
def internal_error(e):
    return send_file('assets/500.jpg', mimetype='image/jpg'), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
