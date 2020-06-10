CREATE DATABASE  IF NOT EXISTS `flask` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `flask`;
-- MySQL dump 10.13  Distrib 8.0.20, for Linux (x86_64)
--
-- Host: localhost    Database: flask
-- ------------------------------------------------------
-- Server version	5.7.30-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
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
/*!50503 SET character_set_client = utf8mb4 */;
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
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `catalogs`
--

LOCK TABLES `catalogs` WRITE;
/*!40000 ALTER TABLE `catalogs` DISABLE KEYS */;
INSERT INTO `catalogs` VALUES (1,'test',0,'1970-01-01 00:00:00','admin'),(2,'mysql',1,'1970-01-01 00:00:00','admin'),(3,'python',2,'1970-01-01 00:00:00','admin'),(4,'performance',3,'1970-01-01 00:00:00','admin'),(5,'security',4,'1970-01-01 00:00:00','admin'),(6,'storage',5,'1970-01-01 00:00:00','admin'),(7,'redis',6,'2020-06-08 14:07:21','admin'),(8,'ELK',7,'2020-06-10 20:51:18','admin');
/*!40000 ALTER TABLE `catalogs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `entries`
--

DROP TABLE IF EXISTS `entries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `entries` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `title` varchar(100) NOT NULL DEFAULT '' COMMENT 'Unique ID for clients.',
  `text` varchar(512) DEFAULT NULL,
  `createTime` datetime NOT NULL DEFAULT '1970-01-01 00:00:00',
  `updateBy` varchar(100) NOT NULL DEFAULT '',
  `Catalogs` int(11) NOT NULL DEFAULT '0' COMMENT '0:测试;1:mysql;2:python...',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_title` (`title`)
) ENGINE=InnoDB AUTO_INCREMENT=80 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `entries`
--

LOCK TABLES `entries` WRITE;
/*!40000 ALTER TABLE `entries` DISABLE KEYS */;
INSERT INTO `entries` VALUES (20,'测试用例设计包含哪些？','1.用例编号\r\n2.story编号\r\n3.优先级\r\n4.前置条件\r\n5.执行步骤\r\n6.预期结果\r\n7.实际结果\r\n8.用例名称\r\n9.测试数据\r\n10.用例分类\r\n11.测试环境\r\n12.设计人\r\n13.通过与否','1970-01-01 00:00:00','admin',0),(21,'测试用例设计方法','1.等价类划分\r\n2.边界值划分\r\n3.因果图\r\n4.正交排列\r\n5.错误推测方法','1970-01-01 00:00:00','admin',0),(22,'软件测试包含哪些方面','功能测试、性能测试、压力测试、负载测试、代码健壮性、可靠性、安全性、可用性、易用性、异常测试、场景测试','2020-05-05 01:31:58','admin',0),(23,'测试金字塔','e2e测试、组件测试、API测试、单元测试','1970-01-01 00:00:00','admin',0),(24,'TDD','Test Driven development:敏捷开发基本思想\r\n单元测试用例首先完成，增加开发效率以及正针对性，但是又增加了代码量，测试代码是开发代码的两倍','1970-01-01 00:00:00','admin',0),(32,'敏捷测试第一象限','单元测试/组件测试: 面向技术,一般是自动化测试完成,集成在CI流程中.测试目的主要是TDD(Test driven development)或者测试驱动设计','1970-01-01 00:00:00','admin',0),(33,'敏捷测试第二象限','功能测试/原型/用户故事测试/实例/仿真,主要是自动化和手动结合.','1970-01-01 00:00:00','admin',0),(34,'敏捷测试第三象限','探索性测试/用户场景测试/可用性测试/用户验收测试,面向业务,手动完成','1970-01-01 00:00:00','admin',0),(35,'敏捷测试第四象限','性能和压力测试/安全测试/非功能测试,一般由工具来完成,用于评价产品','1970-01-01 00:00:00','admin',0),(41,'mysql 主键','能够唯一标识表中某一行的属性或属性组。一个表只能有一个主键，但可以有多个候选索引。主键常常与外键构成参照完整性约束，防止出现数据不一致。主键可以保证记录的唯一和主键域非空,数据库管理系统对于主键自动生成唯一索引，所以主键也是一个特殊的索引','2020-04-22 21:31:27','admin',1),(42,'mysql外键','是用于建立和加强两个表数据之间的链接的一列或多列。外键约束主要用来维护两个表之间数据的一致性。简言之，表的外键就是另一表的主键，外键将两表联系起来。一般情况下，要删除一张表中的主键必须首先要确保其它表中的没有相同外键（即该表中的主键没有一个外键和它相关联）。','2020-04-22 21:40:47','admin',1),(43,'mysql索引','是用来快速地寻找那些具有特定值的记录。主要是为了检索的方便，是为了加快访问速度， 按一定的规则创建的，一般起到排序作用。所谓唯一性索引，这种索引和前面的“普通索引”基本相同，但有一个区别：索引列的所有值都只能出现一次，即必须唯一。','2020-04-22 21:46:17','admin',1),(44,'数据库事务四大原则ACID','事物的原子性(Atomic)、一致性(Consistent)、独立性(Isolated)及持久性(Durable)。   1.事务的原子性是指一个事务要么全部执行,要么不执行.也就是说一个事务不可能只执行了一半就停止了.    2.事务的一致性是指事务的运行并不改变数据库中数据的一致性.    3.事务的独立性是指两个以上的事务不会出现交错执行的状态.因为这样可能会导致数据不一致.    4.事务的持久性是指事务运行成功以后,就系统的更新是永久的.不会无缘无故的回滚.','2020-05-18 13:00:32','admin',1),(45,'性能测试主要考量项','1.响应时间 2.并发用户数 3.吞吐量 4.性能计数器 5.思考时间','2020-04-23 15:51:29','admin',3),(46,'协程','协程（英語：coroutine）是计算机程序的一类组件，推广了协作式多任务的子程序，允许执行被挂起与被恢复。相对子例程而言，协程更为一般和灵活，但在实践中使用没有子例程那样广泛。协程更适合于用来实现彼此熟悉的程序组件，如协作式多任务、异常处理、事件循环、迭代器、无限列表和管道。','2020-04-24 11:01:59','admin',2),(47,'进程','进程是具有一定独立功能的程序关于某个数据集合上的一次运行活动,进程是系统进行资源分配和调度的一个独立单位。每个进程都有自己的独立内存空间，不同进程通过进程间通信来通信。由于进程比较重量，占据独立的内存，所以上下文进程间的切换开销（栈、寄存器、虚拟内存、文件句柄等）比较大，但相对比较稳定安全。','2020-05-20 14:18:37','admin',2),(48,'线程','线程是进程的一个实体,是CPU调度和分派的基本单位,它是比进程更小的能独立运行的基本单位.线程自己基本上不拥有系统资源,只拥有一点在运行中必不可少的资源(如程序计数器,一组寄存器和栈),但是它可与同属一个进程的其他的线程共享进程所拥有的全部资源。线程间通信主要通过共享内存，上下文切换很快，资源开销较少，但相比进程不够稳定容易丢失数据。','2020-04-24 11:05:33','admin',2),(49,'mysql join 联合查询','JOIN: 如果表中有至少一个匹配，则返回行LEFT JOIN: 即使右表中没有匹配，也从左表返回所有的行RIGHT JOIN: 即使左表中没有匹配，也从右表返回所有的行FULL JOIN: 只要其中一个表中存在匹配，就返回行 ','2020-05-20 16:23:29','admin',1),(50,'mysql 两列算数运算','select a1,a2,a1+a2 a,a1*a2 b,a1*1.0/a2 c from bb_sb;\r\n把a表的a1,a2列相加作为新列a，把a1,a2相乘作为新列b，注意：\r\n相除的时候得进行类型转换处理，否则结果为0.\r\nselect a.a1,b.b1,a.a1+b.b1 a from bb_sb a ,bb_cywzbrzb b;\r\n这是两个不同表之间的列进行运算。','2020-04-24 16:12:44','admin',1),(51,'分布式存储','分布式存储系统，是将数据分散存储在多台独立的设备上。传统的网络存储系统采用集中的存储服务器存放所有数据，存储服务器成为系统性能的瓶颈，也是可靠性和安全性的焦点，不能满足大规模存储应用的需要。分布式网络存储系统采用可扩展的系统结构，利用多台存储服务器分担存储负荷，利用位置服务器定位存储信息，它不但提高了系统的可靠性、可用性和存取效率，还易于扩展。(一致性,可用性,分区容错性)','2020-05-22 09:34:48','admin',5),(52,'SQL注入','原理: SQL注入攻击是通过操作输入来修改SQL语句，用以达到执行代码对WEB服务器进行攻击的方法\r\n分类: 1:数字型/字符串型/搜索型 2:基于时间/报错/布尔/联合查询的盲注\r\n防范措施: 1. 分级管理,对用户进行严格的权限管理 2. 参数传值,对用户输入不能直接拼接到SQL语句中,进行参数代换 3. 基础过滤和二次过滤, 对用户输入进行检查，确保数据输入的安全性，在具体检查输入或提交的变量时，对于单引号、双引号、冒号等字符进行转换或者过滤，从而有效防止SQL注入。当然危险字符有很多，在获取用户输入提交的参数时，首先要进行基础过滤，然后根据程序的功能及用户输入的可能性进行二次过滤，以确保系统的安全性 4. 使用安全参数 5.漏洞扫描 6. 多层验证, 现在的网站系统功能越来越庞大复杂。为确保系统的安全，访问者的数据输入必须经过严格的验证才能进入系统，验证没通过的输入直接被拒绝访问数据库，并且向上层系统发出错误提示信息。同时在客户端访问程序中验证访问者的相关输入信息，从而更有效的防止简单的SQL注入。 7. 数据库信息加密,常用加密方法对称/非对称/不可逆加密 8.尽可能少的返回信息','2020-05-04 16:04:34','admin',4),(53,'XSS注入','原理: 跨站脚本攻击（XSS），是最普遍的Web应用安全漏洞。这类漏洞能够使得攻击者嵌入恶意脚本代码到正常用户会访问到的页面中，当正常用户访问该页面时，则可导致嵌入的恶意脚本代码的执行，从而达到恶意攻击用户的目的.\r\n分类: 持久型/响应型/DOM型\r\n防范手段: 1.基于特征的防御,过滤特殊字符串 2.基于代码的防御, 1)用户向服务器上提交的信息要对URL和附带的的HTTP头、POST数据等进行查询，对不是规定格式、长度的内容进行过滤。2)实现Session标记（session tokens）、CAPTCHA系统或者HTTP引用头检查，以防功能被第三方网站所执行。3)确认接收的的内容被妥善的规范化，仅包含最小的、安全的Tag（没有javascript），去掉任何对远程内容的引用（尤其是样式表和javascript），使用HTTP only的cookie。 3. 客户端分层防御策略,1)对每一个网页分配独立线程且分析资源消耗的“网页线程分析模块”；2)包含分层防御策略四个规则的用户输入分析模块；3)保存互联网上有关XSS恶意网站信息的XSS信息数据库。','2020-05-04 16:31:32','admin',4),(54,'CSRF攻击','原理: 1.用户C打开浏览器，访问受信任网站A，输入用户名和密码请求登录网站A;2.在用户信息通过验证后，网站A产生Cookie信息并返回给浏览器，此时用户登录网站A成功，可以正常发送请求到网站A;3.用户未退出网站A之前，在同一浏览器中，打开一个TAB页访问网站B;4.网站B接收到用户请求后，返回一些攻击性代码，并发出一个请求要求访问第三方站点A;5.浏览器在接收到这些攻击性代码后，根据网站B的请求，在用户不知情的情况下携带Cookie信息，向网站A发出请求。网站A并不知道该请求其实是由B发起的，所以会根据用户C的Cookie信息以C的权限处理该请求，导致来自网站B的恶意代码被执行。防范策略: 1.验证 HTTP Referer 字段；2.在请求地址中添加 token 并验证；3.在 HTTP 头中自定义属性并验证；4.Chrome 浏览器端启用 SameSite cookie','2020-05-29 14:41:17','admin',4),(55,'对象存储','对象存储，也叫做基于对象的存储，是用来描述解决和处理离散单元的方法的通用术语，这些离散单元被称作为对象。','2020-05-22 09:18:59','admin',5),(57,'where/having','having字句可以让我们筛选成组后的各种数据，where字句在聚合前先筛选记录，也就是说作用在group by和having字句前。而 having子句在聚合后对组记录进行筛选\r\nselect Catalogs, count(*) from entries where Catalogs = 0 or Catalogs = 1 group by Catalogs;\r\nselect Catalogs, count(*) from entries group by Catalogs having Catalogs = 0 or Catalogs = 1;\r\n第一个首先使用where过滤，数据集变小，在分组统计，性能较好','2020-05-25 16:51:26','admin',1),(60,'字符串转换为布尔型','distutils.util.strtobool(val)\r\nConvert a string representation of truth to true (1) or false (0).\r\nTrue values are y, yes, t, true, on and 1; false values are n, no, f, false, off and 0. Raises ValueError if val is anything else.','2020-05-26 16:51:26','admin',2),(61,'python 不可变数据类型','可变数据类型：列表list和字典dict\r\n不可变数据类型：整型int、浮点型float、字符串型string和元组tuple','2020-05-26 17:00:23','admin',2),(62,'mysql添加/删除外键','添加：alter table 表名 add constraint FK_ID foreign key(你的外键字段名) REFERENCES 外表表名(对应的表的主键字段名);\r\n删除：ALTER TABLE table-name DROP FOREIGN KEY key-id;','2020-05-27 11:16:47','admin',1),(68,'mysql 新增字段','ALTER TABLE <表名> ADD <新字段名><数据类型>[约束条件] after a_column;','2020-05-29 14:52:17','admin',1),(69,'mysql5.7 修改root密码','跳过密码验证:skip-grant-tables\r\n选择数据库：use mysql;\r\n更新root的密码：update user set authentication_string=password(\'新密码\'),plugin=\'mysql_native_password\' where user=\'root\' and Host=\'localhost\';\r\n刷新权限：flush privileges;','2020-06-02 00:12:02','admin',1),(70,'redis 设置密码','1.在配置文件中/etc/redis/redis.conf 加上 requirepass your_pwd 然后重启redis服务，密码一直有效。\r\n2.登陆redis-client设置： config set requirepass your_pwd 立即生效，重启过后失效。','2020-06-08 14:06:12','admin',6),(71,'软件性能测试4个不同层面','用户角度（用户从发出请求到感受到响应）\r\n管理员角度（已知并发数响应时间等，观测服务器CPU/memary/数据库状态；系统可扩展性/并发能力/最大容量/系统瓶颈）\r\n开发人员角度（架构设计/数据库设计/代码性能及合理性/线程同步合理性/资源竞争）\r\nweb前段性能（浏览器页面加载时间：HTML解析/图片和CSS获取加载/JS执行时间/页面展示时间）','2020-06-10 13:57:43','admin',3),(72,'软件性能主要术语','响应时间：（呈现时间/服务端响应时间）并发用户数：（同时在线用户数）吞吐量：请求数/S，页面数/S（反映服务端承受的压力）性能计数器：（内存数/进程时间）思考时间：（两请求间隔时间）','2020-06-10 14:28:19','admin',3),(73,'MySQL数据库作发布系统的存储，一天五万条以上的增量，预计运维三年,怎么优化？','a. 设计良好的数据库结构，允许部分数据冗余，尽量避免join查询，提高效率。\r\nb. 选择合适的表字段数据类型和存储引擎，适当的添加索引。\r\nc. mysql库主从读写分离。\r\nd. 找规律分表，减少单表中的数据量提高查询速度。\r\ne. 添加缓存机制，比如memcached，apc等。\r\nf. 不经常改动的页面，生成静态页面。\r\ng. 书写高效率的SQL。比如 SELECT * FROM TABEL 改为 SELECT field_1, field_2, field_3 FROM TABLE.','2020-06-10 20:26:40','admin',1),(74,'实践中如何优化MySQL','最好是按照以下顺序优化：\r\n1.SQL语句及索引的优化\r\n2.数据库表结构的优化\r\n3.系统配置的优化\r\n4.硬件的优化','2020-06-10 20:26:40','admin',1),(75,'优化数据库的方法','1.选取最适用的字段属性，尽可能减少定义字段宽度，尽量把字段设置NOTNULL，例如’省份’、’性别’最好适用ENUM\r\n2.使用连接(JOIN)来代替子查询\r\n3.适用联合(UNION)来代替手动创建的临时表\r\n4.事务处理\r\n5.锁定表、优化事务处理\r\n6.适用外键，优化锁定表\r\n7.建立索引\r\n8.优化查询语句','2020-06-10 20:26:40','admin',1),(76,'如何通俗地理解三个范式','第一范式：1NF是对属性的原子性约束，要求属性具有原子性，不可再分解；\r\n第二范式：2NF是对记录的惟一性约束，要求记录有惟一标识，即实体的惟一性；  \r\n第三范式：3NF是对字段冗余性的约束，即任何字段不能由其他字段派生出来，它要求字段没有冗余。。\r\n范式化设计优缺点:\r\n优点:可以尽量得减少数据冗余，使得更新快，体积小\r\n缺点:对于查询需要多个表进行关联，减少写得效率增加读得效率，更难进行索引优化\r\n反范式化:\r\n优点:可以减少表得关联，可以更好得进行索引优化\r\n缺点:数据冗余以及数据异常，数据得修改需要更多的成本','2020-06-10 20:26:40','admin',1),(77,'SQL语句优化','（1）Where子句中：where表之间的连接必须写在其他Where条件之前，那些可以过滤掉最大数量记录的条件必须写在Where子句的末尾.HAVING最后。\r\n（2）用EXISTS替代IN、用NOT EXISTS替代NOT IN。\r\n（3）避免在索引列上使用计算\r\n（4）避免在索引列上使用IS NULL和IS NOT NULL\r\n（5）对查询进行优化，应尽量避免全表扫描，首先应考虑在 where 及 order by 涉及的列上建立索引。\r\n（6）应尽量避免在 where 子句中对字段进行 null 值判断，否则将导致引擎放弃使用索引而进行全表扫描\r\n（7）应尽量避免在 where 子句中对字段进行表达式操作，这将导致引擎放弃使用索引而进行全表扫描','2020-06-10 20:26:40','admin',1),(78,'分库分表种类','1、垂直拆分\r\n      在考虑数据拆分的时候，一般情况下，应该先考虑垂直拆分。垂直可以理解为分出来的库表结构是互相独立各不相同的、\r\n      - 如果有多个业务，每个业务直接关联性不大，那么就可以把每个业务拆分为独立的实例、库或表。\r\n      - 如果在一个库里面有多张表，那么可以把每张表拆分到不同的实例上。\r\n      - 如果你有一张表，但这个表里的字段很多，每个字段都有不同的含义，例如user表里面有姓名、生日、地址等，那么可以把每个字段独立出来拆分为一张新表。\r\n2、水平拆分\r\n      水平拆分是针对一张表来说的。在经过垂直拆分之后，如果数据量依然很大，那么可以通过某种算法进行水平拆分。拆分后具有多张相同表结构的表，每张表存储一部分数据。','2020-06-10 20:26:40','admin',1),(79,'分库分表原则','1、原则1：能不分就不分\r\n      MySQL是关系型数据库，数据库表之间的关系从一定角度映射了业务逻辑。任何分库分表的行为都会提升业务逻辑的复杂度，数据库除了承载数据的存储和访问外，协助业务更好地实现需求和逻辑也是其重要的工作之一。分库分表会带来数据的合并、查询、更新条件的分离，以及事物的分离等多种后果，业务实现的复杂度往往会翻倍或指数级上升。所以在分表分库之前，应先升级硬盘、内存、CPU、网络、版本、读写分离、负载均衡及SQL语句优化。\r\n2、原则2：数据量太大，正常的运维影响业务访问\r\n      正常运维主要包括：\r\n      - 数据库的备份\r\n      - 数据表的修改\r\n      - 热点数据\r\n3、原则3：表设计不合理\r\n      - 某个表字段不断被update，压力非常大\r\n      - 某个表字段存在TEXT或BLOB字段\r\n4、原则4：某些数据表出现了无穷增长的情况\r\n      各种评论、消息、日志记录表现为不可控的增长，此时可按用户、时间、用途等进行水平拆分。','2020-06-10 20:26:40','admin',1);
/*!40000 ALTER TABLE `entries` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `permissions`
--

DROP TABLE IF EXISTS `permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `permissionName` varchar(45) NOT NULL COMMENT 'permissions name',
  `permissionCode` int(11) NOT NULL,
  `parentPermissionCode` int(11) NOT NULL DEFAULT '0',
  `description` varchar(100) DEFAULT NULL,
  `createTime` datetime NOT NULL DEFAULT '1970-01-01 00:00:00',
  `createBy` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `permission_id_UNIQUE` (`id`),
  UNIQUE KEY `permissionName_UNIQUE` (`permissionName`),
  UNIQUE KEY `permissionCode_UNIQUE` (`permissionCode`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `permissions`
--

LOCK TABLES `permissions` WRITE;
/*!40000 ALTER TABLE `permissions` DISABLE KEYS */;
INSERT INTO `permissions` VALUES (1,'entry_management',1,0,'entry management','2020-05-29 14:50:47','admin'),(2,'add_entry',2,1,'add entry','2020-05-29 14:50:47','admin'),(3,'search_entry',3,1,'search entry','2020-05-29 14:50:47','admin'),(4,'edit_entry',4,1,'edit entry','2020-05-29 14:50:47','admin'),(5,'delete_entry',5,1,'delete entry','2020-05-29 14:50:47','admin'),(6,'user_management',6,0,'user management','2020-05-29 14:50:47','admin'),(7,'add_user',7,6,NULL,'2020-05-29 14:50:47','admin'),(8,'search_user',8,6,NULL,'2020-05-29 14:50:47','admin'),(9,'edit_user',9,6,NULL,'2020-05-29 14:50:47','admin'),(10,'delete_user',10,6,NULL,'2020-05-29 14:50:47','admin'),(11,'catalog_management',11,0,NULL,'2020-05-29 14:50:47','admin'),(12,'role_management',12,0,NULL,'2020-05-29 14:50:47','admin'),(13,'add_catalog',13,11,NULL,'2020-05-29 14:50:47','admin'),(14,'search_catalog',14,11,NULL,'2020-05-29 14:50:47','admin'),(15,'edit_catalog',15,11,NULL,'2020-05-29 14:50:47','admin'),(16,'delete_catalog',16,11,NULL,'2020-05-29 14:50:47','admin'),(17,'add_role',17,12,NULL,'2020-05-29 14:50:47','admin'),(18,'edit_role',18,12,NULL,'2020-05-29 14:50:47','admin'),(19,'search_role',19,12,NULL,'2020-05-29 14:50:47','admin'),(20,'delete_role',20,12,NULL,'2020-05-29 14:50:47','admin');
/*!40000 ALTER TABLE `permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role_permissions`
--

DROP TABLE IF EXISTS `role_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `role_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `permission` int(11) NOT NULL COMMENT 'permission',
  `roleCode` int(11) NOT NULL,
  `createTime` datetime NOT NULL DEFAULT '1970-01-01 00:00:00',
  `createBy` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role_permissions`
--

LOCK TABLES `role_permissions` WRITE;
/*!40000 ALTER TABLE `role_permissions` DISABLE KEYS */;
INSERT INTO `role_permissions` VALUES (9,1,1,'2020-05-29 14:50:47','admin'),(10,2,1,'2020-05-29 14:50:47','admin'),(11,3,1,'2020-05-29 14:50:47','admin'),(12,4,1,'2020-05-29 14:50:47','admin'),(13,5,1,'2020-05-29 14:50:47','admin'),(14,6,1,'2020-05-29 14:50:47','admin'),(15,7,1,'2020-05-29 14:50:47','admin'),(16,8,1,'2020-05-29 14:50:47','admin'),(17,9,1,'2020-05-29 14:50:47','admin'),(18,10,1,'2020-05-29 14:50:47','admin'),(19,11,1,'2020-05-29 14:50:47','admin'),(20,12,1,'2020-05-29 14:50:47','admin'),(21,13,1,'2020-05-29 14:50:47','admin'),(22,14,1,'2020-05-29 14:50:47','admin'),(23,15,1,'2020-05-29 14:50:47','admin'),(24,16,1,'2020-05-29 14:50:47','admin'),(25,17,1,'2020-05-29 14:50:47','admin'),(26,18,1,'2020-05-29 14:50:47','admin'),(27,19,1,'2020-05-29 14:50:47','admin'),(28,20,1,'2020-05-29 14:50:47','admin'),(29,1,2,'2020-05-29 14:50:47','admin'),(30,2,2,'2020-05-29 14:50:47','admin'),(31,3,2,'2020-05-29 14:50:47','admin'),(32,4,2,'2020-05-29 14:50:47','admin'),(33,3,3,'2020-06-08 15:00:36','admin');
/*!40000 ALTER TABLE `role_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `roleName` varchar(45) NOT NULL COMMENT 'role name',
  `roleCode` int(11) NOT NULL,
  `description` varchar(100) DEFAULT NULL,
  `createTime` datetime NOT NULL DEFAULT '1970-01-01 00:00:00',
  `createBy` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `role_id_UNIQUE` (`id`),
  UNIQUE KEY `roleName_UNIQUE` (`roleName`),
  UNIQUE KEY `roleCode_UNIQUE` (`roleCode`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` VALUES (1,'admin',1,'superadmin','2020-05-29 14:50:47','admin'),(2,'user',2,'default_user','2020-05-29 14:50:47','admin'),(3,'read_user',3,'readonly','2020-06-08 15:00:19','admin');
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test_table`
--

DROP TABLE IF EXISTS `test_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
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
-- Table structure for table `user_role`
--

DROP TABLE IF EXISTS `user_role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(45) NOT NULL COMMENT 'username',
  `roleCode` int(11) NOT NULL,
  `createTime` datetime NOT NULL DEFAULT '1970-01-01 00:00:00',
  `createBy` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_role`
--

LOCK TABLES `user_role` WRITE;
/*!40000 ALTER TABLE `user_role` DISABLE KEYS */;
INSERT INTO `user_role` VALUES (1,'admin',1,'2020-05-29 14:50:47','admin'),(2,'test',2,'2020-05-29 14:50:47','admin'),(3,'test1',2,'2020-05-29 14:50:47','admin'),(4,'test2',2,'2020-05-29 14:50:47','admin');
/*!40000 ALTER TABLE `user_role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `username` varchar(100) NOT NULL DEFAULT '',
  `account` varchar(100) NOT NULL DEFAULT '',
  `email` varchar(100) NOT NULL DEFAULT '',
  `password` varchar(512) DEFAULT NULL,
  `createTime` datetime NOT NULL DEFAULT '1970-01-01 00:00:00',
  `updateBy` varchar(100) NOT NULL DEFAULT '',
  `createBy` varchar(100) NOT NULL DEFAULT '',
  `roleCode` int(11) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (20,'test','test account','test@123.com','e10adc3949ba59abbe56e057f20f883e','1970-01-01 00:00:00','admin','admin',2),(21,'admin','admin','admin@123.com','21232f297a57a5a743894a0e4a801fc3','1970-01-01 00:00:00','admin','admin',1),(22,'test1','test11','test11','25d55ad283aa400af464c76d713c07ad','2020-05-29 14:50:47','admin','admin',2),(23,'test2','test2','12345678','25d55ad283aa400af464c76d713c07ad','2020-05-31 14:35:23','admin','admin',2);
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

-- Dump completed on 2020-06-10 21:02:30
