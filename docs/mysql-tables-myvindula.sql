SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL';

CREATE SCHEMA IF NOT EXISTS `myvindulaDB` DEFAULT CHARACTER SET latin1 ;
USE `myvindulaDB` ;

-- -----------------------------------------------------
-- Table `myvindulaDB`.`vin_myvindula_comments`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `myvindulaDB`.`vin_myvindula_comments` ;

CREATE  TABLE IF NOT EXISTS `myvindulaDB`.`vin_myvindula_comments` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `username` VARCHAR(45) NOT NULL ,
  `date_creation` DATETIME NOT NULL ,
  `type` VARCHAR(45) NULL DEFAULT NULL ,
  `id_obj` VARCHAR(45) NULL DEFAULT NULL ,
  `isPlone` TINYINT(1) NOT NULL DEFAULT '0' ,
  `text` TEXT NULL DEFAULT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
AUTO_INCREMENT = 25
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `myvindulaDB`.`vin_myvindula_confgfuncdetails`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `myvindulaDB`.`vin_myvindula_confgfuncdetails` ;

CREATE  TABLE IF NOT EXISTS `myvindulaDB`.`vin_myvindula_confgfuncdetails` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `name` TINYINT(1) NULL DEFAULT '0' ,
  `phone_number` TINYINT(1) NULL DEFAULT '0' ,
  `cell_phone` TINYINT(1) NULL DEFAULT '0' ,
  `email` TINYINT(1) NULL DEFAULT '0' ,
  `employee_id` TINYINT(1) NULL DEFAULT '0' ,
  `date_birth` TINYINT(1) NULL DEFAULT '0' ,
  `registration` TINYINT(1) NULL DEFAULT '0' ,
  `enterprise` TINYINT(1) NULL DEFAULT '0' ,
  `position` TINYINT(1) NULL DEFAULT '0' ,
  `admission_date` TINYINT(1) NULL DEFAULT '0' ,
  `cost_center` TINYINT(1) NULL DEFAULT '0' ,
  `job_role` TINYINT(1) NULL DEFAULT '0' ,
  `organisational_unit` TINYINT(1) NULL DEFAULT '0' ,
  `reports_to` TINYINT(1) NULL DEFAULT '0' ,
  `location` TINYINT(1) NULL DEFAULT '0' ,
  `postal_address` TINYINT(1) NULL DEFAULT '0' ,
  `special_roles` TINYINT(1) NULL DEFAULT '0' ,
  `photograph` TINYINT(1) NULL DEFAULT '0' ,
  `nickname` TINYINT(1) NULL DEFAULT '0' ,
  `pronunciation_name` TINYINT(1) NULL DEFAULT '0' ,
  `committess` TINYINT(1) NULL DEFAULT '0' ,
  `projetcs` TINYINT(1) NULL DEFAULT '0' ,
  `personal_information` TINYINT(1) NULL DEFAULT '0' ,
  `skills_expertise` TINYINT(1) NULL DEFAULT '0' ,
  `license_plate_numbers` TINYINT(1) NULL DEFAULT '0' ,
  `profit_centre` TINYINT(1) NULL DEFAULT '0' ,
  `languages` TINYINT(1) NULL DEFAULT '0' ,
  `availability` TINYINT(1) NULL DEFAULT '0' ,
  `papers_published` TINYINT(1) NULL DEFAULT '0' ,
  `teaching_research` TINYINT(1) NULL DEFAULT '0' ,
  `delegations` TINYINT(1) NULL DEFAULT '0' ,
  `resume` TINYINT(1) NULL DEFAULT '0' ,
  `blogs` TINYINT(1) NULL DEFAULT '0' ,
  `customised_message` TINYINT(1) NULL DEFAULT '0' ,
  `vin_myvindula_department` TINYINT(1) NULL DEFAULT '0' ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `myvindulaDB`.`vin_myvindula_courses`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `myvindulaDB`.`vin_myvindula_courses` ;

CREATE  TABLE IF NOT EXISTS `myvindulaDB`.`vin_myvindula_courses` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `title` VARCHAR(45) NOT NULL ,
  `length` VARCHAR(45) NULL DEFAULT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
AUTO_INCREMENT = 8
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `myvindulaDB`.`vin_myvindula_department`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `myvindulaDB`.`vin_myvindula_department` ;

CREATE  TABLE IF NOT EXISTS `myvindulaDB`.`vin_myvindula_department` (
  `uid_plone` VARCHAR(45) NOT NULL ,
  `vin_myvindula_funcdetails_id` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`uid_plone`, `vin_myvindula_funcdetails_id`) )
ENGINE = MyISAM
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `myvindulaDB`.`vin_myvindula_funcdetail_couses`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `myvindulaDB`.`vin_myvindula_funcdetail_couses` ;

CREATE  TABLE IF NOT EXISTS `myvindulaDB`.`vin_myvindula_funcdetail_couses` (
  `vin_myvindula_courses_id` INT(11) NOT NULL ,
  `vin_myvindula_funcdetail_username` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`vin_myvindula_courses_id`, `vin_myvindula_funcdetail_username`) ,
  INDEX `fk_vin_myvindula_funcdetail_couses_vin_myvindula_courses1` (`vin_myvindula_courses_id` ASC) ,
  CONSTRAINT `fk_vin_myvindula_funcdetail_couses_vin_myvindula_courses1`
    FOREIGN KEY (`vin_myvindula_courses_id` )
    REFERENCES `myvindulaDB`.`vin_myvindula_courses` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `myvindulaDB`.`vin_myvindula_languages`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `myvindulaDB`.`vin_myvindula_languages` ;

CREATE  TABLE IF NOT EXISTS `myvindulaDB`.`vin_myvindula_languages` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `title` VARCHAR(45) NOT NULL ,
  `level` VARCHAR(45) NULL DEFAULT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
AUTO_INCREMENT = 9
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `myvindulaDB`.`vin_myvindula_funcdetail_languages`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `myvindulaDB`.`vin_myvindula_funcdetail_languages` ;

CREATE  TABLE IF NOT EXISTS `myvindulaDB`.`vin_myvindula_funcdetail_languages` (
  `vin_myvindula_languages_id` INT(11) NOT NULL ,
  `vin_myvindula_funcdetail_username` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`vin_myvindula_languages_id`, `vin_myvindula_funcdetail_username`) ,
  INDEX `fk_vin_myvindula_funcdetail_languages_vin_myvindula_languages1` (`vin_myvindula_languages_id` ASC) ,
  CONSTRAINT `fk_vin_myvindula_funcdetail_languages_vin_myvindula_languages1`
    FOREIGN KEY (`vin_myvindula_languages_id` )
    REFERENCES `myvindulaDB`.`vin_myvindula_languages` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `myvindulaDB`.`vin_myvindula_funcdetails`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `myvindulaDB`.`vin_myvindula_funcdetails` ;

CREATE  TABLE IF NOT EXISTS `myvindulaDB`.`vin_myvindula_funcdetails` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `name` VARCHAR(45) NULL DEFAULT NULL ,
  `phone_number` VARCHAR(45) NULL DEFAULT NULL ,
  `cell_phone` VARCHAR(45) NULL DEFAULT NULL ,
  `email` VARCHAR(45) NULL DEFAULT NULL ,
  `employee_id` VARCHAR(45) NULL DEFAULT NULL ,
  `username` VARCHAR(45) NULL DEFAULT NULL ,
  `date_birth` DATE NULL DEFAULT NULL ,
  `registration` VARCHAR(45) NULL DEFAULT NULL ,
  `position` VARCHAR(45) NULL DEFAULT NULL ,
  `enterprise` VARCHAR(45) NULL DEFAULT NULL ,
  `cost_center` VARCHAR(45) NULL DEFAULT NULL ,
  `admission_date` DATE NULL DEFAULT NULL ,
  `organisational_unit` VARCHAR(45) NULL DEFAULT NULL ,
  `reports_to` VARCHAR(45) NULL DEFAULT NULL ,
  `location` VARCHAR(45) NULL DEFAULT NULL ,
  `postal_address` VARCHAR(45) NULL DEFAULT NULL ,
  `special_roles` VARCHAR(45) NULL DEFAULT NULL ,
  `photograph` TEXT NULL DEFAULT NULL ,
  `nickname` VARCHAR(45) NULL DEFAULT NULL ,
  `pronunciation_name` VARCHAR(45) NULL DEFAULT NULL ,
  `committess` VARCHAR(45) NULL DEFAULT NULL ,
  `projetcs` VARCHAR(45) NULL DEFAULT NULL ,
  `personal_information` VARCHAR(45) NULL DEFAULT NULL ,
  `profit_centre` VARCHAR(45) NULL DEFAULT NULL ,
  `availability` VARCHAR(45) NULL DEFAULT NULL ,
  `papers_published` VARCHAR(45) NULL DEFAULT NULL ,
  `teaching_research` VARCHAR(45) NULL DEFAULT NULL ,
  `delegations` VARCHAR(45) NULL DEFAULT NULL ,
  `resume` VARCHAR(45) NULL DEFAULT NULL ,
  `blogs` VARCHAR(45) NULL DEFAULT NULL ,
  `customised_message` TEXT NULL DEFAULT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
AUTO_INCREMENT = 11
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `myvindulaDB`.`vin_myvindula_howareu`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `myvindulaDB`.`vin_myvindula_howareu` ;

CREATE  TABLE IF NOT EXISTS `myvindulaDB`.`vin_myvindula_howareu` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `username` VARCHAR(45) NOT NULL ,
  `date_creation` DATETIME NOT NULL ,
  `visible_area` VARCHAR(45) NULL DEFAULT NULL ,
  `text` TEXT NULL DEFAULT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
AUTO_INCREMENT = 30
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `myvindulaDB`.`vin_myvindula_like`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `myvindulaDB`.`vin_myvindula_like` ;

CREATE  TABLE IF NOT EXISTS `myvindulaDB`.`vin_myvindula_like` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `username` VARCHAR(45) NOT NULL ,
  `date_creation` DATETIME NOT NULL ,
  `type` VARCHAR(45) NULL DEFAULT NULL ,
  `id_obj` VARCHAR(45) NULL DEFAULT NULL ,
  `isPlone` TINYINT(1) NOT NULL DEFAULT '0' ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
AUTO_INCREMENT = 11
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `myvindulaDB`.`vin_myvindula_recados`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `myvindulaDB`.`vin_myvindula_recados` ;

CREATE  TABLE IF NOT EXISTS `myvindulaDB`.`vin_myvindula_recados` (
  `id` INT(11) NOT NULL AUTO_INCREMENT ,
  `username` VARCHAR(45) NOT NULL ,
  `date_creation` DATETIME NOT NULL ,
  `destination` VARCHAR(45) NOT NULL ,
  `text` TEXT NULL DEFAULT NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
AUTO_INCREMENT = 30
DEFAULT CHARACTER SET = latin1;



SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
