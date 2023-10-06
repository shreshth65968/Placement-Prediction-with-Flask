from flask import Flask, render_template, request
import joblib
import numpy as np
 
app = Flask(__name__)
model = joblib.load("trained_model.pkl")  #

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        gender = request.form.get("gender")
        ssc_p = float(request.form.get("ssc_p"))
        ssc_b = request.form.get("ssc_b")
        hsc_p = float(request.form.get("hsc_p"))
        hsc_b = request.form.get("hsc_b")
        hsc_s = request.form.get("hsc_s")
        degree_p = float(request.form.get("degree_p"))
        degree_t = request.form.get("degree_t")
        workex = request.form.get("workex")
        etest_p = float(request.form.get("etest_p"))
        specialisation = request.form.get("specialisation")
        mba_p = float(request.form.get("mba_p"))


        
        #input_data = [[gender, ssc_p, ssc_b, hsc_p, hsc_b,hsc_s, degree_p, degree_t, workex, etest_p,specialisation, mba_p]]
        int_features=[float(x) for x in request.form.values()]
        input_data=[np.array(int_features)]
        prediction = model.predict(input_data)

        result = "Placed" if prediction[0] == 1 else "Not Placed"
        return render_template("index.html", result=result)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)


    

