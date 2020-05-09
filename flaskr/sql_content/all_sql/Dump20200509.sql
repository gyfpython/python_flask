CREATE DATABASE  IF NOT EXISTS `flask` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `flask`;
-- MySQL dump 10.13  Distrib 5.7.29, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: flask
-- ------------------------------------------------------
-- Server version	5.7.29-0ubuntu0.16.04.1

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
-- Table structure for table `catalogs`
--

DROP TABLE IF EXISTS `catalogs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `catalogs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `catalogName` varchar(45) NOT NULL COMMENT 'all catalogs of notes',
  `catalogNumber` int(11) NOT NULL,
  `createTime` datetime NOT NULL DEFAULT '1970-01-01 00:00:00',
  `createBy` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `catalogName_UNIQUE` (`catalogName`),
  UNIQUE KEY `catalogNumber_UNIQUE` (`catalogNumber`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `catalogs`
--

LOCK TABLES `catalogs` WRITE;
/*!40000 ALTER TABLE `catalogs` DISABLE KEYS */;
INSERT INTO `catalogs` VALUES (1,'test',0,'1970-01-01 00:00:00','admin'),(2,'mysql',1,'1970-01-01 00:00:00','admin'),(3,'python',2,'1970-01-01 00:00:00','admin'),(4,'performance',3,'1970-01-01 00:00:00','admin'),(5,'security',4,'1970-01-01 00:00:00','admin');
/*!40000 ALTER TABLE `catalogs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `entries`
--

DROP TABLE IF EXISTS `entries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `entries` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `title` varchar(100) NOT NULL DEFAULT '' COMMENT 'Unique ID for clients.',
  `text` varchar(512) DEFAULT NULL,
  `createTime` datetime NOT NULL DEFAULT '1970-01-01 00:00:00',
  `updateBy` varchar(100) NOT NULL DEFAULT '',
  `Catalogs` int(11) NOT NULL DEFAULT '0' COMMENT '0:测试;1:mysql;2:python...',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `entries`
--

LOCK TABLES `entries` WRITE;
/*!40000 ALTER TABLE `entries` DISABLE KEYS */;
INSERT INTO `entries` VALUES (20,'测试用例设计包含哪些？','1.用例编号\r\n2.story编号\r\n3.优先级\r\n4.前置条件\r\n5.执行步骤\r\n6.预期结果\r\n7.实际结果\r\n8.用例名称\r\n9.测试数据\r\n10.用例分类\r\n11.测试环境\r\n12.设计人\r\n13.通过与否','1970-01-01 00:00:00','test',0),(21,'测试用例设计方法','1.等价类划分\r\n2.边界值划分\r\n3.因果图\r\n4.正交排列\r\n5.错误推测方法','1970-01-01 00:00:00','test',0),(22,'软件测试包含哪些方面','功能测试、性能测试、压力测试、负载测试、代码健壮性、可靠性、安全性、可用性、易用性、异常测试、场景测试','2020-05-05 01:31:58','admin',0),(23,'测试金字塔','e2e测试、组件测试、API测试、单元测试','1970-01-01 00:00:00','test',0),(24,'TDD','Test Driven development:敏捷开发基本思想\r\n单元测试用例首先完成，增加开发效率以及正针对性，但是又增加了代码量，测试代码是开发代码的两倍','1970-01-01 00:00:00','test',0),(32,'敏捷测试第一象限','单元测试/组件测试: 面向技术,一般是自动化测试完成,集成在CI流程中.测试目的主要是TDD(Test driven development)或者测试驱动设计','1970-01-01 00:00:00','test',0),(33,'敏捷测试第二象限','功能测试/原型/用户故事测试/实例/仿真,主要是自动化和手动结合.','1970-01-01 00:00:00','test',0),(34,'敏捷测试第三象限','探索性测试/用户场景测试/可用性测试/用户验收测试,面向业务,手动完成','1970-01-01 00:00:00','test',0),(35,'敏捷测试第四象限','性能和压力测试/安全测试/非功能测试,一般由工具来完成,用于评价产品','1970-01-01 00:00:00','test',0),(41,'mysql 主键','能够唯一标识表中某一行的属性或属性组。一个表只能有一个主键，但可以有多个候选索引。主键常常与外键构成参照完整性约束，防止出现数据不一致。主键可以保证记录的唯一和主键域非空,数据库管理系统对于主键自动生成唯一索引，所以主键也是一个特殊的索引','2020-04-22 21:31:27','admin',1),(42,'mysql外键','是用于建立和加强两个表数据之间的链接的一列或多列。外键约束主要用来维护两个表之间数据的一致性。简言之，表的外键就是另一表的主键，外键将两表联系起来。一般情况下，要删除一张表中的主键必须首先要确保其它表中的没有相同外键（即该表中的主键没有一个外键和它相关联）。','2020-04-22 21:40:47','admin',1),(43,'mysql索引','是用来快速地寻找那些具有特定值的记录。主要是为了检索的方便，是为了加快访问速度， 按一定的规则创建的，一般起到排序作用。所谓唯一性索引，这种索引和前面的“普通索引”基本相同，但有一个区别：索引列的所有值都只能出现一次，即必须唯一。','2020-04-22 21:46:17','admin',1),(44,'数据库事务四大原则ACID','事物的原子性(Atomic)、一致性(Consistent)、独立性(Isolated)及持久性(Durable)。   1.事务的原子性是指一个事务要么全部执行,要么不执行.也就是说一个事务不可能只执行了一半就停止了.    2.事务的一致性是指事务的运行并不改变数据库中数据的一致性.    3.事务的独立性是指两个以上的事务不会出现交错执行的状态.因为这样可能会导致数据不一致.    4.事务的持久性是指事务运行成功以后,就系统的更新是永久的.不会无缘无故的回滚.','2020-05-05 02:47:28','admin',1),(45,'性能测试主要考量项','1.响应时间 2.并发用户数 3.吞吐量 4.性能计数器 5.思考时间','2020-04-23 15:51:29','admin',3),(46,'协程','协程（英語：coroutine）是计算机程序的一类组件，推广了协作式多任务的子程序，允许执行被挂起与被恢复。相对子例程而言，协程更为一般和灵活，但在实践中使用没有子例程那样广泛。协程更适合于用来实现彼此熟悉的程序组件，如协作式多任务、异常处理、事件循环、迭代器、无限列表和管道。','2020-04-24 11:01:59','admin',2),(47,'进程','进程是具有一定独立功能的程序关于某个数据集合上的一次运行活动,进程是系统进行资源分配和调度的一个独立单位。每个进程都有自己的独立内存空间，不同进程通过进程间通信来通信。由于进程比较重量，占据独立的内存，所以上下文进程间的切换开销（栈、寄存器、虚拟内存、文件句柄等）比较大，但相对比较稳定安全。','2020-05-05 02:09:39','admin',2),(48,'线程','线程是进程的一个实体,是CPU调度和分派的基本单位,它是比进程更小的能独立运行的基本单位.线程自己基本上不拥有系统资源,只拥有一点在运行中必不可少的资源(如程序计数器,一组寄存器和栈),但是它可与同属一个进程的其他的线程共享进程所拥有的全部资源。线程间通信主要通过共享内存，上下文切换很快，资源开销较少，但相比进程不够稳定容易丢失数据。','2020-04-24 11:05:33','admin',2),(49,'mysql join 联合查询','JOIN: 如果表中有至少一个匹配，则返回行\r\nLEFT JOIN: 即使右表中没有匹配，也从左表返回所有的行\r\nRIGHT JOIN: 即使左表中没有匹配，也从右表返回所有的行\r\nFULL JOIN: 只要其中一个表中存在匹配，就返回行 ','2020-04-24 15:59:45','admin',1),(50,'mysql 两列算数运算','select a1,a2,a1+a2 a,a1*a2 b,a1*1.0/a2 c from bb_sb;\r\n把a表的a1,a2列相加作为新列a，把a1,a2相乘作为新列b，注意：\r\n相除的时候得进行类型转换处理，否则结果为0.\r\nselect a.a1,b.b1,a.a1+b.b1 a from bb_sb a ,bb_cywzbrzb b;\r\n这是两个不同表之间的列进行运算。','2020-04-24 16:12:44','admin',1),(51,'分布式存储','分布式存储系统，是将数据分散存储在多台独立的设备上。传统的网络存储系统采用集中的存储服务器存放所有数据，存储服务器成为系统性能的瓶颈，也是可靠性和安全性的焦点，不能满足大规模存储应用的需要。分布式网络存储系统采用可扩展的系统结构，利用多台存储服务器分担存储负荷，利用位置服务器定位存储信息，它不但提高了系统的可靠性、可用性和存取效率，还易于扩展。(一致性,可用性,分区容错性)','2020-04-28 09:27:47','admin',0),(52,'SQL注入','原理: SQL注入攻击是通过操作输入来修改SQL语句，用以达到执行代码对WEB服务器进行攻击的方法\r\n分类: 1:数字型/字符串型/搜索型 2:基于时间/报错/布尔/联合查询的盲注\r\n防范措施: 1. 分级管理,对用户进行严格的权限管理 2. 参数传值,对用户输入不能直接拼接到SQL语句中,进行参数代换 3. 基础过滤和二次过滤, 对用户输入进行检查，确保数据输入的安全性，在具体检查输入或提交的变量时，对于单引号、双引号、冒号等字符进行转换或者过滤，从而有效防止SQL注入。当然危险字符有很多，在获取用户输入提交的参数时，首先要进行基础过滤，然后根据程序的功能及用户输入的可能性进行二次过滤，以确保系统的安全性 4. 使用安全参数 5.漏洞扫描 6. 多层验证, 现在的网站系统功能越来越庞大复杂。为确保系统的安全，访问者的数据输入必须经过严格的验证才能进入系统，验证没通过的输入直接被拒绝访问数据库，并且向上层系统发出错误提示信息。同时在客户端访问程序中验证访问者的相关输入信息，从而更有效的防止简单的SQL注入。 7. 数据库信息加密,常用加密方法对称/非对称/不可逆加密 8.尽可能少的返回信息','2020-05-04 16:04:34','admin',4),(53,'XSS注入','原理: 跨站脚本攻击（XSS），是最普遍的Web应用安全漏洞。这类漏洞能够使得攻击者嵌入恶意脚本代码到正常用户会访问到的页面中，当正常用户访问该页面时，则可导致嵌入的恶意脚本代码的执行，从而达到恶意攻击用户的目的.\r\n分类: 持久型/响应型/DOM型\r\n防范手段: 1.基于特征的防御,过滤特殊字符串 2.基于代码的防御, 1)用户向服务器上提交的信息要对URL和附带的的HTTP头、POST数据等进行查询，对不是规定格式、长度的内容进行过滤。2)实现Session标记（session tokens）、CAPTCHA系统或者HTTP引用头检查，以防功能被第三方网站所执行。3)确认接收的的内容被妥善的规范化，仅包含最小的、安全的Tag（没有javascript），去掉任何对远程内容的引用（尤其是样式表和javascript），使用HTTP only的cookie。 3. 客户端分层防御策略,1)对每一个网页分配独立线程且分析资源消耗的“网页线程分析模块”；2)包含分层防御策略四个规则的用户输入分析模块；3)保存互联网上有关XSS恶意网站信息的XSS信息数据库。','2020-05-04 16:31:32','admin',4),(54,'CSRF攻击','原理: \r\n1.用户C打开浏览器，访问受信任网站A，输入用户名和密码请求登录网站A;\r\n2.在用户信息通过验证后，网站A产生Cookie信息并返回给浏览器，此时用户登录网站A成功，可以正常发送请求到网站A;\r\n3.用户未退出网站A之前，在同一浏览器中，打开一个TAB页访问网站B;\r\n4.网站B接收到用户请求后，返回一些攻击性代码，并发出一个请求要求访问第三方站点A;\r\n5.浏览器在接收到这些攻击性代码后，根据网站B的请求，在用户不知情的情况下携带Cookie信息，向网站A发出请求。网站A并不知道该请求其实是由B发起的，所以会根据用户C的Cookie信息以C的权限处理该请求，导致来自网站B的恶意代码被执行。\r\n防范策略: \r\n1.验证 HTTP Referer 字段；\r\n2.在请求地址中添加 token 并验证；\r\n3.在 HTTP 头中自定义属性并验证；\r\n4.Chrome 浏览器端启用 SameSite cookie','2020-05-04 16:39:51','admin',4);
/*!40000 ALTER TABLE `entries` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test_table`
--

DROP TABLE IF EXISTS `test_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `test_table` (
  `variable` varchar(128) NOT NULL,
  `value` varchar(128) DEFAULT NULL,
  `set_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `set_by` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`variable`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test_table`
--

LOCK TABLES `test_table` WRITE;
/*!40000 ALTER TABLE `test_table` DISABLE KEYS */;
INSERT INTO `test_table` VALUES ('1','enable','2020-04-08 09:11:28','admin'),('2','disable','2020-04-08 09:11:28','admin'),('3','true','2020-04-08 09:11:28','admin');
/*!40000 ALTER TABLE `test_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `username` varchar(100) NOT NULL DEFAULT '',
  `account` varchar(100) NOT NULL DEFAULT '',
  `email` varchar(100) NOT NULL DEFAULT '',
  `password` varchar(512) DEFAULT NULL,
  `createTime` datetime NOT NULL DEFAULT '1970-01-01 00:00:00',
  `updateBy` varchar(100) NOT NULL DEFAULT '',
  `createBy` varchar(100) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (20,'test','test account','test@123.com','e10adc3949ba59abbe56e057f20f883e','1970-01-01 00:00:00','admin','admin'),(21,'admin','admin','admin@123.com','21232f297a57a5a743894a0e4a801fc3','1970-01-01 00:00:00','admin','admin');
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

-- Dump completed on 2020-05-09 12:22:12
