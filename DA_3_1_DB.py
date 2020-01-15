CREATE DATABASE PY_ASSIGNMENT_ANUSHA;
use PY_ASSIGNMENT_ANUSHA;

CREATE TABLE Student_Details(
    Reg_no int(5) PRIMARY key,
    stud_name varchar(10),
    Batch int(4),
    branch varchar(5),
    tot_marks int(3)    );

INSERT INTO `student_details`(`Reg_no`, `stud_name`, `Batch`, `branch`, `tot_marks`) VALUES (001,"Ana",2017,"Ise",502)
UPDATE `student_details` SET tot_marks = tot_marks + 5 where 1

SELECT `Reg_no`, `stud_name`, `Batch`, `branch`, `tot_marks` FROM `student_details` WHERE 1

DROP DATABASE py_assignment_anusha