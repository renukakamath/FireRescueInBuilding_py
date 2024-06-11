/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - fire_py
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`fire_py` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `fire_py`;

/*Table structure for table `building` */

DROP TABLE IF EXISTS `building`;

CREATE TABLE `building` (
  `building_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `owner` varchar(30) DEFAULT NULL,
  `place` varchar(30) DEFAULT NULL,
  `phone` varchar(30) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `latitude` varchar(30) DEFAULT NULL,
  `longitude` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`building_id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `building` */

insert  into `building`(`building_id`,`login_id`,`owner`,`place`,`phone`,`email`,`latitude`,`longitude`) values 
(1,4,'renuka','kerala','2345678907','renukakamath@gmail.com','1234567890','12345678'),
(2,6,'ghjk','fghj','1234578908','user@gmail.com','dfghj','dfghj'),
(3,7,'ghjk','fghj','1234578908','user@gmail.com','dfghj','dfghj'),
(4,8,'ghjk','fghj','1234578908','user@gmail.com','dfghj','dfghj'),
(5,9,'ghjk','fghj','1234578908','user@gmail.com','dfghj','dfghj'),
(6,10,'renuka','kerala','2345678907','renukakamath@gmail.com','1234567890','12345678'),
(7,11,'renuka','kerala','2345678907','renukakamath@gmail.com','1234567890','12345678'),
(8,12,'renuka','kerala','2345678907','renukakamath@gmail.com','1234567890','12345678'),
(9,13,'renuka','kerala','2345678907','renukakamath@gmail.com','1234567890','12345678');

/*Table structure for table `emergency` */

DROP TABLE IF EXISTS `emergency`;

CREATE TABLE `emergency` (
  `emergency_id` int(11) NOT NULL AUTO_INCREMENT,
  `request_id` int(11) DEFAULT NULL,
  `officer_id` int(11) DEFAULT NULL,
  `details` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`emergency_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `emergency` */

insert  into `emergency`(`emergency_id`,`request_id`,`officer_id`,`details`) values 
(1,1,1,'HGKJGJ');

/*Table structure for table `image` */

DROP TABLE IF EXISTS `image`;

CREATE TABLE `image` (
  `image_id` int(11) NOT NULL AUTO_INCREMENT,
  `building_id` int(11) DEFAULT NULL,
  `image` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`image_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `image` */

insert  into `image`(`image_id`,`building_id`,`image`) values 
(1,1,'static/image/8f986e4c-9546-4262-a09f-b3de384cf02a4.jfif'),
(2,1,'static/image/c0c9a442-cf53-4769-a5b6-fbc0fcb50bd1360_F_292075696_hGdSBQ9Bvf1jsaVMP2rTpuRr0VMATck0.jpg');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `type` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`type`) values 
(1,'user','user','user'),
(2,'officer','officer','officer'),
(5,'admin','admin','admin'),
(4,'owner','owner','owner'),
(6,'fghj','dfghj','owner'),
(7,'fghj','dfghj','owner'),
(8,'fghj','dfghj','owner'),
(9,'fghj','qwerty','owner'),
(10,'admin','qwerty','owner'),
(11,'admin','wertyui','owner'),
(12,'admin','tyu','owner'),
(13,'admin','1234','owner');

/*Table structure for table `officers` */

DROP TABLE IF EXISTS `officers`;

CREATE TABLE `officers` (
  `officer_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `firstname` varchar(30) DEFAULT NULL,
  `lastname` varchar(30) DEFAULT NULL,
  `place` varchar(30) DEFAULT NULL,
  `phone` varchar(30) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`officer_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `officers` */

insert  into `officers`(`officer_id`,`login_id`,`firstname`,`lastname`,`place`,`phone`,`email`) values 
(1,2,'user','kamath','kerala','2345678907','user@gmail.com');

/*Table structure for table `position` */

DROP TABLE IF EXISTS `position`;

CREATE TABLE `position` (
  `position_id` int(11) NOT NULL AUTO_INCREMENT,
  `officer_id` int(11) DEFAULT NULL,
  `request_id` int(11) DEFAULT NULL,
  `details` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`position_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `position` */

insert  into `position`(`position_id`,`officer_id`,`request_id`,`details`) values 
(1,1,1,'HGKJGJ'),
(2,1,1,'HGKJGJ');

/*Table structure for table `request` */

DROP TABLE IF EXISTS `request`;

CREATE TABLE `request` (
  `request_id` int(11) NOT NULL AUTO_INCREMENT,
  `building_id` int(11) DEFAULT NULL,
  `description` varchar(30) DEFAULT NULL,
  `date` varchar(30) DEFAULT NULL,
  `time` varchar(30) DEFAULT NULL,
  `status` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`request_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `request` */

insert  into `request`(`request_id`,`building_id`,`description`,`date`,`time`,`status`) values 
(1,1,'descriptions..........','2022-09-14','11:05','accept');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `firstname` varchar(30) DEFAULT NULL,
  `lastname` varchar(30) DEFAULT NULL,
  `place` varchar(30) DEFAULT NULL,
  `phone` varchar(30) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`user_id`,`login_id`,`firstname`,`lastname`,`place`,`phone`,`email`) values 
(1,1,'renuka','kamath','ernakulam','1234567841','renukakamath@gmail.com'),
(2,14,'renuka','kamath','karanakodam','1234567841','staff@gamilcom'),
(3,15,'renuka','kamath','kochi','1234567841','anu@gmail.com');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
