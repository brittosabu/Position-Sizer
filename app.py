import pandas as pd
from flask import Flask,render_template,request,url_for
from position_sizer import postiion_sizing

app = Flask(__name__)

equities = dict(pd.read_csv('EQUITY_L.csv',usecols=['SYMBOL', 'NAME OF COMPANY'],index_col='SYMBOL')['NAME OF COMPANY'])

@app.route('/',methods=['GET','POST'])
def home():
    
    if request.method == "POST":

        eq = request.form.get('equity')
        bp = float(request.form.get('entry'))
        sl = float(request.form.get('sl'))
        maxloss = int(request.form.get('maxl'))

        print(equities[eq])

        p_size = postiion_sizing(bp,sl,maxloss)

    return render_template('position_sizer.html',equities=equities)
    


if __name__ == "__main__":
    app.run(debug=True)
