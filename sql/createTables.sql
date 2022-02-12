create database newsinfomation;

use newsinfomation;
CREATE TABLE `news` (

`id` int(20) NOT NULL AUTO_INCREMENT comment '新闻id',

`title` varchar(255) DEFAULT NULL comment '新闻标题',

`fu_title` varchar(255) DEFAULT NULL comment '新闻副标题',

`url` varchar(255) DEFAULT NULL comment '新闻跳转链接',

`pic_url` varchar(255) DEFAULT NULL comment '新闻封面链接',

`type` tinyint(4) DEFAULT NULL comment '新闻类型 0是',

`created_at` int(11) DEFAULT NULL comment '爬取写入时间',

`updated_at` int(11) DEFAULT NULL comment '更新时间',

`news_address` varchar(50) DEFAULT NULL comment '新闻区域',

`news_time` varchar(50) DEFAULT NULL comment '实际新闻发布时间',

`md5str` char(50) DEFAULT NULL comment '内容识别，爬取判断是否重复',

PRIMARY KEY (`id`),

KEY `created_at` (`created_at`),

KEY `title` (`title`)

) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

create database testFlask;
use testFlask;
CREATE TABLE `tf_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '用户ID（主键ID）',
  `username` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '' COMMENT '昵称',
  `password` varchar(64) CHARACTER SET utf8 NOT NULL DEFAULT '' COMMENT '密码',
  `avatar` varchar(255) CHARACTER SET utf8 NOT NULL DEFAULT '' COMMENT '用户头像',
  `gender` tinyint(1) NOT NULL DEFAULT '0' COMMENT '性别。0=保密，1=男，2=女',
  `email` varchar(64) CHARACTER SET utf8 NOT NULL DEFAULT '' COMMENT '邮箱',
  `birthday` char(10) CHARACTER SET utf8 DEFAULT '' COMMENT '生日。使用字符串类型存储，后期可能存在不同格式拼接字符。格式：YYYY-MM-DD',
  `status` tinyint(1) NOT NULL DEFAULT '0' COMMENT '状态。0=正常，1=禁用',
  `openid` varchar(64) CHARACTER SET utf8 NOT NULL DEFAULT '' COMMENT '用户第三方授权登录openID',
  `os_uuid` varchar(100) CHARACTER SET utf8 NOT NULL DEFAULT '' COMMENT '客户端唯一设备UUID',
  `balance` decimal(10,2) NOT NULL DEFAULT '0.00' COMMENT '余额',
  `login_type` tinyint(1) NOT NULL DEFAULT '0' COMMENT '登录类型。0=游客（默认），1=Facebook，2=Google，3=Line，4=Twitter，5=Apple，6=其他',
  `app_version` varchar(30) CHARACTER SET utf8 NOT NULL DEFAULT '' COMMENT '注册时的APP版本',
  `os_version` varchar(30) CHARACTER SET utf8 NOT NULL DEFAULT '' COMMENT '手机操作系统版本',
  `platform` tinyint(4) NOT NULL DEFAULT '0' COMMENT '用户注册时终端平台。1=安卓，2=IOS',
  `invite_code` varchar(30) CHARACTER SET utf8 NOT NULL DEFAULT '' COMMENT '用户个人邀请码',
  `invite_user_id` int(11) NOT NULL DEFAULT '0' COMMENT '邀请用户ID（被哪个用户邀请进行注册的）',
  `last_login_time` int(11) NOT NULL DEFAULT '0' COMMENT '最近一次登录时间',
  `last_login_ip` varchar(15) CHARACTER SET utf8 NOT NULL DEFAULT '' COMMENT '最近一次登录IP地址',
  `create_time` int(11) NOT NULL DEFAULT '0' COMMENT '创建时间',
  `update_time` int(11) NOT NULL DEFAULT '0' COMMENT '更新时间',
  PRIMARY KEY (`id`),
  KEY `idx_os_uuid` (`os_uuid`) USING BTREE,
  KEY `idx_create_time` (`create_time`) USING BTREE,
  KEY `idx_login_type` (`login_type`) USING BTREE,
  KEY `idx_username` (`username`) USING BTREE,
  KEY `idx_openid` (`openid`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COMMENT='用户表';
select * from tf_user where username='孙军';

CREATE TABLE `invite_record` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '用户ID（主键ID）',
  `username` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '' COMMENT '成功邀请的注册昵称',
  `user_id` int(11) NOT NULL DEFAULT '0' COMMENT '被邀请方用户ID（成功邀请的注册昵称）',
  `invite_user_id` int(11) NOT NULL DEFAULT '0' COMMENT '邀请方用户ID（被哪个用户邀请进行注册的）',
  `invite_code` varchar(30) CHARACTER SET utf8 NOT NULL DEFAULT '' COMMENT '邀请方的邀请码',
  `login_type` tinyint(1) NOT NULL DEFAULT '0' COMMENT '登录类型。0=游客（默认），1=Facebook，2=Google，3=Line，4=Twitter，5=Apple，6=其他',
  `app_version` varchar(30) CHARACTER SET utf8 NOT NULL DEFAULT '' COMMENT '注册时的APP版本',
  `os_uuid` varchar(100) CHARACTER SET utf8 NOT NULL DEFAULT '' COMMENT '客户端唯一设备UUID',
  `platform` tinyint(4) NOT NULL DEFAULT '0' COMMENT '用户注册时终端平台。1=安卓，2=IOS',
  `invite_success_time` int(11) NOT NULL DEFAULT '0' COMMENT '成功邀请时间',
  `create_time` int(11) NOT NULL DEFAULT '0' COMMENT '创建时间',

  PRIMARY KEY (`id`),
  KEY `idx_os_uuid` (`os_uuid`) USING BTREE,
  KEY `idx_create_time` (`create_time`) USING BTREE,
  KEY `idx_login_type` (`login_type`) USING BTREE,
  KEY `idx_username` (`username`) USING BTREE

) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COMMENT='邀请记录表';

CREATE TABLE `tf_task_set` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lang` tinyint(1) NOT NULL DEFAULT '0' COMMENT '语言:1en,2id,3th,4vi,5ru',
  `task_name` varchar(50) NOT NULL DEFAULT '' COMMENT '任务名称',
  `task_desc` varchar(50) NOT NULL DEFAULT '' COMMENT '任务描述',
  `task_name_cn` varchar(50) NOT NULL DEFAULT '' COMMENT '任务中文名称',
  `task_name_cn_desc` varchar(50) NOT NULL DEFAULT '' COMMENT '任务中文描述',
  `task_coin` decimal(10,2) NOT NULL DEFAULT '0.00' COMMENT '任务金币',
  `coin_percent` decimal(10,2) NOT NULL DEFAULT '0.00' COMMENT '金币浮动百分比',
  `platform` tinyint(2) unsigned NOT NULL DEFAULT '0' COMMENT '客户端 0全部 1android 2iphone',
  `is_show` tinyint(2) unsigned NOT NULL DEFAULT '0' COMMENT '是否显示 1显示 0隐藏',
  `list_order` int(3) NOT NULL DEFAULT '1' COMMENT '排序越小越靠前',
  `award_time` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '奖励时间',
  `limit_time` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '触发时间(周听书超过此时间)',
  `task_type` tinyint(2) unsigned NOT NULL DEFAULT '1' COMMENT '任务类型 1邀请,2收听奖励,3(登录分享)每天领取,4一个帐号只能做一次任务',
  `create_time` int(11) NOT NULL DEFAULT '0' COMMENT '创建时间',
  `update_time` int(11) NOT NULL DEFAULT '0' COMMENT '更新时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COMMENT='任务中心设置';