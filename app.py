
from flask import Flask, render_template, send_file
import qrcode
import io
import base64

app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/academics')
def academics():
    return render_template('academics.html')

@app.route('/admissions')
def admissions():
    return render_template('admissions.html')

@app.route('/placement')
def placement():
    return render_template('placement.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/generate-qr')
def generate_qr():
    # Get the current domain URL
    website_url = "https://qrcampus2.onrender.com"  # Replace with your actual deployed URL
    
    # Create QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(website_url)
    qr.make(fit=True)
    
    # Create image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save to bytes
    img_buffer = io.BytesIO()
    img.save(img_buffer, format='PNG')
    img_buffer.seek(0)
    
    return send_file(img_buffer, mimetype='image/png', as_attachment=True, download_name='college_qr_code.png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
