SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL';

CREATE SCHEMA IF NOT EXISTS `myvindulaDB` DEFAULT CHARACTER SET latin1 ;
USE `myvindulaDB` ;

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
-- Dumping data for table `vin_myvindula_confgfuncdetails`
--

LOCK TABLES `vin_myvindula_confgfuncdetails` WRITE;
/*!40000 ALTER TABLE `vin_myvindula_confgfuncdetails` DISABLE KEYS */;
INSERT INTO `vin_myvindula_confgfuncdetails` VALUES (1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1);
/*!40000 ALTER TABLE `vin_myvindula_confgfuncdetails` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2011-12-23 10:31:07
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
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vin_myvindula_funcdetails`
--

LOCK TABLES `vin_myvindula_funcdetails` WRITE;
/*!40000 ALTER TABLE `vin_myvindula_funcdetails` DISABLE KEYS */;
INSERT INTO `vin_myvindula_funcdetails` VALUES (1,'Mariah Carey','(11) 9998-8455','(11) 5717-1689','mariahcarey@vindula.com.br','19156624867','mariahcarey','1970-03-27','18647361512','Diretor de RH','Vindula Tecnologia Ltda.','RH - teste','2011-11-24','Administrativo','Rihanna','4º andar','78968000','Assistente Social','Members/mariahcarey/mariah_carey-jpg','Mariah Carey','Mariah Carey','Administrativo','Vindula','CPF: 287.712.126-71','RH','Horário Comercial','10 artigos','You Don','Precious (2009)','Tennessee (2009)','www.mariahcarey.com','Mariah Angela Carey é uma cantora Pop e R&B, compositora, atriz e produtora musical americana. Ela fez sua primeira gravação em 1990, sob a orientação do executivo da Columbia Records Tommy Mottola, e se tornou a primeira artista a ter 5 singles de estreia no Top 5 da Billboard Hot 100. Após seu casamento com Mottola, em 1993, lança uma série de sucessos, incluindo \"Dreamlover\", \"Hero\", \"Without You\", \"Fantasy\", \"One Sweet Day\" e \"Always Be My Baby\" a partir de álbuns como Music Box e Daydream e o natalino \"All I Want For Christmas Is You\", do \"Merry Christmas\", álbum natalino mais vendido de todos os tempos, estabeleceram sua posição como a artista da Columbia Records que mais vende discos.'),(2,'U2','(11) 4452-1920','(11) 9883-1245','u2@vindula.com.br','64614703950','U2','1976-09-25','05348681504','Editor','Vindula Tecnologia Ltda.','Administrativo','2011-11-24','Administrativo','Iron Maiden','4º andar','98176-686','Cantor','Members/U2/u2-jpg','U2 banda','u2','Administrativo','Vindula','CPF: 287.712.126-71','Administrativo','Horário Comercial','10 artigos','All That You Can','No Line on the Horizon (2009)','How to Dismantle an Atomic Bomb (2004)','www.u2.com','U2 é uma banda de rock formada em Dublin, Irlanda no ano de 1976. O grupo é composto por Bono (vocalista e guitarrista), The Edge (guitarrista, pianista e backing vocal); Adam Clayton (baixista); Larry Mullen Jr. (baterista e percussionista).'),(3,'Iron Maiden','(11) 2828-7576','(11) 9978-7474','ironmaiden@vindula.com.br','20511330','ironmaiden','1975-12-22','13780671697','Comprador','Vindula Tecnologia Ltda.','Compras','2011-11-25','Administrativo','Rihanna','3ª andar','78994-800','Programador','Members/ironmaiden/ironmaiden-jpeg','Iron Maiden','Iron Maiden','Administrativo','Vindula','CPF: 227.762.122-67','Compras','Horário Comercial','5','2006 - A Matter of Life and Death Tour','2010-2011 - The Final Frontier World Tour','2008 - Somewhere Back in Time World Tour','www.ironmanbrazil.com','Iron Maiden é uma banda britânica de heavy metal, formada em 1975 pelo baixista Steve Harris, ex-integrante das bandas Gypsy\'s Kiss e Smiler. Originária de Londres, foi uma das principais bandas do movimento musical que ficou conhecido como NWOBHM (New Wave of British Heavy Metal). O nome \"Iron Maiden\" (\"donzela de ferro\"), homônimo de um instrumento de tortura medieval que aparece no filme O Homem da Máscara de Ferro, baseado na obra de Alexandre Dumas.'),(4,'Coldplay','(11) 2808-4404','(11) 9991-9991','coldplay@vindula.com.br','68778532701','coldplay','1996-12-25','45477261161','Analista de Sistemas','Vindula Tecnologia Ltda.','TI','2011-10-25','TI','Adele','1º andra','78956-000','Analista de Help Desk','Members/coldplay/coldplay-jpg','Coldplay','Coldplay','Tecnologico','Vindula','CPF: 636.151.237-19','TI','24 / 7','10','X&Y (2004)','Mylo Xyloto (2009)','Viva la Vida or Death and All His Friends (20','www.coldplay.com','Coldplay é uma banda britânica de rock alternativo fundada em 1996 na Inglaterra pelo vocalista principal Chris Martin e o guitarrista Jonny Buckland no University College London. Depois de formar o Pectoralz, Guy Berryman se juntou ao grupo como baixista e eles mudaram o nome para Starfish. Will Champion entrou para tocar bateria, como vocal de apoio e multi-instrumentista, completando assim, o grupo. O empresário Phil Harvey é muitas vezes considerado o quinto membro não oficial. A banda passou a se chamar \"Coldplay\" em 1998, antes de gravar e lançar três EPs; Safety em 1998, \"Brothers & Sisters\" como um single em 1999 e The Blue Room no mesmo ano. Este último foi o primeiro lançamento da banda por uma grande gravadora, depois de assinar contrato com a Parlophone.'),(5,'Maroon 5','(11) 2886-6017','(11) 9991-2642','maroon5@vindula.com.br','85383686134','maroon5','1998-04-20','25626719539','Coordenador de TI','Vindula Tecnologia Ltda.','TI','2011-06-01','TI','U2','1º andra','20511-170','Líder de Equipe','Members/Maroon5/maroon5-jpg','Maroon 5','Maroon Five','Tecnologico','Vindula','CPF: 385.347.637-63','TI','24 / 7','10','Live from SoHo (EP Exclusive iTunes) (2008)','Call and Response: The Remix Album (2008)','The B-Side Collection (2007)','www.maroon5.com','Maroon 5 é uma banda de rock alternativo dos Estados Unidos, com influências do pop, soul, funk e R&B.\r\n\r\nÉ formada por Adam Levine (vocal, guitarra) James Valentine (guitarra) Jesse Carmichael (teclados) Mickey Madden (baixo) Matt Flynn (bateria).'),(6,'Beyoncé','(11) 5721-6660','(11) 9936-2688','beyonce@vindula.com.br','61334417989','beyonce','1981-09-04','81318346894','Vendedora','Vindula Tecnologia Ltda.','Vendas','2011-11-10','Faturamento','Adele','4º andar','20511-330','Analista de Vendas','Members/beyonce/cantores-beyonce-7ea9c5-jpg','Beyoncé','Beyoncé','Faturamento','Vindula','CPF: 748.879.863-51','Vendas','Horário Comercial','1','2004–05: Destiny Fulfilled','Live At Roseland','Dangerously in Love','www.beyonceonline.com','Beyoncé Giselle Knowles (Houston, 4 de Setembro de 1981), mais conhecida simplesmente como Beyoncé, é uma cantora, compositora, atriz, dançarina, coreógrafa, arranjadora vocal, produtora, diretora de vídeo e empresária americana nascida e criada em Houston, no Texas. Cantora desde a infância, Beyoncé se tornou conhecida no ano de 1997, como vocalista do grupo feminino de R&B Destiny\'s Child, que mundialmente já vendeu mais de 50 milhões de discos.'),(7,'Katy Perry','(11) 5758-6157','(11) 9936-3608','katyperry@vindula.com.br','50318017601','katyperry','1984-10-25','88687667957','Técnico de Informática','Vindula Tecnologia Ltda.','TI','2001-01-01','TI','Adele','1º andra','78993-000','Analista de Help Desk','Members/katyperry/katy_perry_blog-jpg','Katy Perry','Katy Perry','Tecnologico','Vindula','CPF: 838.747.832-60','TI','Horário Comercial','3','2001 - Katy Hudson','2010 - Teenage Dream','2008 - One of the Boys','www.katyperry.com.br','Katy Perry (nome artístico de Katheryn Elizabeth Hudson, Santa Bárbara, 25 de outubro de 1984) é uma cantora e compositora estadunidense de música pop e dance.'),(8,'Rihanna','(11) 5701-2004','(11) 9978-3217','rihanna@vindula.com.br','19321785701','rihanna','1988-02-20','46643292883','Supervisor de Vendas','Vindula Tecnologia Ltda.','Vendas','2011-02-01','Faturamento','Adele','3ª andar','20511170','Vendedor','Members/rihanna/rihanna-jpg','Rihanna','Rihanna','Faturamento','Vindula','CPF: 213.082.276-20','Vendas','Horário Comercial','3','2006: A Girl Like Me','2008: Good Girl Gone Bad: Reloaded/Live','2007–2009: Good Girl Gone Bad','www.rihannanow.com','Robyn Rihanna Fenty, conhecida pelo seu nome artístico, Rihanna (Saint Michael, 20 de Fevereiro de 1988) é uma cantora de Barbados, de ascendência barbadiana, guianense e irlandesa. Assinou contrato com a editora Def Jam Recordings após uma audição, que assimilou o interesse do produtor Evan Rogers e do vice-presidente na altura da editora, Jay-Z, na jovem artista.'),(9,'Adele silva','(11) 2888-7731','(11) 9978-1006','adele@vindula.com.br','75277119221','adele','1988-12-19','62185536206','Gerente Geral','Vindula Tecnologia Ltda.','Administrativo','2011-01-01','Administrativo','Avril Lavigne','4º andar','13092-150','Secretária de Diretoria','Members/adele/adele-jpg','Adele','Adele','Administrativo','Vindula','CPF: 247.493.526-67','Administrativo','Horário Comercial','10','An Evening with Adele(2008-2009)','Adele Live (2011)','Adele Live (2011)','http://adele.tv','Adele Laurie Blue Adkins (Enfield, 5 de maio de 1988), conhecida pelo nome artístico Adele é uma cantora e compositora britânica. Ela foi a primeira a receber o prêmio Critics\' Choice do BRIT Awards e foi nomeada \"artista revelação\" em 2008 pelos críticos da BBC. Em 2009, Adele ganhou dois Grammy Awards de \"Artista Revelação\" e \"Melhor Vocal Pop Feminino\". Teve seu reconhecimento mundial ao lançar o álbum 21 e dominar as paradas de sucesso nos Estados Unidos e Reino Unido com o single \"Rolling In The Deep.'),(10,'Avril Lavigne','(11) 2008-8420','(11) 9978-6660','avrillavigne@vindula.com.br','58731564844','avrillavigne','1984-09-27','65862259813','Gerente','Vindula Tecnologia Ltda.','Administrativo','2001-01-01','Administrativo','Adele','3ª andar','20530-350','Secretária de Diretoria','Members/avrillavigne/200px-avril_lavigne_cropped2-jpg','Avril Lavigne','Avril Lavigne','Administrativo','Vindula','CPF: 251.154.617-57','Administrativo','Horário Comercial','1','2007–2008: The Best Damn Thing','2010: Goodbye Lullaby e saída da RCA','The Best Damn Tour - Live in Toronto','www.avrillavigne.com','Avril Ramona Lavigne (Belleville, 27 de setembro de 1984) é uma cantora, compositora, designer de moda, atriz e filantropa canadense. A mídia e alguns críticos a denominam como Princesa do Pop Punk. Iniciou sua carreira musical ao assinar contrato em dezembro de 2001, após uma apresentação feita pela cantora em uma feira e exposição de gado, quando despertou o interesse do produtor L. A. Reid, que trabalhava na já extinta Arista Records. Em meados de 2009, os seus então três álbuns de estúdio, Let Go, Under My Skin e The Best Damn Thing, já haviam vendido juntos mais de 30 milhões de cópias e 18 milhões de singles em todo o mundo, além de mais de 500 mil álbuns e 700 mil downloads pagos somente no Brasil, sendo uma das recordistas de vendas digitais no país, de acordo com a ABPD. Lavigne também é uma das jovens mais ricas do mundo, segundo a lista da revista Forbes, com uma renda de mais de 12 milhões de dólares por ano.'),(11,'FATIMA APARECIDA NETTO SILVA','122548',NULL,'eu@fabiorizzo.com.br',NULL,'fatimasilva114341','1989-06-09','114341','OPERADOR DE CAIXA','MEGA PAULISTA -teste','OPERADOR DE CAIXA','2011-06-09',NULL,NULL,NULL,NULL,NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `vin_myvindula_funcdetails` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2011-12-23 10:31:07
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
INSERT INTO `vin_myvindula_funcdetail_languages` VALUES (1,'coldplay'),(1,'katyperry'),(1,'mariahcarey'),(1,'Maroon5'),(1,'U2'),(2,'adele'),(2,'avrillavigne'),(2,'cesaraugusto'),(2,'U2'),(3,'beyonce'),(3,'cesaraugusto'),(3,'ironmaiden'),(3,'mariahcarey'),(3,'Maroon5'),(3,'rihanna'),(4,'ironmaiden'),(5,'avrillavigne'),(5,'coldplay'),(5,'U2'),(7,'beyonce');
/*!40000 ALTER TABLE `vin_myvindula_funcdetail_languages` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2011-12-23 10:31:07
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
-- Dumping data for table `vin_myvindula_languages`
--

LOCK TABLES `vin_myvindula_languages` WRITE;
/*!40000 ALTER TABLE `vin_myvindula_languages` DISABLE KEYS */;
INSERT INTO `vin_myvindula_languages` VALUES (1,'Inglês','Básico'),(2,'Inglês','Avançado'),(3,'Espanhol','Básico'),(4,'Espanhol','Avançado'),(5,'Alemão','Básico'),(6,'Japonês','Básico'),(7,'Frances','Básico'),(8,'Italiano','Básico');
/*!40000 ALTER TABLE `vin_myvindula_languages` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2011-12-23 10:31:07
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
) ENGINE=InnoDB AUTO_INCREMENT=76 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vin_myvindula_comments`
--

LOCK TABLES `vin_myvindula_comments` WRITE;
/*!40000 ALTER TABLE `vin_myvindula_comments` DISABLE KEYS */;
INSERT INTO `vin_myvindula_comments` VALUES (1,'avrillavigne','2011-11-25 13:56:41','vindula.content.content.vindulanews','8e34e64f-ab42-449d-9ab5-31baa00010e7',1,'Interessante , grande avanço tecnológico!!'),(11,'coldplay','2011-11-29 15:55:47','ModelsMyvindulaHowareu','22',0,'Nossa que legal!'),(12,'coldplay','2011-11-29 16:30:11','vindula.content.content.vindulanews','42674ce6-36cc-4f07-b349-67816318c8e8',1,'Que noticia legal!'),(13,'coldplay','2011-11-29 16:30:50','ModelsMyvindulaComments','12',1,'Estamos respondendo'),(14,'coldplay','2011-11-29 16:40:01','ModelsMyvindulaHowareu','21',0,'esa. Empresa, aqui significa o empreendimento, os esforços humanos organizados, feitos em comum, com um fim específico, um objetivo. As instituições (empresas) podem ser públicas, sociedades de economia mista ou privadas, com ou sem fins lucrativos.'),(15,'coldplay','2011-11-29 16:43:09','ModelsMyvindulaHowareu','24',0,'s da organização. Apesar da disseminação em tempos recentes dos cursos de gestão de pessoas, tal prática ainda é confundida com uma atividade restrita ao setor de recursos humanos. Neste âmbito, as habilidades humanas assumem importância capital para qualquer gestor. O principal modelo de gestão de pessoas atualmente é a Gestão por Competências.'),(16,'beyonce','2011-11-29 16:56:19','ModelsMyvindulaHowareu','21',0,'A administração, também chamada gerenciamento ou gestão de empresas, supõe a existência de uma instituição a ser administrada ou gerida, ou seja, uma Entidade Social de pessoas e recursos que se relacionem num determinado ambiente, físico o'),(17,'beyonce','2011-11-29 17:02:03','ModelsMyvindulaHowareu','21',0,'A administração, também chamada gerenciamento ou gestão de empreA administração, também chamada gerenciamento ou gestão de empre'),(21,'beyonce','2011-11-29 17:43:15','ModelsMyvindulaHowareu','3',0,'Somente os extremamente sábios e os extremamente estúpidos é que não mudam. '),(23,'coldplay','2011-11-30 09:43:36','ModelsMyvindulaHowareu','4',0,'Todo homem é poeta quando está apaixonado. '),(24,'beyonce','2011-11-30 10:25:46','ModelsMyvindulaHowareu','28',0,'beyoncebeyoncebeyoncebeyoncebeyoncebeyonce'),(25,'admin','2011-11-30 10:46:08','ModelsMyvindulaComments','5',1,'teste'),(27,'coldplay','2011-11-30 11:31:59','ModelsMyvindulaHowareu','30',0,'al modelo de gestão de pess'),(28,'coldplay','2011-11-30 11:34:43','ModelsMyvindulaRecados','30',0,'ModelsMyvindulaHowareuModelsMyvindulaHowareuModelsMyvindulaHowareu'),(29,'U2','2011-11-30 11:37:16','ModelsMyvindulaRecados','32',0,'Não corrigir nossas falhas é o mesmo que cometer novos erros. '),(30,'adele','2011-11-30 16:20:59','ModelsMyvindulaHowareu','2',0,'safsdf'),(31,'adele','2011-11-30 16:27:24','ModelsMyvindulaHowareu','26',0,'dsfdsf'),(32,'adele','2011-11-30 16:27:30','ModelsMyvindulaHowareu','26',0,'sdfsdf'),(33,'adele','2011-11-30 16:37:09','ModelsMyvindulaHowareu','27',0,'legal!'),(34,'mariahcarey','2011-11-30 16:37:21','ModelsMyvindulaHowareu','27',0,'tambem acho'),(35,'adele','2011-11-30 17:02:28','ModelsMyvindulaHowareu','20',0,'Teste'),(36,'adele','2011-11-30 17:04:53','ModelsMyvindulaComments','1',1,'teste'),(37,'adele','2011-11-30 17:34:54','vindula.content.content.vindulanews','8e34e64f-ab42-449d-9ab5-31baa00010e7',1,'teste'),(38,'adele','2011-11-30 17:42:29','ModelsMyvindulaComments','1',1,'asdasdasd'),(39,'adele','2011-11-30 17:43:52','ModelsMyvindulaRecados','45',0,'asdasda'),(40,'adele','2011-11-30 17:49:04','ModelsMyvindulaHowareu','27',0,'ultimo'),(41,'adele','2011-11-30 17:52:36','ModelsMyvindulaRecados','50',0,'sadasda'),(42,'adele','2011-11-30 17:53:33','ModelsMyvindulaRecados','50',0,'sadasda'),(43,'mariahcarey','2011-11-30 17:53:55','ModelsMyvindulaRecados','53',0,'COMENTARIO DO RECADO'),(44,'mariahcarey','2011-11-30 17:54:18','ModelsMyvindulaRecados','53',0,'COMENTARIO DO REcado.'),(45,'coldplay','2011-12-01 09:41:15','ModelsMyvindulaRecados','31',0,'principal modelo de gestão de pessoas atualmente é a Gestão por Competências. '),(46,'coldplay','2011-12-01 09:54:16','ModelsMyvindulaRecados','31',0,'dasdadsdasd'),(47,'coldplay','2011-12-01 11:05:37','ModelsMyvindulaHowareu','12',0,'A experiência é uma lanterna dependurada nas costas que apenas ilumina o caminho já percorrido. '),(48,'coldplay','2011-12-01 11:09:55','ModelsMyvindulaHowareu','12',0,'experiência é uma lanterna dependurada nas costas que apexperiência é uma lanterna dependurada nas costas que ap'),(49,'admin','2011-12-01 11:16:03','vindula.content.content.vindulanews','5424479c-b1f9-4ecb-98e3-d1a7a92eb769',1,'cia de uma série de fatores excepcionais, incluindo o casamento do príncipe William.'),(50,'coldplay','2011-12-01 11:16:31','vindula.content.content.vindulanews','8e34e64f-ab42-449d-9ab5-31baa00010e7',1,'o baseado em silício que poderia provar ser um componente instrumental na construção de redes totalmente ópticas e de baixo custo no futuro. Como o aparelho do MIT, essa tecnologia lembra a de um transistor, capaz de permitir que a luz se mova em uma direção enquanto bloqueia qualquer movimento de luz na direção oposta (o princípio da computação, 0 e 1).'),(51,'coldplay','2011-12-01 11:16:43','ModelsMyvindulaComments','37',1,'o baseado em silício que poderia provar ser um componente instrumental na construção de redes totalmente ópticas e de baixo custo no futuro.'),(52,'adele','2011-12-01 11:34:09','ModelsMyvindulaHowareu','5',0,'teste'),(53,'adele','2011-12-01 16:57:34','ModelsMyvindulaHowareu','10',0,'sdasda'),(54,'adele','2011-12-01 16:57:41','ModelsMyvindulaHowareu','9',0,'zdssfs'),(55,'adele','2011-12-01 16:58:40','ModelsMyvindulaHowareu','10',0,'teste'),(56,'adele','2011-12-01 17:03:10','ModelsMyvindulaRecados','40',0,'asdasda'),(57,'adele','2011-12-02 09:39:23','ModelsMyvindulaRecados','54',0,'ddgfdg'),(58,'adele','2011-12-02 09:54:28','ModelsMyvindulaHowareu','16',0,'teste'),(59,'adele','2011-12-02 09:54:35','ModelsMyvindulaHowareu','15',0,'teste 2'),(60,'adele','2011-12-02 10:37:40','vindula.content.content.vindulanews','9bce3e19-e493-47bf-9db1-d0710d02df5e',1,'teste'),(61,'adele','2011-12-02 10:38:52','vindula.content.content.vindulanews','9bce3e19-e493-47bf-9db1-d0710d02df5e',1,''),(62,'adele','2011-12-02 10:39:57','vindula.content.content.vindulanews','9bce3e19-e493-47bf-9db1-d0710d02df5e',1,''),(63,'adele','2011-12-02 10:39:57','vindula.content.content.vindulanews','9bce3e19-e493-47bf-9db1-d0710d02df5e',1,''),(64,'adele','2011-12-02 10:51:06','ModelsMyvindulaComments','60',1,'dsfsdfs'),(65,'adele','2011-12-02 11:05:11','ModelsMyvindulaRecados','65',0,'Deixe um recado para U2: Deixe um recado para U2: '),(66,'adele','2011-12-02 11:06:35','ModelsMyvindulaRecados','63',0,'dsfsdfsd'),(67,'adele','2011-12-02 11:08:16','ModelsMyvindulaRecados','54',0,'asdasda'),(68,'adele','2011-12-02 11:08:24','ModelsMyvindulaRecados','54',0,'tttttttttttttttt'),(69,'adele','2011-12-02 11:08:26','ModelsMyvindulaRecados','64',0,'scrapsscrapsscrapsscraps'),(70,'adele','2011-12-02 11:08:55','ModelsMyvindulaHowareu','4',0,'scrapsscraps'),(71,'adele','2011-12-02 11:09:40','ModelsMyvindulaHowareu','16',0,'dsfsdf'),(72,'adele','2011-12-02 11:10:11','ModelsMyvindulaRecados','66',0,'rsfrst'),(73,'adele','2011-12-02 11:11:11','ModelsMyvindulaRecados','66',0,'teste do comentario'),(74,'coldplay','2011-12-02 11:46:41','ModelsMyvindulaHowareu','10',0,'m a morte? A vida tem tantos problemas que temos de res'),(75,'coldplay','2011-12-02 11:53:45','ModelsMyvindulaHowareu','12',0,'ada nas costas que apenasada nas costas que apenasada nas costas que apenasada nas costas que apenas');
/*!40000 ALTER TABLE `vin_myvindula_comments` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2011-12-23 10:31:07
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
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vin_myvindula_recados`
--

LOCK TABLES `vin_myvindula_recados` WRITE;
/*!40000 ALTER TABLE `vin_myvindula_recados` DISABLE KEYS */;
INSERT INTO `vin_myvindula_recados` VALUES (30,'beyonce','2011-11-30 10:43:40','','apital para qualquer gestor. O principal modelo de gestão de pessoas atualmente é a Gestão por Competências. '),(31,'beyonce','2011-11-30 10:48:38','','pital para qualquer gestor. O principal modelo de gestão de pessoas atualmente é a Gestão por Competências. '),(32,'coldplay','2011-11-30 10:58:16','','Somente os extremamente sábios e os extremamente estúpidos é que não mudam. '),(33,'adele','2011-11-30 15:42:16','','Teste do recado'),(34,'adele','2011-11-30 15:42:27','','asdasdas'),(35,'adele','2011-11-30 15:45:39','','asdasdas'),(36,'adele','2011-11-30 15:46:17','','asdasdas'),(37,'adele','2011-11-30 15:47:23','','asdasdas'),(38,'adele','2011-11-30 15:49:37','','asdasdas'),(39,'adele','2011-11-30 15:50:11','','asdasdas'),(40,'adele','2011-11-30 15:50:27','','asdasdas'),(41,'adele','2011-11-30 15:52:12','','Primeiro recado'),(42,'adele','2011-11-30 16:20:39','','TESTE'),(43,'adele','2011-11-30 16:39:13','','teste'),(44,'adele','2011-11-30 16:43:59','','teste'),(45,'adele','2011-11-30 16:44:38','','teste'),(46,'adele','2011-11-30 16:47:31','','Primeiro recado teste'),(47,'adele','2011-11-30 16:48:29','','Primeiro recado teste'),(48,'adele','2011-11-30 16:48:53','','Primeiro recado teste'),(49,'adele','2011-11-30 16:51:28','','segundo recado\r\n'),(50,'adele','2011-11-30 16:52:38','','tttttttttttttt'),(51,'adele','2011-11-30 17:46:40','','ULTIMO'),(52,'adele','2011-11-30 17:48:51','','ULTIMO'),(53,'mariahcarey','2011-11-30 17:50:59','','Primeiro recado para Adele.'),(54,'mariahcarey','2011-11-30 17:56:56','','Novo recado ora voce'),(55,'coldplay','2011-12-01 09:55:37','','Deixe um recado para Beyoncé:'),(56,'coldplay','2011-12-01 10:06:31','','dfsfdfsfdsfdsfdsfsdf'),(57,'coldplay','2011-12-01 10:46:01','','sdadadaddasdfgffggg'),(59,'coldplay','2011-12-01 10:48:46','','sdadadaddasdfgffggg'),(60,'coldplay','2011-12-01 10:57:44','','	04/09/1981'),(61,'coldplay','2011-12-01 11:05:45','','A experiência é uma lanterna dependurada nas costas que apenas ilumina o caminho já percorrido. '),(62,'coldplay','2011-12-01 11:09:46','','experiência é uma lanterna dependurada nas costas que ap'),(63,'admin','2011-12-02 09:34:17','','teste'),(65,'adele','2011-12-02 11:04:57','','Deixe um recado para U2:'),(66,'adele','2011-12-02 11:09:46','','ssfsdf'),(67,'adele','2011-12-02 11:26:43','','sdagfdgfgdfgfgfgfgdfgd'),(69,'coldplay','2011-12-02 11:44:14','','hjgjghjhgjgjgh'),(71,'coldplay','2011-12-02 11:52:35','','amente sábios e os extremamente estúpidos é que não mudam. '),(72,'coldplay','2011-12-02 11:53:52','','ada nas costas que apenasada nas costas que apenasada nas costas que apenas');
/*!40000 ALTER TABLE `vin_myvindula_recados` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2011-12-23 10:31:07
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
INSERT INTO `vin_myvindula_department` VALUES ('56045db9-d381-4548-9c57-435ea95d453b','coldplay'),('56045db9-d381-4548-9c57-435ea95d453b','ironmaiden'),('56045db9-d381-4548-9c57-435ea95d453b','katyperry'),('56045db9-d381-4548-9c57-435ea95d453b','Maroon5'),('b9e3eb8f-0fce-4dba-a257-63ed0d5001b8','beyonce'),('b9e3eb8f-0fce-4dba-a257-63ed0d5001b8','rihanna'),('b9e3eb8f-0fce-4dba-a257-63ed0d5001b8','U2'),('d5c47705-6844-4b97-884b-eef24475a731','avrillavigne'),('d5c47705-6844-4b97-884b-eef24475a731','cesaraugusto'),('d5c47705-6844-4b97-884b-eef24475a731','ironmaiden'),('d5c47705-6844-4b97-884b-eef24475a731','U2'),('fbfa842d-c98b-41ae-a97a-2fb04e7f7249','adele'),('fbfa842d-c98b-41ae-a97a-2fb04e7f7249','mariahcarey');
/*!40000 ALTER TABLE `vin_myvindula_department` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2011-12-23 10:31:07
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
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vin_myvindula_like`
--

LOCK TABLES `vin_myvindula_like` WRITE;
/*!40000 ALTER TABLE `vin_myvindula_like` DISABLE KEYS */;
INSERT INTO `vin_myvindula_like` VALUES (3,'admin','2011-11-29 14:23:20','ModelsMyvindulaComments','5',0),(4,'coldplay','2011-11-29 15:00:40','ModelsMyvindulaHowareu','1',0),(5,'coldplay','2011-11-29 15:25:18','ModelsMyvindulaHowareu','3',0),(6,'coldplay','2011-11-29 16:31:01','ModelsMyvindulaComments','12',0),(7,'beyonce','2011-11-29 16:40:21','ModelsMyvindulaHowareu','21',0),(8,'beyonce','2011-11-29 17:03:05','ModelsMyvindulaComments','17',0),(9,'coldplay','2011-11-30 10:24:39','ModelsMyvindulaHowareu','28',0),(11,'admin','2011-11-30 10:46:18','ModelsMyvindulaComments','6',0),(14,'adele','2011-11-30 17:02:19','ModelsMyvindulaHowareu','20',0),(15,'coldplay','2011-12-01 11:14:05','ModelsMyvindulaRecados','62',0),(16,'adele','2011-12-01 11:37:00','ModelsMyvindulaComments','29',0),(17,'adele','2011-12-01 11:37:02','ModelsMyvindulaComments','29',0),(18,'adele','2011-12-01 16:23:46','ModelsMyvindulaHowareu','17',0),(19,'adele','2011-12-02 10:27:44','ModelsMyvindulaComments','58',0),(20,'adele','2011-12-02 10:49:22','ModelsMyvindulaComments','60',0),(21,'adele','2011-12-02 10:50:52','ModelsMyvindulaComments','61',0),(22,'coldplay','2011-12-02 11:54:54','ModelsMyvindulaRecados','66',0),(23,'coldplay','2011-12-02 12:32:47','ModelsMyvindulaHowareu','14',0),(24,'coldplay','2011-12-02 12:32:47','ModelsMyvindulaHowareu','14',0);
/*!40000 ALTER TABLE `vin_myvindula_like` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2011-12-23 10:31:07
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
-- Dumping data for table `vin_myvindula_courses`
--

LOCK TABLES `vin_myvindula_courses` WRITE;
/*!40000 ALTER TABLE `vin_myvindula_courses` DISABLE KEYS */;
INSERT INTO `vin_myvindula_courses` VALUES (1,'Informática','10 horas'),(2,'Secretariado','20 Horas'),(3,'Marketing','20 horas'),(4,'Logística','30 Horas'),(5,'Gestão de empresas','10 horas'),(6,'Design','10 horas'),(7,'Administração','20 Horas');
/*!40000 ALTER TABLE `vin_myvindula_courses` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2011-12-23 10:31:07
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
INSERT INTO `vin_myvindula_funcdetail_couses` VALUES (1,'coldplay'),(1,'katyperry'),(1,'mariahcarey'),(1,'Maroon5'),(1,'U2'),(2,'adele'),(2,'avrillavigne'),(2,'U2'),(3,'beyonce'),(3,'ironmaiden'),(3,'mariahcarey'),(3,'Maroon5'),(3,'rihanna'),(4,'ironmaiden'),(5,'avrillavigne'),(5,'coldplay'),(5,'U2'),(7,'beyonce');
/*!40000 ALTER TABLE `vin_myvindula_funcdetail_couses` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2011-12-23 10:31:07
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
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vin_myvindula_howareu`
--

LOCK TABLES `vin_myvindula_howareu` WRITE;
/*!40000 ALTER TABLE `vin_myvindula_howareu` DISABLE KEYS */;
INSERT INTO `vin_myvindula_howareu` VALUES (1,'mariahcarey','2011-11-29 11:28:27','True','Eu não procuro saber as respostas, procuro compreender as perguntas.'),(2,'mariahcarey','2011-11-29 11:28:36','True','É fazendo que se aprende a fazer aquilo que se deve aprender a fazer.'),(3,'U2','2011-11-29 11:29:08','True','Somente os extremamente sábios e os extremamente estúpidos é que não mudam.'),(4,'U2','2011-11-29 11:29:21','True','Todo homem é poeta quando está apaixonado.'),(5,'ironmaiden','2011-11-29 11:29:49','True','Querem que vos ensine o modo de chegar à ciência verdadeira? Aquilo que se sabe, saber que se sabe; aquilo que não se sabe, saber que não se sabe; na verdade é este o saber.'),(6,'ironmaiden','2011-11-29 11:30:03','True','Não corrigir nossas falhas é o mesmo que cometer novos erros.'),(7,'coldplay','2011-11-29 11:30:48','True','A dúvida é o principio da sabedoria.'),(8,'coldplay','2011-11-29 11:30:55','True','Se queres prever o futuro, estuda o passado.'),(9,'maroon5','2011-11-29 11:31:53','True','Eu não procuro saber as respostas, procuro compreender as perguntas.'),(10,'maroon5','2011-11-29 11:31:58','True','Para quê preocuparmo-nos com a morte? A vida tem tantos problemas que temos de resolver primeiro.'),(11,'beyonce','2011-11-29 11:33:34','True','A humildade é a única base sólida de todas as virtudes.'),(12,'beyonce','2011-11-29 11:33:38','True','A experiência é uma lanterna dependurada nas costas que apenas ilumina o caminho já percorrido.'),(13,'katyperry','2011-11-29 11:34:04','True','É fazendo que se aprende a fazer aquilo que se deve aprender a fazer.'),(14,'katyperry','2011-11-29 11:34:23','True','Somente os extremamente sábios e os extremamente estúpidos é que não mudam.'),(15,'rihanna','2011-11-29 11:34:56','True','O mestre disse: Quem se modera, raramente se perde.'),(16,'rihanna','2011-11-29 11:35:05','True','Aprender sem pensar é tempo perdido.'),(17,'adele','2011-11-29 11:35:34','True','Entre amigos as frequentes censuras afastam a amizade.'),(18,'adele','2011-11-29 11:35:41','True','Não corrigir nossas falhas é o mesmo que cometer novos erros.'),(19,'avrillavigne','2011-11-29 11:36:13','True','Uma vida não questionada não merece ser vivida.'),(20,'avrillavigne','2011-11-29 11:36:21','True','O segredo da criatividade é saber como esconder as fontes.\r\n'),(21,'adele','2011-11-29 15:28:27','d5c47705-6844-4b97-884b-eef24475a731','Meu novo pensamento...'),(22,'adele','2011-11-29 15:53:40','True','Estamos em uma reunião!'),(23,'adele','2011-11-29 15:55:56','True','Estamos em uma reunião!'),(24,'coldplay','2011-11-29 16:13:17','fbfa842d-c98b-41ae-a97a-2fb04e7f7249','O que você está pensando agora?\r\n'),(25,'adele','2011-11-30 16:26:36','True','teste'),(26,'adele','2011-11-30 16:27:09','True','Bla Bla Bla'),(27,'mariahcarey','2011-11-30 16:36:40','True','Ultimo pensamento');
/*!40000 ALTER TABLE `vin_myvindula_howareu` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2011-12-23 10:31:07
