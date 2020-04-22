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

ALTER TABLE flask.entries ADD COLUMN `Catalogs` int(11) NOT NULL DEFAULT '0' COMMENT '0:test;1:mysql;2:python...' ;