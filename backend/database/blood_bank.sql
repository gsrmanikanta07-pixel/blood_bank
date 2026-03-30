CREATE DATABASE blood_bank;
USE blood_bank;

-- Donors
CREATE TABLE donors (
    donor_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    blood_type VARCHAR(5),
    contact VARCHAR(15),
    last_donation DATE
);

-- Blood Stock
CREATE TABLE blood_stock (
    stock_id INT AUTO_INCREMENT PRIMARY KEY,
    blood_type VARCHAR(5),
    quantity INT
);

-- Hospitals
CREATE TABLE hospitals (
    hospital_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    location VARCHAR(100),
    contact VARCHAR(15)
);

-- Requests
CREATE TABLE requests (
    request_id INT AUTO_INCREMENT PRIMARY KEY,
    hospital_id INT,
    blood_type VARCHAR(5),
    quantity INT,
    request_date DATE,
    status VARCHAR(20),
    FOREIGN KEY (hospital_id) REFERENCES hospitals(hospital_id)
);

-- Issues
CREATE TABLE issues (
    issue_id INT AUTO_INCREMENT PRIMARY KEY,
    request_id INT,
    issue_date DATE,
    units_issued INT,
    FOREIGN KEY (request_id) REFERENCES requests(request_id)
);