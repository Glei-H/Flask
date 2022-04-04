from crypt import methods
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
        radius = form['radius']
        height = form['height']
        top_area = 3.14 * radius^2
        side_area = 2(3.14(radius*height))
        total_area = top_area + side_area
        total_sqft = total_area / 144
        material_cost = 25
        total_material_cost = total_sqft * material_cost
        labor_cost = 15
        total_labor_cost =  total_sqft * labor_cost
        total_cost_estimate = total_labor_cost + total_material_cost
        #fname = form['radius']
        #lname = form['diameter']
        #return redirect(url_for('index'))
    #return redirect(url_for('index'))
    return render_template('estimate.html', pageTitle= 'Estimate VPM')

if __name__ == '__main__':
    app.run(debug=True) #set to false when putting on azure