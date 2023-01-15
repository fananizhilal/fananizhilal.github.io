from flask import Flask, render_template, request
from sklearn.naive_bayes import GaussianNB
app = Flask(__name__)

# membuat model klasifikasi dengan naive bayes
model = GaussianNB()

# melakukan training model
X_train = df[["IPK", "TAK", "SKS"]]
y_train = df["STATUS"]
model.fit(X_train, y_train)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # mengambil nilai dari inputan
    nama = str(request.form['nama'])
    ipk = float(request.form['ipk'])
    tak = int(request.form['tak'])
    sks = request.form['sks']

    # mengubah kategori menjadi numerik
    if (sks == "BELUM MEMENUHI SYARAT"):
        sks = 0
    else:
        sks = 1

    # melakukan prediksi
    data_baru = [[ipk, tak, sks]]
    hasil_prediksi = model.predict(data_baru)

    #menampilkan hasil prediksi
    if hasil_prediksi[0] == 0:
        hasil_prediksi = "Tepat Waktu"
    else:
        hasil_prediksi = "Tertunda"
    return render_template('index.html', prediction=hasil_prediksi)

if __name__ == '__main__':
    app.run(debug=True)

