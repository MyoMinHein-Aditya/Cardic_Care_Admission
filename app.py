from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Initial Patient Data

patients = [
    {"id": 1, "name": "Aditya", "hr": "80", "bp": "120/80", "status": "Stable"}
]

@app.route('/')
def dashboard():
    return render_template('index.html', patients=patients)

@app.route('/add', methods=['POST'])
def add_patient():
    name = request.form.get('name')
    hr_str = request.form.get('hr')
    bp = request.form.get('bp')
    
    hr = int(hr_str) if hr_str else 0
    
    if hr > 100 or hr < 60:
        status = "High-Risk"
    else:
        status = "Stable"
    
    # Create unique ID based on the highest existing ID + 1
    new_id = max([p['id'] for p in patients], default=0) + 1
    
    new_patient = {"id": new_id, "name": name, "hr": hr, "bp": bp, "status": status}
    patients.append(new_patient)
    return redirect('/')

@app.route('/remove/<int:patient_id>')
def remove_patient(patient_id):
    global patients
    patients = [p for p in patients if p['id'] != patient_id]
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)