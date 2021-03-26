from flask import Flask, render_template,request
from covid_india import states

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        state = request.form.get('stateName')
        data=(states.getdata(state))
        activeC=data['Active']
        deathC=data['Death']
        curedC=data['Cured']
        totalC= activeC+curedC+deathC
        result=[state,totalC, activeC, curedC, deathC]
        return render_template('index.html', variable=result)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)