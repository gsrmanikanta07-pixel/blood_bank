from flask import Flask, request, jsonify
from flask_cors import CORS
from db import get_db

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/donors', methods=['GET'])
def get_donors():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM donors")
    return jsonify(cursor.fetchall())

@app.route('/donors', methods=['POST'])
def add_donor():
    try:
        data = request.get_json()

        name = data.get('name')
        blood_type = data.get('blood_type')
        contact = data.get('contact')
        last_donation = data.get('last_donation')

        db = get_db()
        cursor = db.cursor()

        cursor.execute(
            "INSERT INTO donors (name, blood_type, contact, last_donation) VALUES (%s, %s, %s, %s)",
            (name, blood_type, contact, last_donation)
        )

        db.commit()

        return jsonify({"message": "Donor added"}), 201

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": str(e)}), 500

# ------------------ BLOOD STOCK ------------------
@app.route('/stock', methods=['GET'])
def get_stock():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM blood_stock")
    return jsonify(cursor.fetchall())

@app.route('/stock', methods=['POST'])
def add_stock():
    try:
        data = request.get_json()

        blood_type = data.get('blood_type')
        quantity = data.get('quantity')

        db = get_db()
        cursor = db.cursor()

        cursor.execute(
            "INSERT INTO blood_stock (blood_type, quantity) VALUES (%s, %s)",
            (blood_type, quantity)
        )

        db.commit()
        return jsonify({"message": "Stock added"}), 201

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": str(e)}), 500

# ------------------ HOSPITALS ------------------
@app.route('/hospitals', methods=['GET'])
def get_hospitals():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM hospitals")
    return jsonify(cursor.fetchall())

@app.route('/hospitals', methods=['POST'])
def add_hospital():
    try:
        data = request.get_json()

        name = data.get('name')
        location = data.get('location')
        contact = data.get('contact')

        db = get_db()
        cursor = db.cursor()

        cursor.execute(
            "INSERT INTO hospitals (name, location, contact) VALUES (%s, %s, %s)",
            (name, location, contact)
        )

        db.commit()
        return jsonify({"message": "Hospital added"}), 201

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": str(e)}), 500
# ------------------ REQUESTS ------------------
@app.route('/requests', methods=['GET'])
def get_requests():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM requests")
    return jsonify(cursor.fetchall())

@app.route('/requests', methods=['POST'])
def add_request():
    try:
        data = request.get_json()

        hospital_id = data.get('hospital_id')
        blood_type = data.get('blood_type')
        quantity = data.get('quantity')
        request_date = data.get('request_date')

        db = get_db()
        cursor = db.cursor()

        cursor.execute(
            """INSERT INTO requests 
            (hospital_id, blood_type, quantity, request_date, status) 
            VALUES (%s, %s, %s, %s, 'Pending')""",
            (hospital_id, blood_type, quantity, request_date)
        )

        db.commit()
        return jsonify({"message": "Request added"}), 201

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": str(e)}), 500

# ------------------ ISSUE BLOOD ------------------
@app.route('/issues', methods=['POST'])
def issue_blood():
    try:
        data = request.get_json()

        request_id = data.get('request_id')
        issue_date = data.get('issue_date')
        units_issued = data.get('units_issued')

        db = get_db()
        cursor = db.cursor()

        # insert issue
        cursor.execute(
            "INSERT INTO issues (request_id, issue_date, units_issued) VALUES (%s, %s, %s)",
            (request_id, issue_date, units_issued)
        )

        # update request status
        cursor.execute(
            "UPDATE requests SET status='Issued' WHERE request_id=%s",
            (request_id,)
        )

        # reduce stock
        cursor.execute("""
            UPDATE blood_stock bs
            JOIN requests r ON bs.blood_type = r.blood_type
            SET bs.quantity = bs.quantity - %s
            WHERE r.request_id = %s
        """, (units_issued, request_id))

        db.commit()

        return jsonify({"message": "Blood issued"}), 201

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": str(e)}), 500

# ------------------ ISSUES ------------------
@app.route('/issues', methods=['GET'])
def get_issues():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM issues")
    return jsonify(cursor.fetchall())

if __name__ == '__main__':
    app.run(debug=True)