from flask import Flask, render_template, request
from caesar_cipher import caesar_cipher_encrypt, caesar_cipher_decrypt
from monoalphabetic_cipher import generate_key, monoalphabetic_cipher_encrypt, monoalphabetic_cipher_decrypt

app = Flask(__name__)

# Store the key for the session
key = generate_key()


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


@app.route('/monoalphabetic', methods=['GET', 'POST'])
def monoalphabetic():
    global key
    if request.method == 'POST':
        text = request.form['text']
        operation = request.form['operation']
        if operation == 'encrypt':
            result_text = monoalphabetic_cipher_encrypt(text, key)
        elif operation == 'decrypt':
            result_text = monoalphabetic_cipher_decrypt(text, key)
        return render_template('monoalphabetic.html', result_text=result_text, text=text, key=key, operation=operation)
    return render_template('monoalphabetic.html', key=key)


if __name__ == '__main__':
    app.run(debug=True)
