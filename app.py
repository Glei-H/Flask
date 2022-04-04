from crypt import methods
import string
from flask import Flask, redirect, request, url_for
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/estimate', methods= ['POST','GET'])
def estimate():
    if request.method == 'POST':
        form = request.form
        radius = float(form['radius'])
        height = float(form['height'])
        top_area = 3.14 * radius**2
        side_area = 2*3.14*radius*height
        total_area = top_area + side_area
        total_sqft = total_area / 144
        total_material_cost = total_sqft * 25
        total_labor_cost =  total_sqft * 15
        total_cost_estimate = total_labor_cost + total_material_cost
        estimate = round(total_cost_estimate, 2)
        return render_template('estimate.html', quote=estimate)
    return render_template('estimate.html', pageTitle= 'Estimate VPM')
     #print(total_cost_estimate)
        #return redirect(url_for('index'))
    #return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True) #set to false when putting on azure