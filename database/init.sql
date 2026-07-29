CREATE TABLE employees (

    id SERIAL PRIMARY KEY,

    username VARCHAR(50),

    fullname VARCHAR(100),

    department VARCHAR(50)

);

INSERT INTO employees(username,fullname,department)

VALUES

('alice','Alice Johnson','IT'),

('bob','Bob Smith','Finance'),

('charlie','Charlie Brown','HR'),

('david','David Miller','Security');