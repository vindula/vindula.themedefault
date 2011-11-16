-- MySQL dump 10.13  Distrib 5.1.41, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: myvindulaDB
-- ------------------------------------------------------
-- Server version	5.1.41-3ubuntu12.10

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `myvindulaDB`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `myvindulaDB` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `myvindulaDB`;

--
-- Table structure for table `vin_myvindula_comments`
--

DROP TABLE IF EXISTS `vin_myvindula_comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vin_myvindula_comments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(45) NOT NULL,
  `date_creation` datetime NOT NULL,
  `type` varchar(45) DEFAULT NULL,
  `id_obj` varchar(45) DEFAULT NULL,
  `isPlone` tinyint(1) NOT NULL DEFAULT '0',
  `text` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vin_myvindula_comments`
--

LOCK TABLES `vin_myvindula_comments` WRITE;
/*!40000 ALTER TABLE `vin_myvindula_comments` DISABLE KEYS */;
INSERT INTO `vin_myvindula_comments` VALUES (2,'maumau','2011-10-28 15:27:44','ModelsMyvindulaHowareu','1',0,':boolean:boolean:boolean:boolean:boolean:boolean:boolean:boolean:boolean:boolean'),(3,'maumau','2011-10-31 10:03:51','ModelsMyvindulaHowareu','1',0,'Welcome to Vindula: MauricioWelcome to Vindula: MauricioWelcome to Vindula: MauricioWelcome to Vindula: MauricioWelcome to Vindula: MauricioWelcome to Vindula: MauricioWelcome to Vindula: MauricioWelcome to Vindula: MauricioWelcome to Vindula: Mauricio'),(5,'fabio','2011-10-31 11:29:47','ModelsMyvindulaHowareu','8',0,'Welcome to Vindula: FabioWelcome to Vindula: FabioWelcome to Vindula: FabioWelcome to Vindula: FabioWelcome to Vindula: FabioWelcome to Vindula: FabioWelcome to Vindula: FabioWelcome to Vindula: Fabio '),(6,'cesar','2011-10-31 17:36:42','ModelsMyvindulaHowareu','10',0,'Welcome to Vindula: Cesar ausgustoWelcome to Vindula: Cesar ausgustoWelcome to Vindula: Cesar ausgustoWelcome to Vindula: Cesar ausgustoWelcome to Vindula: Cesar ausgustoWelcome to Vindula: Cesar ausgusto'),(7,'fabio','2011-10-31 18:08:38','ModelsMyvindulaHowareu','4',0,'dwefdwef');
/*!40000 ALTER TABLE `vin_myvindula_comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vin_myvindula_confgfuncdetails`
--

DROP TABLE IF EXISTS `vin_myvindula_confgfuncdetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vin_myvindula_confgfuncdetails` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` tinyint(1) DEFAULT '0',
  `phone_number` tinyint(1) DEFAULT '0',
  `cell_phone` tinyint(1) DEFAULT '0',
  `email` tinyint(1) DEFAULT '0',
  `employee_id` tinyint(1) DEFAULT '0',
  `date_birth` tinyint(1) DEFAULT '0',
  `registration` tinyint(1) DEFAULT '0',
  `enterprise` tinyint(1) DEFAULT '0',
  `position` tinyint(1) DEFAULT '0',
  `admission_date` tinyint(1) DEFAULT '0',
  `cost_center` tinyint(1) DEFAULT '0',
  `job_role` tinyint(1) DEFAULT '0',
  `organisational_unit` tinyint(1) DEFAULT '0',
  `reports_to` tinyint(1) DEFAULT '0',
  `location` tinyint(1) DEFAULT '0',
  `postal_address` tinyint(1) DEFAULT '0',
  `special_roles` tinyint(1) DEFAULT '0',
  `photograph` tinyint(1) DEFAULT '0',
  `nickname` tinyint(1) DEFAULT '0',
  `pronunciation_name` tinyint(1) DEFAULT '0',
  `committess` tinyint(1) DEFAULT '0',
  `projetcs` tinyint(1) DEFAULT '0',
  `personal_information` tinyint(1) DEFAULT '0',
  `skills_expertise` tinyint(1) DEFAULT '0',
  `license_plate_numbers` tinyint(1) DEFAULT '0',
  `profit_centre` tinyint(1) DEFAULT '0',
  `languages` tinyint(1) DEFAULT '0',
  `availability` tinyint(1) DEFAULT '0',
  `papers_published` tinyint(1) DEFAULT '0',
  `teaching_research` tinyint(1) DEFAULT '0',
  `delegations` tinyint(1) DEFAULT '0',
  `resume` tinyint(1) DEFAULT '0',
  `blogs` tinyint(1) DEFAULT '0',
  `customised_message` tinyint(1) DEFAULT '0',
  `vin_myvindula_department` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vin_myvindula_confgfuncdetails`
--

LOCK TABLES `vin_myvindula_confgfuncdetails` WRITE;
/*!40000 ALTER TABLE `vin_myvindula_confgfuncdetails` DISABLE KEYS */;
INSERT INTO `vin_myvindula_confgfuncdetails` VALUES (4,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,0,1,1,1,0,0,0,1,0,1,0,0,1,0,0,1,0);
/*!40000 ALTER TABLE `vin_myvindula_confgfuncdetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vin_myvindula_courses`
--

DROP TABLE IF EXISTS `vin_myvindula_courses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vin_myvindula_courses` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(45) NOT NULL,
  `length` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vin_myvindula_courses`
--

LOCK TABLES `vin_myvindula_courses` WRITE;
/*!40000 ALTER TABLE `vin_myvindula_courses` DISABLE KEYS */;
INSERT INTO `vin_myvindula_courses` VALUES (1,'lb 07','10'),(2,'lb 01','10'),(3,'lb 74','5'),(4,'administração','10');
/*!40000 ALTER TABLE `vin_myvindula_courses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vin_myvindula_department`
--

DROP TABLE IF EXISTS `vin_myvindula_department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vin_myvindula_department` (
  `uid_plone` varchar(45) NOT NULL,
  `vin_myvindula_funcdetails_id` varchar(45) NOT NULL,
  PRIMARY KEY (`uid_plone`,`vin_myvindula_funcdetails_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vin_myvindula_department`
--

LOCK TABLES `vin_myvindula_department` WRITE;
/*!40000 ALTER TABLE `vin_myvindula_department` DISABLE KEYS */;
INSERT INTO `vin_myvindula_department` VALUES ('54544314-2d32-4ecb-85db-45fac27aaf6e','fabio'),('54544314-2d32-4ecb-85db-45fac27aaf6e','rafaela'),('7ae6b87d-a2c1-4ed0-a4ed-95314230dd21','cesar'),('7ae6b87d-a2c1-4ed0-a4ed-95314230dd21','maumau'),('7ae6b87d-a2c1-4ed0-a4ed-95314230dd21','rafaela'),('b1a83cda-ab3c-44e9-9205-a372f5257143','cesar'),('b1a83cda-ab3c-44e9-9205-a372f5257143','fabio'),('b1a83cda-ab3c-44e9-9205-a372f5257143','maumau');
/*!40000 ALTER TABLE `vin_myvindula_department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vin_myvindula_funcdetail_couses`
--

DROP TABLE IF EXISTS `vin_myvindula_funcdetail_couses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vin_myvindula_funcdetail_couses` (
  `vin_myvindula_courses_id` int(11) NOT NULL,
  `vin_myvindula_funcdetail_username` varchar(45) NOT NULL,
  PRIMARY KEY (`vin_myvindula_courses_id`,`vin_myvindula_funcdetail_username`),
  KEY `fk_vin_myvindula_funcdetail_couses_vin_myvindula_courses1` (`vin_myvindula_courses_id`),
  CONSTRAINT `fk_vin_myvindula_funcdetail_couses_vin_myvindula_courses1` FOREIGN KEY (`vin_myvindula_courses_id`) REFERENCES `vin_myvindula_courses` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vin_myvindula_funcdetail_couses`
--

LOCK TABLES `vin_myvindula_funcdetail_couses` WRITE;
/*!40000 ALTER TABLE `vin_myvindula_funcdetail_couses` DISABLE KEYS */;
INSERT INTO `vin_myvindula_funcdetail_couses` VALUES (1,'maumau'),(1,'rafaela'),(2,'cesar'),(2,'fabio'),(2,'maumau'),(3,'cesar'),(3,'fabio');
/*!40000 ALTER TABLE `vin_myvindula_funcdetail_couses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vin_myvindula_funcdetail_languages`
--

DROP TABLE IF EXISTS `vin_myvindula_funcdetail_languages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vin_myvindula_funcdetail_languages` (
  `vin_myvindula_languages_id` int(11) NOT NULL,
  `vin_myvindula_funcdetail_username` varchar(45) NOT NULL,
  PRIMARY KEY (`vin_myvindula_languages_id`,`vin_myvindula_funcdetail_username`),
  KEY `fk_vin_myvindula_funcdetail_languages_vin_myvindula_languages1` (`vin_myvindula_languages_id`),
  CONSTRAINT `fk_vin_myvindula_funcdetail_languages_vin_myvindula_languages1` FOREIGN KEY (`vin_myvindula_languages_id`) REFERENCES `vin_myvindula_languages` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vin_myvindula_funcdetail_languages`
--

LOCK TABLES `vin_myvindula_funcdetail_languages` WRITE;
/*!40000 ALTER TABLE `vin_myvindula_funcdetail_languages` DISABLE KEYS */;
INSERT INTO `vin_myvindula_funcdetail_languages` VALUES (1,'maumau'),(1,'rafaela'),(2,'cesar'),(2,'fabio'),(2,'maumau'),(3,'cesar'),(3,'fabio');
/*!40000 ALTER TABLE `vin_myvindula_funcdetail_languages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vin_myvindula_funcdetails`
--

DROP TABLE IF EXISTS `vin_myvindula_funcdetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vin_myvindula_funcdetails` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `phone_number` varchar(45) DEFAULT NULL,
  `cell_phone` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `employee_id` varchar(45) DEFAULT NULL,
  `username` varchar(45) DEFAULT NULL,
  `date_birth` date DEFAULT NULL,
  `registration` varchar(45) DEFAULT NULL,
  `position` varchar(45) DEFAULT NULL,
  `enterprise` varchar(45) DEFAULT NULL,
  `cost_center` varchar(45) DEFAULT NULL,
  `admission_date` date DEFAULT NULL,
  `job_role` varchar(45) DEFAULT NULL,
  `organisational_unit` varchar(45) DEFAULT NULL,
  `reports_to` varchar(45) DEFAULT NULL,
  `location` varchar(45) DEFAULT NULL,
  `postal_address` varchar(45) DEFAULT NULL,
  `special_roles` varchar(45) DEFAULT NULL,
  `photograph` text,
  `nickname` varchar(45) DEFAULT NULL,
  `pronunciation_name` varchar(45) DEFAULT NULL,
  `committess` varchar(45) DEFAULT NULL,
  `projetcs` varchar(45) DEFAULT NULL,
  `personal_information` varchar(45) DEFAULT NULL,
  `license_plate_numbers` varchar(45) DEFAULT NULL,
  `profit_centre` varchar(45) DEFAULT NULL,
  `availability` varchar(45) DEFAULT NULL,
  `papers_published` varchar(45) DEFAULT NULL,
  `teaching_research` varchar(45) DEFAULT NULL,
  `delegations` varchar(45) DEFAULT NULL,
  `resume` varchar(45) DEFAULT NULL,
  `blogs` varchar(45) DEFAULT NULL,
  `customised_message` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vin_myvindula_funcdetails`
--

LOCK TABLES `vin_myvindula_funcdetails` WRITE;
/*!40000 ALTER TABLE `vin_myvindula_funcdetails` DISABLE KEYS */;
INSERT INTO `vin_myvindula_funcdetails` VALUES (1,'Cesar ausgusto','123453','12356564','cesar@cesar.com','gfhghfghfhgfh','cesar','1989-11-01','123456','desenvolvimento','liberiun','desev','2011-10-27',NULL,'gfhfhhgf',NULL,'hfghgfh','r. coimbra','desev',NULL,NULL,'adsad','sadasdsa','fghfghfgh','dsadsadsd',NULL,'djakfhkajfdhkdfjkfdkj','sdfsaf','sdfsaf','sdafdf','safsdaf',NULL,'sdfsf','fhfghfxghfxhfhxfhf'),(2,'Mauricio','324598','dfsfsfdsf','mauricio@mauricio.com',NULL,'maumau','1989-11-01','45632','sadasd','liberiun','asdad','2011-10-27',NULL,NULL,NULL,'asdadas','asdasd','asdasd','Members/maumau/logo_portal-jpeg',NULL,'sdasdasd','asdasd',NULL,'sadasd',NULL,NULL,'sadsaffdfds','dsfdsf','sdfsf','sdfsfd','wqewqew','sdfsdf','ewrewrewrwreqwewqeqw'),(3,'Fabio','36528','12312456','fabio@fabio.com','23123123213131','fabio','2011-11-01','121545','12321','121613','asdsad','2011-10-27',NULL,NULL,NULL,NULL,'sadasd','asdsad',NULL,NULL,'rtytryty','rtytryr','srdfdsdf','hgfhg',NULL,'sdfsdff','gfhgfh','fghfgh','fghfgh','fghgfh',NULL,'gfhfgh','qweqweewssDDDsdsadsadDDDSA'),(4,'Rafaela Saconi','4452369','9163135','rafaela@liberiun.com','1423456','rafaela','1990-11-02','12345','dev','liberiun','desenvolvimneto','2010-01-01',NULL,'são paulo','[]','são paulo','091578','dev',NULL,'[]','rafa','fhgfgh','ghfghj','[]',NULL,'1245','12345','[]','[]','123345','[]','[]','sadasfdfdfdfdsfdsfsfddsfdsfsdf'),(5,'rafael','12345','1131787','','','rafael',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `vin_myvindula_funcdetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vin_myvindula_howareu`
--

DROP TABLE IF EXISTS `vin_myvindula_howareu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vin_myvindula_howareu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(45) NOT NULL,
  `date_creation` datetime NOT NULL,
  `visible_area` varchar(45) DEFAULT NULL,
  `text` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vin_myvindula_howareu`
--

LOCK TABLES `vin_myvindula_howareu` WRITE;
/*!40000 ALTER TABLE `vin_myvindula_howareu` DISABLE KEYS */;
INSERT INTO `vin_myvindula_howareu` VALUES (1,'maumau','2011-10-28 12:31:54','False','sdddsdad'),(3,'maumau','2011-10-28 14:29:24','False','sadasdadsad'),(4,'fabio','2011-10-31 11:20:53','False','Welcome to Vindula: FabioWelcome to Vindula: FabioWelcome to Vindula: FabioWelcome to Vindula: FabioWelcome to Vindula: FabioWelcome to Vindula: FabioWelcome to Vindula: FabioWelcome to Vindula: Fabio'),(7,'fabio','2011-10-31 11:24:58','False','Welcome to Vindula: FabioWelcome to Vindula: FabioWelcome to Vindula: FabioWelcome to Vindula: FabioWelcome to Vindula: FabioWelcome to Vindula: FabioWelcome to Vindula: FabioWelcome to Vindula: Fabio\r\n'),(8,'fabio','2011-10-31 11:27:14','False','A forma de comentar e curtir, terão seu funcionamento igual ao Facebook, e o layout deverá ser parecido em sua organização, porém, deve respeitar o default do Vindula.A forma de comentar e curtir, terão seu funcionamento igual ao Facebook, e o layout deverá ser parecido em sua organização, porém, deve respeitar o default do Vindula.'),(9,'fabio','2011-10-31 11:27:57','3','igual ao Facebook, e o layout deverá ser parecido em sua organização, porém, deve respeitar o default do Vindula.A forma de comentar e curtir, terão seu funcionamento igual ao Facebook, e o layout deverá ser parecido em sua organização, porém, deve respeitar o default do Vindula. '),(10,'cesar','2011-10-31 17:36:29','True','Welcome to Vindula: Cesar ausgustoWelcome to Vindula: Cesar ausgustoWelcome to Vindula: Cesar ausgustoWelcome to Vindula: Cesar ausgusto'),(11,'cesar','2011-11-01 16:13:31','b1a83cda-ab3c-44e9-9205-a372f5257143','In nec tortor ut est mollis elementum. Integer faucibus luctus justo nec lacinia. Donec adipiscing blandit orci, eget imperdiet eros convallis sit amet. Nam id ipsum dolor. Praesent elit ipsum, imperdiet id feugiat eu, sodales ut ligula. Maecenas hendrerit luctus nulla ac tempus. Aliquam malesuada risus turpis, blandit tincidunt dolor. Mauris venenatis nisl sed justo tincidunt eget imperdiet neque euismod. Integer vitae mattis ipsum. Sed gravida ornare enim et aliquet. Praesent magna ante, mollis in facilisis nec, mollis congue lacus. Vestibulum viverra velit sodales mauris egestas laoreet. Nunc commodo elementum ornare. Quisque a mattis nisi. Nullam at lacinia nisi. Praesent vehicula sapien non justo aliquam sodales. '),(12,'rafaela','2011-11-04 10:38:02','True','Nunc in elit lectus, eu pulvinar neque. Ut malesuada aliquam risus lobortis varius. Suspendisse potenti. Nulla faucibus fringilla faucibus. Cras tincidunt fermentum elit eget elementum. Sed accumsan metus quis leo adipiscing malesuada. Ut consequat eleifend blandit. Pellentesque feugiat tincidunt nunc pharetra volutpat. Aliquam luctus tempor tincidunt. Vivamus ut dui libero. '),(13,'rafaela','2011-11-04 10:40:58','b1a83cda-ab3c-44e9-9205-a372f5257143','fermentum sit amet magna. Integer non odio ut ante ultrices egestas eu nec arcu. Suspendisse varius, risus vel sodales ullamcorper, lorem nulla lacinia tortor, eu tristique metus massa nec ligula. Vivamus in dolor ut eros dignissim ullamcorper. ');
/*!40000 ALTER TABLE `vin_myvindula_howareu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vin_myvindula_languages`
--

DROP TABLE IF EXISTS `vin_myvindula_languages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vin_myvindula_languages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(45) NOT NULL,
  `level` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vin_myvindula_languages`
--

LOCK TABLES `vin_myvindula_languages` WRITE;
/*!40000 ALTER TABLE `vin_myvindula_languages` DISABLE KEYS */;
INSERT INTO `vin_myvindula_languages` VALUES (1,'espanhol','basico'),(2,'ingles - inter','intermediario'),(3,'ingles','basico'),(4,'espanho - inter','intermediario');
/*!40000 ALTER TABLE `vin_myvindula_languages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vin_myvindula_like`
--

DROP TABLE IF EXISTS `vin_myvindula_like`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vin_myvindula_like` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(45) NOT NULL,
  `date_creation` datetime NOT NULL,
  `type` varchar(45) DEFAULT NULL,
  `id_obj` varchar(45) DEFAULT NULL,
  `isPlone` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vin_myvindula_like`
--

LOCK TABLES `vin_myvindula_like` WRITE;
/*!40000 ALTER TABLE `vin_myvindula_like` DISABLE KEYS */;
INSERT INTO `vin_myvindula_like` VALUES (2,'cesar','2011-10-28 16:55:55','ModelsMyvindulaHowareu','1',0),(4,'fabio','2011-10-28 16:58:06','ModelsMyvindulaHowareu','3',0),(10,'maumau','2011-10-31 11:10:40','ModelsMyvindulaComments','3',0),(11,'fabio','2011-10-31 11:29:52','ModelsMyvindulaHowareu','8',0),(12,'fabio','2011-10-31 11:31:22','ModelsMyvindulaComments','5',0),(13,'cesar','2011-10-31 17:36:34','ModelsMyvindulaHowareu','10',0),(14,'fabio','2011-10-31 18:06:49','ModelsMyvindulaHowareu','4',0),(15,'cesar','2011-11-01 16:13:50','ModelsMyvindulaHowareu','11',0),(16,'rafaela','2011-11-04 11:12:06','ModelsMyvindulaHowareu','12',0);
/*!40000 ALTER TABLE `vin_myvindula_like` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vin_food_restaurant`
--

DROP TABLE IF EXISTS `vin_food_restaurant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vin_food_restaurant` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `phone_number` varchar(45) DEFAULT NULL,
  `delivery` tinyint(1) DEFAULT NULL,
  `opening_hours` varchar(45) DEFAULT NULL,
  `vin_food_specialty_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_vin_food_restaurant_vin_food_specialty1` (`vin_food_specialty_id`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vin_food_restaurant`
--

LOCK TABLES `vin_food_restaurant` WRITE;
/*!40000 ALTER TABLE `vin_food_restaurant` DISABLE KEYS */;
INSERT INTO `vin_food_restaurant` VALUES (1,'Yokamura','Av Dom Pedro II, Santo André, 123','45254785',1,'24hrs',4),(2,'teste','Av Utinga, Santo André, 124','14124412',1,'24hrs',1),(3,'Teste','Av Goias, São Caetano do Sul, 123','',1,'',2),(4,'teste','Rua das Moncoes, Santo André, 45','',0,'24hrs',1),(5,'Yotoka','Av Dom Pedro II, Santo André, 123','45254785',1,'24hrs',3),(6,'Yotoka','Av Dom Pedro II, Santo André, 123','45254785',1,'24hrs',3),(7,'Yotoka','Av Dom Pedro II, Santo André, 123','45254785',1,'24hrs',3),(8,'Yotoka','Av Dom Pedro II, Santo André, 123','45254785',1,'24hrs',3),(9,'Yotoka','Av Dom Pedro II, Santo André, 123','45254785',1,'24hrs',3),(10,'Yotoka','Av Dom Pedro II, Santo André, 123','45254785',1,'24hrs',3),(11,'Two Options','Rua das Paineiras, Santo André, SP, 12','14124412',0,'12 - 15',5);
/*!40000 ALTER TABLE `vin_food_restaurant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vin_food_specialty`
--

DROP TABLE IF EXISTS `vin_food_specialty`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vin_food_specialty` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vin_food_specialty`
--

LOCK TABLES `vin_food_specialty` WRITE;
/*!40000 ALTER TABLE `vin_food_specialty` DISABLE KEYS */;
INSERT INTO `vin_food_specialty` VALUES (1,'Brasileira'),(2,'Italiana'),(3,'Chinesa'),(4,'Japonesa'),(5,'Arroz e Feijão'),(6,'Francesa'),(7,'Teste'),(8,'Lanches'),(9,'Frango'),(10,'Picanha'),(11,'Costela'),(12,'Londrina'),(13,'Frutos do mar');
/*!40000 ALTER TABLE `vin_food_specialty` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2011-11-04 11:15:43
