from flask import Flask, render_template, request
from caesar_cipher import caesar_cipher_encrypt, caesar_cipher_decrypt

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/caesar', methods=['GET', 'POST'])
def caesar():
    if request.method == 'POST':
        text = request.form['text']
        shift = int(request.form['shift'])
        operation = request.form['operation']
        if operation == 'encrypt':
            result_text = caesar_cipher_encrypt(text, shift)
        elif operation == 'decrypt':
            result_text = caesar_cipher_decrypt(text, shift)
        return render_template('caesar.html', result_text=result_text, text=text, shift=shift, operation=operation)
    return render_template('caesar.html')


if __name__ == '__main__':
    app.run(debug=True)
