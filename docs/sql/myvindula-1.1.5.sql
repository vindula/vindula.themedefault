
CREATE SCHEMA IF NOT EXISTS `myvindulaDB` DEFAULT CHARACTER SET latin1 ;
USE `myvindulaDB` ;

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL';

DROP TABLE `myvindulaDB`.`vin_myvindula_confgfuncdetails`;
CREATE TABLE  `myvindulaDB`.`vin_myvindula_confgfuncdetails` (
  `fields` varchar(45) NOT NULL,
  `ativo_edit` tinyint(1) DEFAULT '1',
  `ativo_view` tinyint(1) DEFAULT '1',
  `label` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`fields`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1


ALTER TABLE `myvindulaDB`.`vin_myvindula_funcdetails` CHANGE COLUMN `projetcs` `projects` VARCHAR(45) NULL DEFAULT NULL  ;

