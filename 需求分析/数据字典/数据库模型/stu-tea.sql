/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2021/6/29 21:31:37                           */
/*==============================================================*/


drop table if exists admin;

drop table if exists captain;

drop table if exists collect;

drop table if exists collectGroup;

drop table if exists comments;

drop table if exists communicate;

drop table if exists communicate2;

drop table if exists communication;

drop table if exists complain;

drop table if exists createOrder;

drop table if exists goods;

drop table if exists group;

drop table if exists group_order;

drop table if exists group_user;

drop table if exists inform;

drop table if exists message;

drop table if exists recommends;

drop table if exists relationship;

drop table if exists relationship2;

drop table if exists report;

drop table if exists sComments;

drop table if exists sTag;

drop table if exists share;

drop table if exists tag;

drop table if exists user;

/*==============================================================*/
/* Table: admin                                                 */
/*==============================================================*/
create table admin
(
   admin_id             int not null,
   use_user_account     varchar(255),
   user_account         varchar(255) not null,
   primary key (admin_id)
);

/*==============================================================*/
/* Table: captain                                               */
/*==============================================================*/
create table captain
(
   captain_id           int not null,
   use_user_account     varchar(255),
   user_account         varchar(255) not null,
   captain_name         varchar(255) not null,
   captain_idCard       int not null,
   hasShop              int not null,
   captain_location     varchar(255) not null,
   captain_locationNum  varchar(255),
   captain_location_pic varchar(255) not null,
   captain_idCard_pic   varchar(255) not null,
   captain_license_pic  varchar(255),
   primary key (captain_id)
);

/*==============================================================*/
/* Table: collect                                               */
/*==============================================================*/
create table collect
(
   收藏ID                 char(10) not null,
   user_account         varchar(255),
   用户账号                 char(10) not null,
   团购ID                 char(10) not null,
   primary key (收藏ID)
);

/*==============================================================*/
/* Table: collectGroup                                          */
/*==============================================================*/
create table collectGroup
(
   group_id             int not null,
   收藏ID                 char(10) not null,
   primary key (group_id, 收藏ID)
);

/*==============================================================*/
/* Table: comments                                              */
/*==============================================================*/
create table comments
(
   group_id             int not null,
   comments_id          int not null,
   use_user_account     varchar(255),
   gro_group_id         int,
   user_account         varchar(255) not null,
   comments_content     varchar(255) not null,
   comments_date        varchar(255) not null,
   comments_tagCnt      int not null,
   comments_reportCnt   int not null,
   primary key (group_id, comments_id)
);

/*==============================================================*/
/* Table: communicate                                           */
/*==============================================================*/
create table communicate
(
   communicate_id       int not null,
   use_user_account     varchar(255),
   com_communication_room_id int,
   communication_room_id int not null,
   user_account         varchar(255) not null,
   communicate_content  varchar(255) not null,
   communicate_sendtime int not null,
   primary key (communicate_id)
);

/*==============================================================*/
/* Table: communicate2                                          */
/*==============================================================*/
create table communicate2
(
   communication_room_id int not null,
   user_account         varchar(255) not null,
   primary key (communication_room_id, user_account)
);

/*==============================================================*/
/* Table: communication                                         */
/*==============================================================*/
create table communication
(
   communication_room_id int not null,
   user_account         varchar(255),
   primary key (communication_room_id)
);

/*==============================================================*/
/* Table: complain                                              */
/*==============================================================*/
create table complain
(
   complain_id          int not null,
   use_user_account     varchar(255),
   user_account         varchar(255) not null,
   complain_time        varchar(255) not null,
   complain_function    int not null,
   primary key (complain_id)
);

/*==============================================================*/
/* Table: createOrder                                           */
/*==============================================================*/
create table createOrder
(
   order_id             int not null,
   group_id             varchar(255) not null,
   gro_group_id         int not null,
   primary key (order_id, group_id, gro_group_id)
);

/*==============================================================*/
/* Table: goods                                                 */
/*==============================================================*/
create table goods
(
   group_id             int not null,
   gro_group_id         int,
   goods_name           varchar(255) not null,
   goods_starttime      varchar(255) not null,
   goods_period         varchar(255) not null,
   goods_specs          varchar(40) not null,
   goods_price          decimal(11) not null,
   goods_origination    varchar(255) not null,
   primary key (group_id)
);

/*==============================================================*/
/* Table: group                                                 */
/*==============================================================*/
create table group
(
   group_id             int not null,
   captain_id           int,
   goo_group_id         int,
   use_user_account     varchar(255),
   gro_user_account     varchar(255),
   gro_group_id         int,
   user_account         varchar(255) not null,
   group_description    varchar(255) not null,
   group_time           int not null,
   group_max_capacity   int not null,
   group_area_limit     int not null,
   group_type           int not null,
   group_totalRecommend int not null,
   group_totalComments  int not null,
   group_vedio          varchar(255),
   isFinish             tinyint not null,
   isSend               tinyint not null,
   group_reportCnt      int not null,
   group_deliveryway    int not null,
   primary key (group_id)
);

/*==============================================================*/
/* Table: group_order                                           */
/*==============================================================*/
create table group_order
(
   group_id             varchar(255) not null,
   order_id             int not null,
   use_user_account     varchar(255),
   user_account         varchar(255) not null,
   order_state          int not null,
   primary key (order_id, group_id)
);

/*==============================================================*/
/* Table: group_user                                            */
/*==============================================================*/
create table group_user
(
   group_id             int not null,
   user_account         varchar(255) not null,
   isPay                tinyint not null,
   isDelivery           tinyint not null,
   primary key (user_account, group_id)
);

/*==============================================================*/
/* Table: inform                                                */
/*==============================================================*/
create table inform
(
   user_account         varchar(255) not null,
   message_id           int not null,
   primary key (user_account, message_id)
);

/*==============================================================*/
/* Table: message                                               */
/*==============================================================*/
create table message
(
   message_id           int not null,
   user_account         varchar(255) not null,
   message_content      varchar(255) not null,
   message_time         varchar(255) not null,
   message_creator      varchar(255) not null,
   primary key (message_id)
);

/*==============================================================*/
/* Table: recommends                                            */
/*==============================================================*/
create table recommends
(
   group_id             int not null,
   recommends_id        int not null,
   use_user_account     varchar(255),
   gro_group_id         int,
   user_account         varchar(255) not null,
   primary key (group_id, recommends_id)
);

/*==============================================================*/
/* Table: relationship                                          */
/*==============================================================*/
create table relationship
(
   relationship_id      int not null,
   user_account1        varchar(255),
   user_account2        varchar(255),
   primary key (relationship_id)
);

/*==============================================================*/
/* Table: relationship2                                         */
/*==============================================================*/
create table relationship2
(
   user_account         varchar(255) not null,
   relationship_id      int not null,
   primary key (user_account, relationship_id)
);

/*==============================================================*/
/* Table: report                                                */
/*==============================================================*/
create table report
(
   report_id            int not null,
   group_id             int,
   com_group_id         int,
   comments_id          int,
   share_id             int,
   sComments_id         int,
   report_cause         varchar(255),
   report_time          varchar(255),
   report_type          int,
   report_state         int,
   primary key (report_id)
);

/*==============================================================*/
/* Table: sComments                                             */
/*==============================================================*/
create table sComments
(
   sComments_id         int not null,
   sha_share_id         int,
   use_user_account     varchar(255),
   user_account         varchar(255) not null,
   sComments_content    varchar(255) not null,
   sComments_time       varchar(255) not null,
   share_id             int not null,
   primary key (sComments_id)
);

/*==============================================================*/
/* Table: sTag                                                  */
/*==============================================================*/
create table sTag
(
   sTag_id              int not null,
   use_user_account     varchar(255) not null,
   sha_share_id         int,
   user_account         varchar(255),
   share_id             int,
   primary key (sTag_id)
);

/*==============================================================*/
/* Table: share                                                 */
/*==============================================================*/
create table share
(
   share_id             int not null,
   use_user_account     varchar(255),
   user_account         varchar(255) not null,
   share_content        varchar(255) not null,
   share_vedio          varchar(255),
   share_time           varchar(255) not null,
   share_commentCnt     int not null,
   share_tagCnt         int not null,
   share_reportCnt      int not null,
   primary key (share_id)
);

/*==============================================================*/
/* Table: tag                                                   */
/*==============================================================*/
create table tag
(
   tag_id               int not null,
   group_id             int,
   com_comments_id      int,
   use_user_account     varchar(255),
   comments_id          int,
   user_account         varchar(255),
   primary key (tag_id)
);

/*==============================================================*/
/* Table: user                                                  */
/*==============================================================*/
create table user
(
   user_account         varchar(255) not null,
   admin_id             int,
   captain_id           int,
   user_password        varchar(255) not null,
   user_nickname        varchar(255) not null,
   user_picture         varchar(255),
   user_location        varchar(255) not null,
   user_phone           varchar(255) not null,
   user_state           bool not null,
   user_repository      varchar(255),
   report_commentCnt    int,
   report_groupCn       int,
   report_shareCnt      int,
   primary key (user_account)
);

alter table admin add constraint FK_appoint foreign key (use_user_account)
      references user (user_account) on delete restrict on update restrict;

alter table captain add constraint FK_become foreign key (use_user_account)
      references user (user_account) on delete restrict on update restrict;

alter table collect add constraint FK_collectBelong foreign key (user_account)
      references user (user_account) on delete restrict on update restrict;

alter table collectGroup add constraint FK_collectGroup foreign key (group_id)
      references group (group_id) on delete restrict on update restrict;

alter table collectGroup add constraint FK_collectGroup2 foreign key (收藏ID)
      references collect (收藏ID) on delete restrict on update restrict;

alter table comments add constraint FK_commentsBelong foreign key (gro_group_id)
      references group (group_id) on delete restrict on update restrict;

alter table comments add constraint FK_createComment foreign key (use_user_account)
      references user (user_account) on delete restrict on update restrict;

alter table communicate add constraint FK_send foreign key (use_user_account)
      references user (user_account) on delete restrict on update restrict;

alter table communicate add constraint FK_sendIn foreign key (com_communication_room_id)
      references communication (communication_room_id) on delete restrict on update restrict;

alter table communicate2 add constraint FK_communicate foreign key (communication_room_id)
      references communication (communication_room_id) on delete restrict on update restrict;

alter table communicate2 add constraint FK_communicate2 foreign key (user_account)
      references user (user_account) on delete restrict on update restrict;

alter table complain add constraint FK_complain foreign key (use_user_account)
      references user (user_account) on delete restrict on update restrict;

alter table createOrder add constraint FK_createOrder foreign key (order_id, group_id)
      references group_order (order_id, group_id) on delete restrict on update restrict;

alter table createOrder add constraint FK_createOrder2 foreign key (gro_group_id)
      references group (group_id) on delete restrict on update restrict;

alter table goods add constraint FK_goodsBelong2 foreign key (gro_group_id)
      references group (group_id) on delete restrict on update restrict;

alter table group add constraint FK_create foreign key (use_user_account)
      references user (user_account) on delete restrict on update restrict;

alter table group add constraint FK_goodsBelong foreign key (goo_group_id)
      references goods (group_id) on delete restrict on update restrict;

alter table group add constraint FK_join foreign key (gro_user_account, gro_group_id)
      references group_user (user_account, group_id) on delete restrict on update restrict;

alter table group add constraint FK_manage foreign key (captain_id)
      references captain (captain_id) on delete restrict on update restrict;

alter table group_order add constraint FK_haveOrder foreign key (use_user_account)
      references user (user_account) on delete restrict on update restrict;

alter table inform add constraint FK_inform foreign key (user_account)
      references user (user_account) on delete restrict on update restrict;

alter table inform add constraint FK_inform2 foreign key (message_id)
      references message (message_id) on delete restrict on update restrict;

alter table recommends add constraint FK_createRecommend foreign key (use_user_account)
      references user (user_account) on delete restrict on update restrict;

alter table recommends add constraint FK_recommendBelong foreign key (gro_group_id)
      references group (group_id) on delete restrict on update restrict;

alter table relationship2 add constraint FK_relationship foreign key (user_account)
      references user (user_account) on delete restrict on update restrict;

alter table relationship2 add constraint FK_relationship2 foreign key (relationship_id)
      references relationship (relationship_id) on delete restrict on update restrict;

alter table report add constraint FK_reportComment foreign key (com_group_id, comments_id)
      references comments (group_id, comments_id) on delete restrict on update restrict;

alter table report add constraint FK_reportGroup foreign key (group_id)
      references group (group_id) on delete restrict on update restrict;

alter table report add constraint FK_reportScomment foreign key (sComments_id)
      references sComments (sComments_id) on delete restrict on update restrict;

alter table report add constraint FK_reportShare foreign key (share_id)
      references share (share_id) on delete restrict on update restrict;

alter table sComments add constraint FK_has foreign key (sha_share_id)
      references share (share_id) on delete restrict on update restrict;

alter table sComments add constraint FK_shareComment foreign key (use_user_account)
      references user (user_account) on delete restrict on update restrict;

alter table sTag add constraint FK_tag foreign key (use_user_account)
      references user (user_account) on delete restrict on update restrict;

alter table sTag add constraint FK_tagShare foreign key (sha_share_id)
      references share (share_id) on delete restrict on update restrict;

alter table share add constraint FK_shareShare foreign key (use_user_account)
      references user (user_account) on delete restrict on update restrict;

alter table tag add constraint FK_tagBelong foreign key (group_id, com_comments_id)
      references comments (group_id, comments_id) on delete restrict on update restrict;

alter table tag add constraint FK_tagComment foreign key (use_user_account)
      references user (user_account) on delete restrict on update restrict;

alter table user add constraint FK_appoint2 foreign key (admin_id)
      references admin (admin_id) on delete restrict on update restrict;

alter table user add constraint FK_become2 foreign key (captain_id)
      references captain (captain_id) on delete restrict on update restrict;

