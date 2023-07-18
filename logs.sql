create database fca;
use fca;
create table logs(
id INT NOT NULL AUTO_INCREMENT,
date timestamp not null DEFAULT CURRENT_TIMESTAMP(),
action varchar(100), 
parameter varchar(1000),
status varchar(100),
primary key (id)
);
select * from logs;
