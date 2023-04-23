from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    "id":1,
    "title": "Data Analyst",
    'location' : "Bengaluru, India",
    "salary": "USD 130000"
  },
  {
    "id":2,
    "title": "Software Engineer",
    'location' : "Bengaluru, India",
    "salary": "USD 135000"
  },
  {
    "id":3,
    "title": "Data Scientist",
    'location' : "Bengaluru, India",
    "salary": "USD 150000"
  },
  {
    "id":4,
    "title": "Backend Engineer",
    'location' : "Bengaluru, India",
    "salary": "USD 140000"
  },
  
]

@app.route("/")

def hello_world():
  return render_template('home.html', 
                         jobs = JOBS,
                         company_name='Jean')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host = '0.0.0.0', debug=True)