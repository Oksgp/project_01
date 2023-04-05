import sqlite3 as sl
con = sl.connect('teatchers.db')
cur = con.cursor()

with con:
    con.execute ("CREATE TABLE Students(Students_Id INTEGER, Student_Name TEXT, School_Id INTEGER);");

with con:
    con.execute ("INSERT INTO Students (Students_Id, Student_Name, School_Id) VALUES ('201', 'Иван', '1'),('202', 'Петр', '2'),('203', 'Анастасия', '3'),('204', 'Игорь', '4');")


cur.execute("SELECT s.Students_Id, s.Student_Name, s.School_Id, sc.School_Name FROM Students AS s LEFT JOIN School AS sc WHERE Students_Id = 201")
rows = cur.fetchall()
print(rows)