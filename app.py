from flask import Flask, render_template, request
from flask_cors import cross_origin
from sklearn.preprocessing import StandardScaler
import pickle

application = Flask(__name__) # initializing a flask app
app=application
@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            process_temp =float(request.form['process_temp'])
            rotational_speed = float(request.form['rotational_speed'])
            hdf = float(request.form['hdf'])

            filename = 'final_a141_2020_predictive_model.pickle'
            loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage
            # predictions using the loaded model file
            print(filename)
            print(process_temp,rotational_speed,hdf)

            prediction=loaded_model.predict([[process_temp,rotational_speed,hdf]])
            print('prediction is', prediction)
            # showing the prediction results in a UI
            return render_template('results.html',prediction=round(prediction[0],2))
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    application.run(debug=True) # running the app

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
