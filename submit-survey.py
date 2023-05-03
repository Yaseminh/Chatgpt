from flask import Flask, request
import csv
import os

app = Flask(__name__)

@app.route('/anketverisi', methods=['POST'])
def handle_post():
    fieldnames = []  # formdan gelen alan adlarını tutmak için boş bir liste oluşturun

    # formdan gelen verileri alın ve fieldnames listesini güncelleyin
    for key in request.form.keys():
        fieldnames.append(key)

        if os.path.isfile('form-data.csv'):
            dosyadurumu=1;
        else:
            dosyadurumu=0;

    # CSV dosyasını açın ve alan adlarını yazın
    with open('form-data.csv', mode='a', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        if (dosyadurumu==0):
            writer.writeheader()

        # formdan gelen verileri CSV dosyasına yazın
        for i in range(len(request.form.getlist(fieldnames[0]))):
            row_dict = {}
            for fieldname in fieldnames:
                row_dict[fieldname] = request.form.getlist(fieldname)[i]
            writer.writerow(row_dict)

    return 'Form submitted successfully!'


if __name__ == '__main__':
    app.run(debug=True, port=8080, use_reloader=False)