from flask import Flask, render_template, request
import unit_values

app = Flask(__name__)

#conversion logic:

def convert_length(length, from_unit, to_unit):
    try:
        # Perform conversion using the dictionary
        return length * unit_values.length_dict[from_unit][to_unit]
    except KeyError:
        # Handle unsupported units
        return "Unsupported unit conversion."
    
def convert_weight(weight, from_unit, to_unit):
    try:
        # Perform conversion using the dictionary
        return weight * unit_values.weight_dict[from_unit][to_unit]
    except KeyError:
        # Handle unsupported units
        return "Unsupported unit conversion."
    
def convert_temp(temp, from_unit, to_unit):
    try:
        # Perform conversion using the dictionary
        return temp * unit_values.temp_dict[from_unit][to_unit]
    except KeyError:
        # Handle unsupported units
        return "Unsupported unit conversion."

#routes:

@app.route('/')

def main():
    return render_template('main.html')


@app.route('/default_page')

def default():
    return render_template('default.html')


@app.route('/convert_length',methods=['POST','GET']) #route that maps the URL to the function.

def length():   #function that will be executed when the route is accessed.
    converted_value = None  # Initialize converted_value to None
    
    # Handle GET request (first visit to the page)
    if request.method == 'GET':
        return render_template('length.html', converted_value=converted_value)

    # Handle POST request (form submission)
    if request.method == 'POST':  #getting the input values from the form
        input_length = float(request.form['length'])
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']

        #return result
        converted_value = convert_length(input_length, from_unit, to_unit)

        return render_template('length.html', converted_value=converted_value)
    
@app.route('/convert_weight',methods=['POST','GET'])

def weight():
    converted_value = None

    if request.method == 'GET':
        return render_template('weight.html', converted_value=converted_value)
    
    if request.method == 'POST':
        input_weight = float(request.form['weight'])
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']

        converted_value = convert_weight(input_weight, from_unit, to_unit)

        return render_template('weight.html', converted_value=converted_value)
    
@app.route('/convert_temp',methods=['POST','GET'])

def temp():
    converted_value = None

    if request.method == 'GET':
        return render_template('temp.html', converted_value=converted_value)
    
    if request.method == 'POST':
        input_temp = float(request.form['temp'])
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']

        converted_value = convert_temp(input_temp, from_unit, to_unit)

        return render_template('temp.html', converted_value=converted_value)
    
if __name__ == '__main__':
    app.run(debug=True)