from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id':1,
        'title':"Data Analyst",
        'location':'Bangalore, India',
        'salary':'Rs. 10,00,000'
    },
        {
        'id':2,
        'title':"Data scientist",
        'location':'Delhi, India',
        'salary':'Rs. 15,00,000'
    },    {
        'id':3,
        'title':"Front-end Engineer",
        'location':'Remote'
    },    {
        'id':4,
        'title':"Back-end enginner",
        'location':'London',
        'salary':'$120,000'
    }

]

@app.route("/")
def hello():
    return render_template('base.html', jobs=JOBS, company_name='Jovian')

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)#local host