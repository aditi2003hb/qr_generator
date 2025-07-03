from flask import Flask, render_template, request, send_file
import qrcode
import os
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_qr():
    data = request.form.get('data')
    if not data:
        return "No data provided", 400

    # Create QR code
    qr = qrcode.make(data)

    # Save to a BytesIO stream instead of disk
    img_io = BytesIO()
    qr.save(img_io, 'PNG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/png', download_name='qrcode.png')

if __name__ == '__main__':
    app.run(debug=True)
