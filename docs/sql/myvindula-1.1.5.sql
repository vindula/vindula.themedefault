
USE `myvindulaDB`;
CREATE TABLE  `myvindulaDB`.`vin_myvindula_photo_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(45) NOT NULL,
  `date_creation` datetime NOT NULL,
  `photograph` longblob,
  `thumb` longblob,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1
