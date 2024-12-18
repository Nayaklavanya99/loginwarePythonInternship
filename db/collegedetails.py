#student: sid, ename, lname, age,grade,email,enrollment
#course: cid, course_name, dept
#enrollment: eid,sid,cid,sem

import sqlite3

conn = sqlite3.connect("College.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS student")
cur.execute("DROP TABLE IF EXISTS course")
cur.execute("DROP TABLE IF EXISTS enrollment")
# table creation
create_student = """CREATE TABLE IF NOT EXISTS student (
    sid INTEGER PRIMARY KEY,
    ename TEXT NOT NULL,
    lname TEXT NOT NULL,
    age INTEGER NOT NULL,
    grade TEXT NOT NULL,
    email TEXT NOT NULL
    )"""
cur.execute(create_student)

create_course = """CREATE TABLE IF NOT EXISTS course (
    cid INTEGER PRIMARY KEY,
    course_name TEXT NOT NULL,
    dept TEXT NOT NULL
    )"""
cur.execute(create_course)

create_enrollment = """CREATE TABLE IF NOT EXISTS enrollment (
    eid INTEGER PRIMARY KEY,
    sid INTEGER,
    cid INTEGER,
    sem INTEGER,
    FOREIGN KEY (sid) REFERENCES student(sid),
    FOREIGN KEY (cid) REFERENCES course(cid)
    )"""
cur.execute(create_enrollment)




# inserting values to table
insert_student = """INSERT INTO student(sid,ename,lname,age,grade,email) VALUES(1,'sahil','belurkar',22,'A','sahilbelur@example.com'),
(2,'lavanya','nayak',23,'B','lavanayak@example.com'),
(3,'robin','mp',22,'c','robin@example.com'),
(4,'kavya','SR',23,'B','kavya@example.com'),
(5,'Poorvi','gowda',24,'B','poorvi@example.com')"""
cur.execute(insert_student)

insert_course = """INSERT INTO course(cid,course_name, dept) VALUES(1,'computer science','cse'),
(2,'mathematics','math'),
(3,'physics','physics'),
(4,'AI/ML','mca'),
(5,"accounts",'mba')"""
cur.execute(insert_course)

insert_enrollment = """INSERT INTO enrollment(sid, cid, sem) VALUES(1,1,1),
(1,2,2),
(2,1,1),
(3,3,2),
(4, 4, 1),
(5,5,3)
"""
cur.execute(insert_enrollment)


alter_student = """ALTER TABLE student ADD COLUMN eid INTEGER REFERENCES enrollment(eid)"""
cur.execute(alter_student)

update_student = """UPDATE student SET eid = (SELECT eid FROM enrollment WHERE sid = student.sid)"""
cur.execute(update_student)

select_query1 = """SELECT * FROM student"""
cur.execute(select_query1)
student_row1 = cur.fetchall()
print(student_row1[0])
print(student_row1[0][1])
for i in cur.fetchall():
    print(i)
print('-' *20)

select_query2 = """SELECT * FROM course"""
cur.execute(select_query2)
for i in cur.fetchall():
    print(i)
print('-' *20)

select_query1 = """SELECT * FROM enrollment"""
cur.execute(select_query1)
for i in cur.fetchall():
    print(i)
print('-' *20)



conn.commit()
conn.close()

