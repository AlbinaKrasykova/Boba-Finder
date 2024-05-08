from flask import Flask, render_template, request
from function import get_api




app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    name, img , rating = None, None, None
    if request.method == 'POST':
        theme = request.form['theme']
        location = request.form['locationName']
        
        name, img, rating  = get_api(theme, location)
        print(name)
        print(img)
        print(rating)

    return render_template('index.html', name=name, rating=rating, img=img )

if __name__ == '__main__':
    app.run(debug=True)