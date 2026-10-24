--CREATE DATABASE HopeFoundationDB;

--USE HopeFoundationDB;

/*CREATE TABLE Students (
    StudentID INT,
    Name VARCHAR(100),
    Age INT,
    City VARCHAR(50),
    Phone VARCHAR(15),
    Email VARCHAR(100),
    Attendance DECIMAL(5,2),
    Assessment DECIMAL(5,2),
    PlacementStatus VARCHAR(30)
);

INSERT INTO Students
(StudentID, Name, Age, City, Phone, Email, Attendance, Assessment, PlacementStatus)
VALUES
(1001, 'Rahul', 21, 'Pune', '9876543210', 'rahul@gmail.com', 88.50, 82.00, 'Not Placed'),
(1002, 'Abhi', 22, 'Mumbai', '9876543211', 'abhi@gmail.com', 92.00, 90.00, 'Placed'),
(1003, 'Arjunh', 20, 'Pune', '9876543212', 'arjunh@gmail.com', 79.50, 76.00, 'Not Placed');

SELECT * FROM Students;
*/
/*
--create
INSERT INTO Students
(StudentID, Name, Age, City, Phone, Email, Attendance, Assessment, PlacementStatus)
VALUES
(1001, 'Rahul', 21, 'Pune', '9876543210', 'rahul@gmail.com', 88.50, 82.00, 'Not Placed'),

--read
SELECT * FROM Students

--update
UPDATE Students
SET Phone = '888888888'
WHERE StudentID = 1001;

--delete
DELETE FROM Students
WHERE StudentID = 1004;

*/

SELECT * FROM Students;