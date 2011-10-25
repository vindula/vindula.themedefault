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
-- Table structure for table `ConfMyvindula`
--

DROP TABLE IF EXISTS `ConfMyvindula`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ConfMyvindula` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` tinyint(1) DEFAULT '0',
  `phone_number` tinyint(1) DEFAULT '0',
  `email` tinyint(1) DEFAULT '0',
  `employee_id` tinyint(1) DEFAULT '0',
  `username` tinyint(1) DEFAULT '0',
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
  `Department_id` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ConfMyvindula`
--

LOCK TABLES `ConfMyvindula` WRITE;
/*!40000 ALTER TABLE `ConfMyvindula` DISABLE KEYS */;
INSERT INTO `ConfMyvindula` VALUES (3,1,1,1,0,0,1,0,1,1,1,1,1,0,0,0,1,1,1,0,1,1,0,1,1,0,0,1,1,1,1,0,1,1,0,1);
/*!40000 ALTER TABLE `ConfMyvindula` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Department`
--

DROP TABLE IF EXISTS `Department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Department` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `description` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Department`
--

LOCK TABLES `Department` WRITE;
/*!40000 ALTER TABLE `Department` DISABLE KEYS */;
INSERT INTO `Department` VALUES (1,'logistica','logistica'),(2,'administrativo','adminsitrativo'),(3,'financeiro','financeiro');
/*!40000 ALTER TABLE `Department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `FuncDetails`
--

DROP TABLE IF EXISTS `FuncDetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `FuncDetails` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `phone_number` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `employee_id` varchar(45) DEFAULT NULL,
  `username` varchar(45) DEFAULT NULL,
  `date_birth` date DEFAULT NULL,
  `registration` varchar(45) DEFAULT NULL,
  `enterprise` varchar(45) DEFAULT NULL,
  `position` varchar(45) DEFAULT NULL,
  `admission_date` date DEFAULT NULL,
  `cost_center` varchar(45) DEFAULT NULL,
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
  `skills_expertise` varchar(45) DEFAULT NULL,
  `license_plate_numbers` varchar(45) DEFAULT NULL,
  `profit_centre` varchar(45) DEFAULT NULL,
  `languages` varchar(45) DEFAULT NULL,
  `availability` varchar(45) DEFAULT NULL,
  `papers_published` varchar(45) DEFAULT NULL,
  `teaching_research` varchar(45) DEFAULT NULL,
  `delegations` varchar(45) DEFAULT NULL,
  `resume` varchar(45) DEFAULT NULL,
  `blogs` varchar(45) DEFAULT NULL,
  `customised_message` text,
  `Department_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_FuncDetails_Department` (`Department_id`),
  CONSTRAINT `fk_FuncDetails_Department` FOREIGN KEY (`Department_id`) REFERENCES `Department` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `FuncDetails`
--

LOCK TABLES `FuncDetails` WRITE;
/*!40000 ALTER TABLE `FuncDetails` DISABLE KEYS */;
INSERT INTO `FuncDetails` VALUES (1,'admin','44532112','teste@teste.com','124578','admin','2010-02-12','333223','saraiva','sdfsdffdsf','2011-02-12','desenvolvimneto','sdfdsf','hgjghhgj','jose','ghjghj','av dom pedro','Nonesfsdfdsf',NULL,'admin','wrewr','wrwe','saraiva','sdfsfsdsdsd','hjgjghj','sfdfds','dfsfsdsdsd','tyytutyu','10','dsfsdd','tyytu','tyutyuty','sdffdsf','hgjghjh','tyutyuyt',2),(2,'mauricio souza','11453222','maumau@teste.com','124578','maumau','1989-10-25','sdf3223',NULL,'sdfsfdsf','2011-10-18','dev','dddd',NULL,'asdd','centro','av dom pedro',NULL,NULL,'maumau',NULL,'ssdfsf','sariva','100',NULL,'333234','102','sdfdsfdsf','dfsdsd','10',NULL,'andre','tess','teste','sdfsffwerrewree',1),(3,'teste teste','123456','teste@cesar.com','123456','teste','1990-11-25','asdad','sfds','fsdffsfd','2011-10-18','dsfsfds','hhjhghj','dasdadasd','asdsad','sadasd','testete','sdfsf',NULL,'sdfsf','sdfsfdfd','ghjgjggj','fgdg','sfsdf','asdd','asdad','werwe','asdasd','asdasd','teste','asdsad','asdad','tdgdgdhg','sdadas','dsfsfs',1),(4,'cesar augusto','45352922','cesar@teste.com','12345','cesar','2010-10-18','234455','liberiunteste','devenvolvedor','2011-10-18','dev','teste222','sdad','testetgdgg','r coimbra','teste rua','teste',NULL,'cesra','dfffgdfgfdg','tetdghg','teste','testefffff','testte','2133654','cesar','portugues','testetdt','testearq','testetdgdg','testdgg','teste tetste','sdadsfd','testetdggdhdffdssdfdsdsdssdfds',1),(5,'jeferson ramal','45352922','jefferosn@teste.com','12345','jefferosn','2000-10-18','234455','liberiunteste','devenvolvedor','2011-10-18','dev','teste222','sdad','testetgdgg','jefferson','testerua','teste',NULL,'cesra','dfffgdfgfdg','tetdghg','teste','testefffff','testte','2133654','cesar','portugues','testetdt','testearq','testetdgdg','testdgg','teste tetste','sdadsfd','jeff jeff',2),(6,'denis pimenta','45352922','denis@teste.com','12345','denis','2001-10-18','234455','liberiunteste','devenvolvedor','2011-10-18','dev','teste222','sdad','testetgdgg','denis','teste rua','teste',NULL,'cesra','dfffgdfgfdg','tetdghg','teste','testefffff','testte','2133654','cesar','portugues','testetdt','testearq','testetdgdg','testdgg','teste tetste','sdadsfd','denis denis denis',1),(7,'rafaela saconni','45352922','rafaela@teste.com','12345','rafaela','1980-11-03','234455','liberiunteste','devenvolvedor','2011-10-18','dev','teste222','sdad','testetgdgg','so Paulo','teste rua','teste',NULL,'cesra','dfffgdfgfdg','tetdghg','teste','testefffff','testte','2133654','cesar','portugues','testetdt','testearq','testetdgdg','testdgg','teste tetste','sdadsfd','rafela rafela',1),(8,'fabio rizzo','45352922','fabio@teste.com','12345','fabio','1980-11-28','234455','liberiunteste','devenvolvedor','2011-10-18','dev','teste222','sdad','testetgdgg','santo andre sp','teste rua','teste',NULL,'cesra','dfffgdfgfdg','tetdghg','teste','testefffff','testte','2133654','fabio','portugues','testetdt','testearq','testetdgdg','testdgg','teste tetste','sdadsfd','fabio fabio',1),(9,'rodrigo reis','45352922','rodigo@teste.com','12345','rodrigo','2000-10-28','234455','liberiunteste','devenvolvedor','2011-10-18','dev','teste222','sdad','testetgdgg','rodrigo','teste rua','teste',NULL,'rodigo','dfffgdfgfdg','tetdghg','teste','testefffff','testte','2133654','cesar','portugues','testetdt','testearq','testetdgdg','testdgg','teste tetste','sdadsfd','rodrigo rodigo rodrigo',1),(10,'jose dilva',NULL,'jose@jose.com',NULL,'jose','2000-11-26',NULL,NULL,NULL,'2011-10-15','fdgfdgg',NULL,'fdgfdgfdg','fgdfgfdg','jose','rua jose',NULL,NULL,'jose','hggh','fghfghfgh','fghfghfg','gfhfgh','gfhgfh','fghgfh','fghfgh','fghfgh','hfgh','gfhgfh','gfhfgh','ghfgh','jose jose','gfhgfhf','jose jose jose jose',2),(11,'deni 2','112225','tesdenis@teste.com','213213','denidenis','2000-11-26',NULL,'liberiun','asdsad','2011-10-20','sdad',NULL,'sdad','sdasdds','sdasdsd',NULL,'sdadsd',NULL,'deni 2',NULL,NULL,NULL,'asdsa',NULL,NULL,NULL,NULL,'asdsad',NULL,NULL,NULL,'asdsad','sadasd','asdad',1);
/*!40000 ALTER TABLE `FuncDetails` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2011-10-25 15:19:49
