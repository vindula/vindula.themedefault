/*
MyVindula Change - 1.1.6
*/
use myvindulaDB;
ALTER TABLE vin_myvindula_comments add ip VARCHAR(45) NOT NULL;

ALTER TABLE vin_myvindula_funcdetails CHANGE COLUMN `projetcs` `projects` VARCHAR(45) NULL DEFAULT NULL ;

