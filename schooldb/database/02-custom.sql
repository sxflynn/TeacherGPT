BEGIN TRANSACTION;

-- Important Note:
-- If you have previously run this Docker setup, you may need to delete the existing Docker Postgres volume 
-- to apply these initialization commands. Use the following commands to list and remove Docker volumes:
-- 
-- List all Docker volumes:
-- docker volume ls
-- 
-- Remove a specific Docker volume:
-- docker volume rm [name-of-postgres-volume]

-- Custom SQL Section
-- Users can add their custom SQL commands here.
-- For example, to create a new table, use:
-- CREATE TABLE my_table (
--   column1 datatype,
--   column2 datatype,
--   column3 datatype,
--   ...
-- );

-- More custom SQL commands can be added below.

-- "assignment_types"
-- "attendance_types"
-- "department"
-- "period_list"
-- "rooms"
-- "sped_categories"
-- "staff"
-- "student"


INSERT INTO "student" ("first_name","middle_name","last_name","sex","dob","email","ohio_ssid")
VALUES
('Monty','Nathaniel','Anthony','M','2010-03-18','moanthony28@titanacademy.edu','WW4542553'),
('Lacey','Aubrey','Baldwin','F','2009-11-09','labaldwin28@titanacademy.edu','QE2954355'),
('Hasan','Jake','Bell','M','2009-06-02','habell28@titanacademy.edu','ZI6882339'),
('Richard','Joshua','Bradshaw','M','2010-04-11','ribradshaw28@titanacademy.edu','IS5669694'),
('Aliya','Amelia','Castro','F','2010-01-27','alcastro28@titanacademy.edu','QN7419694'),
('Hayley','Gianna','Cervantes','F','2009-05-10','hacervantes28@titanacademy.edu','TM3366377'),
('Leonardo','Ryan','Chambers','M','2009-05-28','lechambers28@titanacademy.edu','KG5565391'),
('Aston','Hudson','Chen','M','2009-10-13','aschen28@titanacademy.edu','AR3083975'),
('Rowan','Jason','Chung','M','2010-02-25','rochung28@titanacademy.edu','CD1841601'),
('Bailey','Hunter','Daugherty','M','2010-05-27','badaugherty28@titanacademy.edu','MT5173345'),
('Iona','Audrey','Dunn','F','2009-07-24','iodunn28@titanacademy.edu','UW3272831'),
('Alina','Bailey','Figueroa','F','2009-05-03','alfigueroa28@titanacademy.edu','PX3295318'),
('Alexandra','Anna','Finley','F','2010-04-23','alfinley28@titanacademy.edu','BB4694356'),
('Josh','Dylan','Frank','M','2009-07-04','jofrank28@titanacademy.edu','CA5276526'),
('Henri','Jackson','Frost','M','2010-07-28','hefrost28@titanacademy.edu','YX4224517'),
('Bruno','Hayden','Gates','M','2010-07-20','brgates28@titanacademy.edu','VB3884835'),
('Frazer','Caleb','Glenn','M','2009-05-08','frglenn28@titanacademy.edu','QP4345374'),
('Rory','Asher','Hanna','M','2010-04-29','rohanna28@titanacademy.edu','DN5658819'),
('Inaya','Katherine','Hobbs','F','2009-05-19','inhobbs28@titanacademy.edu','IU5280418'),
('Rio','Justin','Jones','M','2009-08-21','rijones28@titanacademy.edu','JT6485526'),
('Halima','Sienna','Lam','F','2010-03-29','halam28@titanacademy.edu','LU2601847'),
('Sami','Benjamin','Lester','M','2010-04-09','salester28@titanacademy.edu','JX4802309'),
('Daniyal','David','Mack','M','2010-01-21','damack28@titanacademy.edu','EI6068314'),
('Joseph','Logan','Mann','M','2010-03-16','jomann28@titanacademy.edu','VO2336156'),
('Keegan','Brody','Mayo','M','2010-03-17','kemayo28@titanacademy.edu','CQ2574241'),
('Taylor','Stella','Mcclain','F','2010-05-22','tamcclain28@titanacademy.edu','WR2051785'),
('Natasha','Allison','Mendez','F','2009-09-25','namendez28@titanacademy.edu','MX1925335'),
('Luna','Jordyn','Monroe','F','2009-07-12','lumonroe28@titanacademy.edu','EQ1633507'),
('Lauren','Aaliyah','Moon','F','2010-06-17','lamoon28@titanacademy.edu','LN5643005'),
('Tegan','Alexa','Moyer','F','2010-01-01','temoyer28@titanacademy.edu','FJ4463680'),
('Nicole','Savannah','Ochoa','F','2010-02-03','niochoa28@titanacademy.edu','MC5553862'),
('Mia','Lillian','Phelps','F','2009-06-16','miphelps28@titanacademy.edu','CJ8061498'),
('Ruth','Penelope','Pollard','F','2010-03-07','rupollard28@titanacademy.edu','WD6338083'),
('Dawid','Mason','Pope','M','2010-01-20','dapope28@titanacademy.edu','XY4538112'),
('Leyla','Caroline','Prince','F','2010-01-02','leprince28@titanacademy.edu','BH7409472'),
('Alesha','Kate','Pugh','F','2009-09-06','alpugh28@titanacademy.edu','YO1314429'),
('Evie-Rose','Harper','Schroeder','F','2010-01-03','evschroeder28@titanacademy.edu','UF1852409'),
('Umar','Owen','Soto','M','2010-06-10','umsoto28@titanacademy.edu','QQ1097255'),
('Henri','Adam','Stout','M','2009-10-03','hestout28@titanacademy.edu','IE8428552'),
('Tabitha','Charlotte','Thomas','F','2009-11-01','tathomas28@titanacademy.edu','WC8121978');





COMMIT;
