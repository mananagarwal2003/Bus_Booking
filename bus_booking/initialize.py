import sqlite3
conn = sqlite3.connect("bus_reservation_211b420.db")
cur=conn.cursor()
cur.execute('create table Operator(Op_Id int PRIMARY KEY, Name varchar(20), Address varchar(20), Email varchar(50), Phone int(12));')
cur.execute('create table Route(Route_Id int(10), S_Id int(10), Sname varchar(10), PRIMARY KEY(Route_Id,S_Id));')
cur.execute('create table Bus(Bus_Id int PRIMARY KEY, Type varchar(10),Capacity int(5),Fare int(10),Route_Id int(10),Op_Id int(10),CONSTRAINT fk_route FOREIGN KEY(Route_Id) REFERENCES Route(Route_Id),CONSTRAINT fk_opID FOREIGN KEY(Op_Id) REFERENCES operator(op_Id));')
cur.execute('create table Runs(Bus_Id int(10),Date varchar(10), Seat_Available int(5),CONSTRAINT fk_bus FOREIGN KEY(bus_Id) REFERENCES BUS(Bus_Id));')
cur.execute('create table Booking_history(Reference_Id int auto_increment Primary Key,Name varchar(20),Phone numeric(11),Age int(10),Gender varchar(10),Boarding varchar(10),Upto varchar(10),Travelling_Date date,Booking_date date, Seates_booked int(10),Bus_Id int(10),fare numeric(10))')

cur.execute('insert into Operator values(01,"Kamla","Jhansi","kamlatravel@gmail.com",884531259);');
cur.execute('insert into Operator values(02,"Babu","Kanpur","Babutravel@gmail.com",963258741)');

cur.execute('insert into Route values(30,1,"Ajmer");')
cur.execute('insert into Route values(30,2,"Nasirabad");')
cur.execute('insert into Route values(30,3,"Kekri")')
cur.execute('insert into Route values(30,4,"Bundi");')
cur.execute('insert into Route values(30,5,"Kota");')

cur.execute('insert into Route values(32,1,"Kota");')
cur.execute('insert into Route values(32,2,"Bundi");')
cur.execute('insert into Route values(32,3,"Kekri");')
cur.execute('insert into Route values(32,4,"Nasirabad");')
cur.execute('insert into Route values(32,5,"Ajmer");')

cur.execute('insert into Bus values(21,"AC 2x2",50,1000,30,01);')
cur.execute('insert into Bus values(22,"Non Ac2x2",60,800,32,02);')

cur.execute('insert into Runs values(21,"28/12/22",50);')
cur.execute('insert into Runs values(22,"29/12/22",60);')
conn.commit()
conn.close







