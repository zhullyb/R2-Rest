from flask import Flask, send_file
import botocore

from r2 import R2
from vars import info

app = Flask(__name__)
r2 = R2(info)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET'])
def index(path):
    try:
        r2_object = r2.get_object(path)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchKey':
            return send_file('assets/404.jpg', mimetype='image/jpg'), 404
    return send_file(r2_object.get('Body'), mimetype=r2_object.get('ContentType'), download_name=path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)