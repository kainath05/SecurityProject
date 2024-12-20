from flask import Flask, render_template, request

from bop_it_cipher import bop_it_cipher_encrypt, bop_it_cipher_decrypt
from caesar_cipher import caesar_cipher_encrypt, caesar_cipher_decrypt
from monoalphabetic_cipher import generate_key, monoalphabetic_cipher_encrypt, monoalphabetic_cipher_decrypt
from vigenère_cipher import vigenere_cipher_encrypt, vigenere_cipher_decrypt
from block_cipher import block_encrypt, block_decrypt
from transposition_cipher import encrypt_transposition, decrypt_transposition

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
            ciphertext = block_encrypt(text, key, block_size)
            result_text = ciphertext.hex()  # Convert to hex for display
        elif operation == "Decrypt":
            ciphertext = bytes.fromhex(request.form["text"])  # Decode from hex
            result_text = block_decrypt(ciphertext, key, block_size).decode("utf-8", errors="replace")

    return render_template(
        "block.html",
        result_text=result_text,
        key=request.form.get("key", ""),
        operation=request.form.get("operation", ""),
        text=request.form.get("text", "")
    )


@app.route('/transposition', methods=['GET', 'POST'])
def transposition():
    result_text = None
    text = ""
    key = ""
    operation = ""

    if request.method == 'POST':
        text = request.form['text']
        key = request.form['key']  # Get the key from the form
        operation = request.form['operation']

        if operation == 'Encrypt':
            result_text = encrypt_transposition(text, key)
        elif operation == 'Decrypt':
            result_text = decrypt_transposition(text, key)

    return render_template(
        'transposition.html',
        result_text=result_text,
        text=text,
        key=key,
        operation=operation
    )


@app.route('/bop_it', methods=['GET', 'POST'])
def bob_it():
    if request.method == 'POST':
        text = request.form['text']
        twist_count = int(request.form['twist_count'])
        pull_count = int(request.form['pull_count'])
        bop_count = int(request.form['bop_count'])
        operation = request.form['operation']
        if operation == 'Encrypt':
            result_text = bop_it_cipher_encrypt(text, twist_count, pull_count, bop_count)
        elif operation == 'Decrypt':
            result_text = bop_it_cipher_decrypt(text, twist_count, pull_count, bop_count)
        return render_template('bop_it.html', result_text=result_text, text=text, twist_count=twist_count,
                               pull_count=pull_count, bop_count=bop_count, operation=operation)
    return render_template('bop_it.html')


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
