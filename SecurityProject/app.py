from flask import Flask, render_template, request
from caesar_cipher import caesar_cipher_encrypt, caesar_cipher_decrypt
from monoalphabetic_cipher import generate_key, monoalphabetic_cipher_encrypt, monoalphabetic_cipher_decrypt
from vigenère_cipher import vigenere_cipher_encrypt, vigenere_cipher_decrypt
from block_cipher import block_encrypt, block_decrypt

app = Flask(__name__)

#  store the key for the session
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
        if operation == 'Encrypt':
            result_text = caesar_cipher_encrypt(text, shift)
        elif operation == 'Decrypt':
            result_text = caesar_cipher_decrypt(text, shift)
        return render_template('caesar.html', result_text=result_text, text=text, shift=shift, operation=operation)
    return render_template('caesar.html')


@app.route('/monoalphabetic', methods=['GET', 'POST'])
def monoalphabetic():
    global key
    if request.method == 'POST':
        text = request.form['text']
        operation = request.form['operation']
        if operation == 'Encrypt':
            result_text = monoalphabetic_cipher_encrypt(text, key)
        elif operation == 'Decrypt':
            result_text = monoalphabetic_cipher_decrypt(text, key)
        return render_template('monoalphabetic.html', result_text=result_text, text=text, key=key, operation=operation)
    return render_template('monoalphabetic.html', key=key)


@app.route('/vigenere', methods=['GET', 'POST'])
def vigenere():
    if request.method == 'POST':
        text = request.form['text']
        key = request.form['key']
        operation = request.form['operation']
        if operation == 'Encrypt':
            result_text = vigenere_cipher_encrypt(text, key)
        elif operation == 'Decrypt':
            result_text = vigenere_cipher_decrypt(text, key)
        return render_template('vigenere.html', result_text=result_text, text=text, key=key, operation=operation)
    return render_template('vigenere.html')

@app.route("/block", methods=["GET", "POST"])
def block():
    result_text = None
    block_size = 16  # Fixed block size

    if request.method == "POST":
        text = request.form["text"].encode("utf-8")
        key_input = request.form["key"]
        operation = request.form["operation"]

        # Ensure the key is exactly block_size bytes, either by truncating or padding
        key = key_input.encode("utf-8")
        if len(key) > block_size:
            key = key[:block_size]
        elif len(key) < block_size:
            key = key.ljust(block_size, b'\0')  # Pad with null bytes

        if operation == "Encrypt":
            result_text = block_encrypt(text, key, block_size)
        elif operation == "Decrypt":
            result_text = block_decrypt(text, key, block_size)
        result_text = result_text.decode("utf-8", errors="ignore")

    return render_template(
        "block.html",
        result_text=result_text,
        key=request.form.get("key", ""),
        operation=request.form.get("operation", ""),
        text=request.form.get("text", "")
    )




if __name__ == '__main__':
    app.run(debug=True)
