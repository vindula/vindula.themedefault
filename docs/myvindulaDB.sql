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
  `has_agreement` tinyint(1) DEFAULT NULL,
  `agreement` varchar(45) DEFAULT NULL,
  `vin_food_specialty_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_vin_food_restaurant_vin_food_specialty1` (`vin_food_specialty_id`),
  CONSTRAINT `fk_vin_food_restaurant_vin_food_specialty1` FOREIGN KEY (`vin_food_specialty_id`) REFERENCES `vin_food_specialty` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

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
  `profit_centre` varchar(45) DEFAULT NULL,
  `availability` varchar(45) DEFAULT NULL,
  `papers_published` varchar(45) DEFAULT NULL,
  `teaching_research` varchar(45) DEFAULT NULL,
  `delegations` varchar(45) DEFAULT NULL,
  `resume` varchar(45) DEFAULT NULL,
  `blogs` varchar(45) DEFAULT NULL,
  `customised_message` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

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
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `vin_myvindula_recados`
--

DROP TABLE IF EXISTS `vin_myvindula_recados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vin_myvindula_recados` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(45) NOT NULL,
  `date_creation` datetime NOT NULL,
  `destination` varchar(45) NOT NULL,
  `text` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2011-11-30 10:53:41
