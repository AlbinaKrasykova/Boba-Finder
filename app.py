from flask import Flask, render_template, request
from function import get_api


api_key = '_WRbNCTbDokxy_wfb5q_8dlFN0ZOMyaB4PTZUxiQZVqHRi29zPpVyyduIGbem_m7XIy9oXw408Cu0LcKTncaTnMOeZ2k2-jcFANJAfjZbZ6bAoWXgZ-hTVTcI2lrZnYx'

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    name, img  = None, None
    if request.method == 'POST':
        users_keyword = request.form['users_keyword']
        
        #location = request.form['locationName']
        location = 'NYC'
        
        name, img = get_api( api_key, users_keyword, location)
        print(name)
        print(img)
        

    return render_template('index.html', name=name,  img=img )

if __name__ == '__main__':
    app.run(debug=True)
  