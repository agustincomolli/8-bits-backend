-- MySQL dump 10.13  Distrib 8.0.35, for Win64 (x86_64)
--
-- Host: viaduct.proxy.rlwy.net    Database: 8-bits
-- ------------------------------------------------------
-- Server version	8.2.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `plan_details`
--

DROP TABLE IF EXISTS `plan_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `plan_details` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'Primary Key',
  `id_plan` int NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Detalles de planes';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `plan_details`
--

/*!40000 ALTER TABLE `plan_details` DISABLE KEYS */;
INSERT INTO `plan_details` VALUES (1,1,'Tarifa mínima que incluye 1 hora de trabajo para el diagnóstico y solución de problemas.'),(2,1,'Asesoramiento técnico'),(3,2,'Actualizaciónes de software'),(4,2,'Limpieza de malware'),(5,2,'Limpieza del Sistema Operativo'),(6,2,'Limpieza física del CPU'),(7,2,'Copia de seguridad de datos sensibles'),(8,2,'Asistencia remota y en sitio'),(9,3,'Incluye todo lo del plan Profesional'),(10,3,'Formateo e instalación del Sistema Operativo'),(11,3,'Instalación de software básico'),(12,3,'Instalación y configuración del software específico'),(13,3,'Prioridad en la atención al cliente');
/*!40000 ALTER TABLE `plan_details` ENABLE KEYS */;

--
-- Table structure for table `plans`
--

DROP TABLE IF EXISTS `plans`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `plans` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'Primary Key',
  `name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `price` decimal(10,2) NOT NULL DEFAULT '0.00',
  `subscription_time` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT 'Por hora / Mensual',
  `description` varchar(255) DEFAULT NULL,
  `valid_time` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT 'Válido por...',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Planes de mantenimiento';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `plans`
--

/*!40000 ALTER TABLE `plans` DISABLE KEYS */;
INSERT INTO `plans` VALUES (1,'Base',5000.00,'Por hora','Ideal para los que necesitan un arreglo ocacional',NULL),(2,'Profesional',10000.00,'Mensual','Para los que quieren un soporte técnico regular.','Válido por 3 meses'),(3,'Premium',12000.00,'Mensual','Ideal para los que quieren un soporte full all time','Válido por 3 meses');
/*!40000 ALTER TABLE `plans` ENABLE KEYS */;

--
-- Table structure for table `services`
--

DROP TABLE IF EXISTS `services`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `services` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `services`
--

/*!40000 ALTER TABLE `services` DISABLE KEYS */;
INSERT INTO `services` VALUES (1,'Diagnóstico y Resolución de Fallas','Nuestros expertos identificarán y resolverán de manera eficiente cualquier problema en tu equipo, manteniendo tus sistemas en pleno funcionamiento.'),(2,'Instalación de Sistemas Operativos','Deja que 8-bits se encargue de la instalación de sistemas operativos, asegurando que todo esté configurado y listo para funcionar sin problemas.'),(3,'Eliminación de Malware','Mantén tu sistema libre de amenazas con nuestra eliminación de virus y spyware, protegiendo tus datos y tu privacidad.'),(4,'Actualización de Sistema','Mantén tu software actualizado y seguro con nuestras actualizaciones de sistema regulares, garantizando un rendimiento óptimo.'),(5,'Limpieza Física de los Equipos','Una limpieza física regular ayuda a prolongar la vida útil de tus equipos y a mantenerlos funcionando sin problemas.'),(6,'Instalación de Hardware','Añade o reemplaza componentes de hardware con confianza, gracias a nuestros servicios de instalación de hardware.'),(7,'Instalación y Configuración de Software','Desde software empresarial hasta programas personalizados, te asistimos en la instalación y configuración para satisfacer tus necesidades específicas.'),(8,'Networking','Mantén una conectividad sin interrupciones con nuestros servicios de chequeo, instalación y reparación de cableado de red y datos.'),(9,'Instalación y Reparación de Sistemas Operativos','Ya sea Windows, Mac o Linux, nuestros expertos pueden instalar y reparar sistemas operativos para garantizar un rendimiento óptimo.'),(10,'Configuración y Mantenimiento de Servidores','Asegura un flujo constante de datos y servicios con nuestra configuración y mantenimiento de servidores experto.'),(11,'Instalación de Antivirus y Programas de Seguridad','Protege tus sistemas con nuestra experiencia en la instalación, actualización y mantenimiento de antivirus y programas de seguridad.'),(12,'Gestión de Redes y Sistemas','Mantén tus redes y sistemas bajo control con nuestra gestión experta, garantizando una operación sin problemas.'),(13,'Reparación de Computadoras y Notebooks','Solucionamos problemas de hardware y software en tus computadoras y notebooks, devolviéndote equipos en perfectas condiciones de funcionamiento.'),(14,'Backups de los Datos de tu Empresa','Protege tus datos cruciales con nuestros servicios de copia de seguridad, asegurando que nunca se pierda información valiosa.'),(15,'Asesoramiento y Consultoría','Obtén orientación experta en tecnología y toma decisiones informadas para tu empresa con nuestro servicio de asesoramiento y consultoría.'),(16,'Asesoramiento en Software Legal y Licenciamiento','Cumple con las regulaciones y adquiere el software legal necesario con nuestra orientación en software legal y licenciamiento.'),(17,'Soporte Remoto','Obtén asistencia inmediata sin importar tu ubicación con nuestro soporte remoto a través de RustDesk, AnyDesk o Team Viewer. Nuestros expertos están a un clic de distancia.'),(19,'Servicio de Prueba 2','lo cambie');
/*!40000 ALTER TABLE `services` ENABLE KEYS */;

--
-- Dumping routines for database '8-bits'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-07 13:57:58
