-- MySQL dump 10.13  Distrib 5.5.16, for Win32 (x86)
--
-- Host: localhost    Database: libraryworld
-- ------------------------------------------------------
-- Server version	5.5.16

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
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `books` (
  `S_NO` int(11) DEFAULT NULL,
  `BOOK_Name` char(50) DEFAULT NULL,
  `BOOK_NO` char(10) DEFAULT NULL,
  `Author` char(20) DEFAULT NULL,
  `Availability` char(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES (1,'The Famous Five-Five on a Treasure Island','BN01','Enid Blyton','Yes'),(2,'The Famous Five-Five go adventuring again','BN02','Enid Blyton','No'),(3,'The Famous Five-Five Run Away Together','BN03','Enid Blyton','No'),(4,'Harry Potter and the Philosopher\'s Stone','BN04','J.K Rowling','Yes'),(5,'Harry Potter and the Chamber of Secrets','BN05','J.K Rowling','No'),(6,'Harry Potter and the Prisoner of Azkaban','BN06','J.K Rowling','No'),(7,'The Secret Seven','BN07','Enid Blyton','No'),(8,'Secret Seven Adventure','BN08','Enid Blyton','Yes'),(9,'The Chronicles of Narnia-Prince Caspian','BN09','C.S.Lewis','No'),(10,'The Chronicles of Narnia-The Last Battle','BN10','C.S.Lewis','Yes'),(11,'The Lord of the Rings-The Two Towers','BN11','J.R.R.Tolkiem','Yes'),(12,'The Lord of the Rings-The Return of the King','BN12','J.R.R.Tolkiem','Yes'),(13,'Malgudi Days','BN13','R K Narayan','Yes');
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `status`
--

DROP TABLE IF EXISTS `status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `status` (
  `S_NO` int(11) DEFAULT NULL,
  `BOOK_NO` char(10) DEFAULT NULL,
  `ID_NO` char(10) DEFAULT NULL,
  `IssueDate` char(10) DEFAULT NULL,
  `DueDate` char(10) DEFAULT NULL,
  `Status` char(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `status`
--

LOCK TABLES `status` WRITE;
/*!40000 ALTER TABLE `status` DISABLE KEYS */;
INSERT INTO `status` VALUES (1,'BN05','FN04','22-01-2021','01-02-2021','LENT'),(2,'BN02','FN02','12-2-2020','22-2-2020','LENT'),(3,NULL,'12B05',NULL,NULL,'RETURNED'),(4,'BN06','12D01','06-01-2021','16-01-2021','LENT'),(5,NULL,'12C02',NULL,NULL,'RETURNED'),(6,NULL,'FN01',NULL,NULL,'RETURNED'),(7,NULL,'12B10',NULL,NULL,'RETURNED'),(8,'BN07','12A04','26-05-2021','02-06-2021','LENT'),(9,'BN09','12A03','26-05-2021','02-06-2021','LENT'),(10,NULL,'12B09',NULL,NULL,'RETURNED'),(11,NULL,'FN03',NULL,NULL,'RETURNED'),(12,NULL,'12A01',NULL,NULL,'RETURNED'),(13,NULL,'12A02',NULL,NULL,'RETURNED');
/*!40000 ALTER TABLE `status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `S_NO` int(11) DEFAULT NULL,
  `Name` char(30) DEFAULT NULL,
  `ID_NO` char(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Aadishankar','12A01'),(2,'Ahana','12A02'),(3,'Aanandi','12A03'),(4,'Bajrang','12A04'),(5,'Chanchal','12B01'),(6,'Damodar','12B02'),(7,'Harsh','12B03'),(8,'Krishna','12B04'),(9,'Kaira','12B05'),(10,'Lakshmikanth','12B06'),(11,'Manmohan','12B07'),(12,'Narayani','12B08'),(13,'Narottam','12B09'),(14,'Radha','12B10'),(15,'Sadashiv','12C01'),(16,'Shiv','12C02'),(17,'Tanirika','12D01'),(18,'MR.Udjith','FN01'),(19,'MRS.Vaidehi','FN02'),(20,'MS.Yashvi','FN03'),(21,'MR.Yadunath','FN04');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-12-11 12:01:24
