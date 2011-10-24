SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL';

CREATE SCHEMA IF NOT EXISTS `myvindulaDB` DEFAULT CHARACTER SET latin1 ;
USE `myvindulaDB` ;

-- -----------------------------------------------------
-- Table `myvindulaDB`.`Department`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `myvindulaDB`.`Department` ;

CREATE  TABLE IF NOT EXISTS `myvindulaDB`.`Department` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `name` VARCHAR(45) NOT NULL ,
  `description` VARCHAR(45) NULL ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `myvindulaDB`.`FuncDetails`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `myvindulaDB`.`FuncDetails` ;

CREATE  TABLE IF NOT EXISTS `myvindulaDB`.`FuncDetails` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `name` VARCHAR(45) NULL ,
  `phone_number` VARCHAR(45) NULL ,
  `email` VARCHAR(45) NULL ,
  `employee_id` VARCHAR(45) NULL ,
  `username` VARCHAR(45) NULL ,
  `date_birth` DATE NULL ,
  `registration` VARCHAR(45) NULL ,
  `enterprise` VARCHAR(45) NULL ,
  `position` VARCHAR(45) NULL ,
  `admission_date` DATE NULL ,
  `cost_center` VARCHAR(45) NULL ,
  `job_role` VARCHAR(45) NULL ,
  `organisational_unit` VARCHAR(45) NULL ,
  `reports_to` VARCHAR(45) NULL ,
  `location` VARCHAR(45) NULL ,
  `postal_address` VARCHAR(45) NULL ,
  `special_roles` VARCHAR(45) NULL ,
  `photograph` TEXT NULL ,
  `nickname` VARCHAR(45) NULL ,
  `pronunciation_name` VARCHAR(45) NULL ,
  `committess` VARCHAR(45) NULL ,
  `projetcs` VARCHAR(45) NULL ,
  `personal_information` VARCHAR(45) NULL ,
  `skills_expertise` VARCHAR(45) NULL ,
  `license_plate_numbers` VARCHAR(45) NULL ,
  `profit_centre` VARCHAR(45) NULL ,
  `languages` VARCHAR(45) NULL ,
  `availability` VARCHAR(45) NULL ,
  `papers_published` VARCHAR(45) NULL ,
  `teaching_research` VARCHAR(45) NULL ,
  `delegations` VARCHAR(45) NULL ,
  `resume` VARCHAR(45) NULL ,
  `blogs` VARCHAR(45) NULL ,
  `customised_message` TEXT NULL ,
  `Department_id` INT NOT NULL ,
  PRIMARY KEY (`id`) ,
  INDEX `fk_FuncDetails_Department` (`Department_id` ASC) ,
  CONSTRAINT `fk_FuncDetails_Department`
    FOREIGN KEY (`Department_id` )
    REFERENCES `myvindulaDB`.`Department` (`id` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `myvindulaDB`.`ConfMyvindula`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `myvindulaDB`.`ConfMyvindula` ;

CREATE  TABLE IF NOT EXISTS `myvindulaDB`.`ConfMyvindula` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `name` TINYINT(1)  NULL DEFAULT FALSE ,
  `phone_number` TINYINT(1)  NULL DEFAULT FALSE ,
  `email` TINYINT(1)  NULL DEFAULT FALSE ,
  `employee_id` TINYINT(1)  NULL DEFAULT FALSE ,
  `username` TINYINT(1)  NULL DEFAULT FALSE ,
  `date_birth` TINYINT(1)  NULL DEFAULT FALSE ,
  `registration` TINYINT(1)  NULL DEFAULT FALSE ,
  `enterprise` TINYINT(1)  NULL DEFAULT FALSE ,
  `position` TINYINT(1)  NULL DEFAULT FALSE ,
  `admission_date` TINYINT(1)  NULL DEFAULT FALSE ,
  `cost_center` TINYINT(1)  NULL DEFAULT FALSE ,
  `job_role` TINYINT(1)  NULL DEFAULT FALSE ,
  `organisational_unit` TINYINT(1)  NULL DEFAULT FALSE ,
  `reports_to` TINYINT(1)  NULL DEFAULT FALSE ,
  `location` TINYINT(1)  NULL DEFAULT FALSE ,
  `postal_address` TINYINT(1)  NULL DEFAULT FALSE ,
  `special_roles` TINYINT(1)  NULL DEFAULT FALSE ,
  `photograph` TINYINT(1)  NULL DEFAULT FALSE ,
  `nickname` TINYINT(1)  NULL DEFAULT FALSE ,
  `pronunciation_name` TINYINT(1)  NULL DEFAULT FALSE ,
  `committess` TINYINT(1)  NULL DEFAULT FALSE ,
  `projetcs` TINYINT(1)  NULL DEFAULT FALSE ,
  `personal_information` TINYINT(1)  NULL DEFAULT FALSE ,
  `skills_expertise` TINYINT(1)  NULL DEFAULT FALSE ,
  `license_plate_numbers` TINYINT(1)  NULL DEFAULT FALSE ,
  `profit_centre` TINYINT(1)  NULL DEFAULT FALSE ,
  `languages` TINYINT(1)  NULL DEFAULT FALSE ,
  `availability` TINYINT(1)  NULL DEFAULT FALSE ,
  `papers_published` TINYINT(1)  NULL DEFAULT FALSE ,
  `teaching_research` TINYINT(1)  NULL DEFAULT FALSE ,
  `delegations` TINYINT(1)  NULL DEFAULT FALSE ,
  `resume` TINYINT(1)  NULL DEFAULT FALSE ,
  `blogs` TINYINT(1)  NULL DEFAULT FALSE ,
  `customised_message` TINYINT(1)  NULL DEFAULT FALSE ,
  `Department_id` TINYINT(1)  NULL DEFAULT FALSE ,
  PRIMARY KEY (`id`) )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;



SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
