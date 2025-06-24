import os
import uuid
import numpy as np
from flask import Flask, render_template, request, session, redirect, url_for
from tensorflow.keras.models import load_model
from PIL import Image, ImageOps

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.secret_key = 'your_secret_key'  # Ganti dengan secret key Anda

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

model = load_model('model/final_model.h5', compile=False)

labels = ['Kaos/Atasan', 'Celana Panjang', 'Sweater', 'Gaun', 'Mantel',
          'Sandal', 'Kemeja', 'Sepatu Olahraga', 'Tas', 'Sepatu Boot Pendek']

@app.route('/', methods=['GET', 'POST'])
def form():
    prediction = None
    name = price = description = image_path = None

    products = session.get('products', {str(i): [] for i in range(10)})

    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        description = request.form['description']
        file = request.files['image']

        if file:
            filename = str(uuid.uuid4()) + ".png"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Preprocessing gambar
            img = Image.open(filepath).convert('L')
            img = ImageOps.invert(img)
            img = img.resize((28, 28))
            img = np.array(img).astype('float32') / 255.0
            img = img.flatten()                # Ubah dari (28,28) ke (784,)
            img = img.reshape(1, 784)          # Ubah ke (1, 784) untuk batch

            # Prediksi
            pred = model.predict(img)
            class_id = int(np.argmax(pred))
            prediction = labels[class_id]

            # Simpan produk ke session
            product_data = {
                'name': name,
                'price': price,
                'description': description,
                'image_path': filepath,
                'prediction': prediction
            }
            products[str(class_id)].append(product_data)
            session['products'] = products

            # Simpan data hasil submit ke session untuk GET berikutnya
            session['last_product'] = {
                'name': name,
                'price': price,
                'description': description,
                'image_path': filepath,
                'prediction': prediction
            }
            # Tambahkan pesan pop up produk berhasil ditambahkan
            session['message'] = "✅ Produk berhasil ditambahkan!"

            return redirect(url_for('form'))

    # Ambil data hasil submit jika ada, lalu hapus dari session
    last_product = session.pop('last_product', None)
    if last_product:
        name = last_product['name']
        price = last_product['price']
        description = last_product['description']
        image_path = last_product['image_path']
        prediction = last_product['prediction']

    # Ambil pesan jika ada, lalu hapus dari session
    message = session.pop('message', None)

    return render_template(
        'form.html',
        name=name,
        price=price,
        description=description,
        image_path=image_path,
        prediction=prediction,
        products=products,
        labels=labels,
        message=message
    )

@app.route('/delete_all', methods=['POST'])
def delete_all():
    products = session.get('products', {str(i): [] for i in range(10)})
    # Hapus semua file gambar
    for category in products:
        for product in products[category]:
            image_path = product.get('image_path')
            if image_path and os.path.exists(image_path):
                try:
                    os.remove(image_path)
                except Exception as e:
                    print(f"Gagal menghapus file: {image_path} ({e})")
    session['products'] = {str(i): [] for i in range(10)}
    session['message'] = "🎉 Semua produk berhasil dihapus!"
    return redirect(url_for('form'))

@app.route('/delete_product/<category>/<int:product_idx>', methods=['POST'])
def delete_product(category, product_idx):
    products = session.get('products', {str(i): [] for i in range(10)})
    if category in products and 0 <= product_idx < len(products[category]):
        # Hapus file gambar jika ada
        image_path = products[category][product_idx].get('image_path')
        if image_path and os.path.exists(image_path):
            try:
                os.remove(image_path)
            except Exception as e:
                print(f"Gagal menghapus file: {image_path} ({e})")
        products[category].pop(product_idx)
        session['products'] = products
        session['message'] = "🗑️ Produk berhasil dihapus!"
    return redirect(url_for('form'))

if __name__ == '__main__':
    app.run(debug=True)