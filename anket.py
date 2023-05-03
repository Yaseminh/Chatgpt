# importing Flask and other modules
from flask import Flask, request, render_template
import json

# Flask constructor
app = Flask(__name__)


@app.route('/create', methods=['POST'])
def register():
    if request.method == 'POST':
        anketalani = request.form['anket_alani']
        sorusayisi= request.form['soru_sayisi']
        cevapsayisi=request.form['cevap_sayisi']
        anketsuresi = request.form['anket_suresi']
        print("anket alani:",  anketalani)
        print("anket süresi:", anketsuresi)
        print("soru sayisi:",sorusayisi)
        print("cevap sayisi:",cevapsayisi)
        anket = {
            "anket_alani":  anketalani,
            "anket_suresi": anketsuresi,
            "soru_sayisi": sorusayisi,
            "cevap_sayisi": cevapsayisi
        }

        with open("anket.json", "w") as f:
            json.dump(anket, f)
    return 'İşlem başarılı'


if __name__ == '__main__':
    app.run(debug=True, port=8080, use_reloader=False)