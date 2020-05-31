drop table if exists entries;
CREATE TABLE entries (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `title` varchar(100) NOT NULL DEFAULT '' COMMENT 'Unique ID for clients.',
  `text` varchar(512) DEFAULT NULL,
  `createTime` datetime NOT NULL DEFAULT '1970-01-01 00:00:00',
  `updateBy` varchar(100) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;

CREATE TABLE users (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `username` varchar(100) NOT NULL DEFAULT '',
  `account` varchar(100) NOT NULL DEFAULT '',
  `email` varchar(100) NOT NULL DEFAULT '',
  `password` varchar(512) DEFAULT NULL,
  `createTime` datetime NOT NULL DEFAULT '1970-01-01 00:00:00',
  `updateBy` varchar(100) NOT NULL DEFAULT '',
  `createBy` varchar(100) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;

create unique index uk_username
	on users (username);

create unique index uk_title
	on entries (title);

ALTER TABLE flask.entries ADD COLUMN `Catalogs` int(11) NOT NULL DEFAULT '0' COMMENT '0:test;1:mysql;2:python...' ;

CREATE TABLE `flask`.`catalogs` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `catalogName` VARCHAR(45) NOT NULL COMMENT 'all catalogs of notes',
  `catalogNumber` INT NOT NULL,
  `createTime` DATETIME NOT NULL DEFAULT '1970-01-01 00:00:00',
  `createBy` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  UNIQUE INDEX `catalogName_UNIQUE` (`catalogName` ASC),
  UNIQUE INDEX `catalogNumber_UNIQUE` (`catalogNumber` ASC));

CREATE TABLE `roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `roleName` varchar(45) NOT NULL COMMENT 'role name',
  `roleCode` int(11) NOT NULL,
  `description` varchar(100) default NULL,
  `createTime` datetime NOT NULL DEFAULT '1970-01-01 00:00:00',
  `createBy` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `role_id_UNIQUE` (`id`),
  UNIQUE KEY `roleName_UNIQUE` (`roleName`),
  UNIQUE KEY `roleCode_UNIQUE` (`roleCode`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

CREATE TABLE `permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `permissionName` varchar(45) NOT NULL COMMENT 'permissions name',
  `permissionCode` int(11) NOT NULL,
  `description` varchar(100) default NULL,
  `createTime` datetime NOT NULL DEFAULT '1970-01-01 00:00:00',
  `createBy` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `permission_id_UNIQUE` (`id`),
  UNIQUE KEY `permissionName_UNIQUE` (`permissionName`),
  UNIQUE KEY `permissionCode_UNIQUE` (`permissionCode`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

CREATE TABLE `role_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `permission` int(11) NOT NULL COMMENT 'permissionCode',
  `roleCode` int(11) NOT NULL,
  `createTime` datetime NOT NULL DEFAULT '1970-01-01 00:00:00',
  `createBy` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

CREATE TABLE `user_role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(45) NOT NULL COMMENT 'username',
  `roleCode` int(11) NOT NULL,
  `createTime` datetime NOT NULL DEFAULT '1970-01-01 00:00:00',
  `createBy` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- add role code column of table users
alter table users add roleCode int(11) not null default 1;

-- add default role admin/user
INSERT INTO `flask`.`roles` (`roleName`, `roleCode`, `description`, `createTime`, `createBy`) VALUES ('admin', '1', 'superadmin', '2020-05-29 14:50:47', 'admin');
INSERT INTO `flask`.`roles` (`roleName`, `roleCode`, `description`, `createTime`, `createBy`) VALUES ('user', '2', 'default_user', '2020-05-29 14:50:47', 'admin');

-- add parent permission code of table permissions
alter table permissions add parentPermissionCode int(11) not null default 0 after permissionCode;