mysql> create database datarepproject;
Query OK, 1 row affected (0.01 sec)
mysql> use datarepproject;
Database changed

mysql> create table training(
    -> userid int NOT NULL AUTO_INCREMENT,
    -> name varchar(250) NOT NULL,
    -> trainingrecord varchar(250) NOT NULL,
    -> yearcompleted int,
    -> expiryyear int,
    -> PRIMARY KEY (userid)
    -> );
Query OK, 0 rows affected (0.04 sec)
	
mysql> desc training;
+----------------+--------------+------+-----+---------+----------------+
| Field          | Type         | Null | Key | Default | Extra          |
+----------------+--------------+------+-----+---------+----------------+
| userid         | int(11)      | NO   | PRI | NULL    | auto_increment |
| name           | varchar(250) | NO   |     | NULL    |                |
| trainingrecord | varchar(250) | NO   |     | NULL    |                |
| yearcompleted  | int(11)      | YES  |     | NULL    |                |
| expiryyear     | int(11)      | YES  |     | NULL    |                |
+----------------+--------------+------+-----+---------+----------------+
5 rows in set (0.00 sec)