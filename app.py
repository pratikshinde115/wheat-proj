from flask import Flask , request , flash , render_template
import pickle
import pandas as pd

app = Flask(__name__)
app.config['SECRET_KEY'] = '..'


filename = 'model.pkl'
model = pickle.load(open(filename, 'rb'))

transform = pickle.load(open('transform.pkl', 'rb'))


@app.route('/' ,methods = ['POST','GET'])
def home():
    if request.method == 'POST':
        compactness = request.form['compactness']
        length_of_kernel= request.form['length_of_kernel']
        width_of_kernel = request.form['width_of_kernel']
        asymmetry_coefficient = request.form['asymmetry_coefficient']
        length_of_kernel_groove = request.form['length_of_kernel_groove']
        print(compactness)
#validation


        df = pd.DataFrame([[compactness,length_of_kernel,width_of_kernel, asymmetry_coefficient, length_of_kernel_groove]],columns=['compactness','length_of_kernel','width_of_kernel','asymmetry_coefficient','length_of_kernel_groove'])
        predictions = transform.transform(df)
        predictions = model.predict(predictions)
        predictions = int(predictions)
        if predictions == 0:
            predictions = 'Kama'
        elif predictions == 1:
            predictions = 'Rosa'
        else:
            predictions  = 'Canadian'
        print(predictions)



        return render_template('home.html',predictions = predictions)
    else:
        return render_template('home.html')

if __name__ == '__main__':
	app.run(debug=True)