## 数据库介绍
`names.sql`是本项目的数据库文件，包含了所有的语料数据  
数据库名为`names`，包含了以下表：
- `chinese`：中文人名语料库1874887条记录（字段`nametype`表示人名类型，0-常见人名，1-古代人名，2-翻译人名）
- `english`：英文人名语料库29880条记录
- `idiom`：中文成语词典50528条记录
- `japanese`：日文人名语料库183963条记录

详细表结构如下：  
```txt
mysql> select
    ->   table_schema, table_name, engine, table_rows,
    ->   (data_length+index_length)/1024/1024 AS SIZE_MB
    -> FROM information_schema.tables WHERE table_schema = 'names';
+--------------+------------+--------+------------+-------------+
| TABLE_SCHEMA | TABLE_NAME | ENGINE | TABLE_ROWS | SIZE_MB     |
+--------------+------------+--------+------------+-------------+
| names        | chinese    | InnoDB |    1874887 | 73.59375000 |
| names        | english    | InnoDB |      29880 |  1.51562500 |
| names        | idiom      | InnoDB |      50528 |  2.51562500 |
| names        | japanese   | InnoDB |     183963 |  7.51562500 |
+--------------+------------+--------+------------+-------------+
4 rows in set (0.001 sec)

mysql> desc names.chinese;
+----------+-------------+------+-----+---------+----------------+
| Field    | Type        | Null | Key | Default | Extra          |
+----------+-------------+------+-----+---------+----------------+
| id       | int         | NO   | PRI | NULL    | auto_increment |
| content  | varchar(20) | YES  |     | NULL    |                |
| nametype | int         | YES  |     | NULL    |                |
+----------+-------------+------+-----+---------+----------------+
3 rows in set (0.001 sec)

mysql> desc names.english;
+---------+-------------+------+-----+---------+----------------+
| Field   | Type        | Null | Key | Default | Extra          |
+---------+-------------+------+-----+---------+----------------+
| id      | int         | NO   | PRI | NULL    | auto_increment |
| content | varchar(25) | YES  |     | NULL    |                |
+---------+-------------+------+-----+---------+----------------+
2 rows in set (0.001 sec)

mysql> desc names.idiom;
+---------+-------------+------+-----+---------+----------------+
| Field   | Type        | Null | Key | Default | Extra          |
+---------+-------------+------+-----+---------+----------------+
| id      | int         | NO   | PRI | NULL    | auto_increment |
| content | varchar(20) | YES  |     | NULL    |                |
+---------+-------------+------+-----+---------+----------------+
2 rows in set (0.001 sec)

mysql> desc names.english;
+---------+-------------+------+-----+---------+----------------+
| Field   | Type        | Null | Key | Default | Extra          |
+---------+-------------+------+-----+---------+----------------+
| id      | int         | NO   | PRI | NULL    | auto_increment |
| content | varchar(25) | YES  |     | NULL    |                |
+---------+-------------+------+-----+---------+----------------+
2 rows in set (0.001 sec)

mysql> desc names.japanese;
+---------+-------------+------+-----+---------+----------------+
| Field   | Type        | Null | Key | Default | Extra          |
+---------+-------------+------+-----+---------+----------------+
| id      | int         | NO   | PRI | NULL    | auto_increment |
| content | varchar(20) | YES  |     | NULL    |                |
+---------+-------------+------+-----+---------+----------------+
2 rows in set (0.001 sec)
```

## 解析人名
基于Python3 环境编写代码，需要创建对应版本的虚拟环境并安装`pymysql`库  
修改配置文件的名字为`config.py`并改为自己的配置信息  
输入`python3 main.py`运行代码即可把数据导入到数据库中

# 中文人名语料库（Chinese-Names-Corpus）
业余项目“萌名NameMoe（一个基于语料库技术的取名工具）”的副产品。

不定期更新。只删词，不加词。

可用于中文分词、人名识别。

---

<strong>请勿将本库打包上传其他网站挣积分，已上传的请配合删除，谢谢！</strong>

---

<strong>中文常见人名（Chinese_Names_Corpus）</strong>

数据大小：120万。

语料来源：从亿级人名语料中提取。

数据清洗：已清洗，但仍存有少量badcase。

新增性别标注。

---

<strong>中文古代人名（Ancient_Names_Corpus）</strong>

数据大小：25万。

语料来源：多个人名词典汇总。

数据清洗：已清洗。

---

<strong>中文姓氏（Chinese_Family_Name）</strong>

数据大小：1千。

语料来源：从亿级人名语料中提取。

数据清洗：已清洗。

---

<strong>中文称呼（Chinese_Relationship）</strong>

数据大小：5千，称呼词根；18万，中文称呼。

语料来源：多个人名词典汇总。

数据清洗：已清洗，但仍存有大量badcase。

---

# 英文人名语料库（English-Names-Corpus）
<strong>翻译人名（English_Cn_Name_Corpus）</strong>

数据大小：48万。

语料来源：多个人名词典汇总。

数据清洗：已清洗，但仍存有少量badcase，以地名居多。

本语料的人名识别由网友 “[ltccss](https://github.com/ltccss)” 友情提供。

---

# 日文人名语料库（Japanese_Names_Corpus）
<strong>日文人名（Japanese_Names_Corpus）</strong>

数据大小：18万。

数据来源：从维基百科中提取。

数据清洗：已清洗，但仍存有少量badcase。

数据清洗过程详见：“[日本人名数据清洗分享](https://github.com/wainshine/Chinese-Names-Corpus/issues/4)”。

---

# 中文词典语料库（Chinese_Dict_Corpus）
<strong>成语词典（ChengYu_Corpus）</strong>

数据大小：5万。

语料来源：多个成语词典汇总。

数据清洗：已清洗。

---

# 提醒与备注
<strong>请勿提交涉政issue：</strong>

惹不起呀，谢谢～

语料中还存有的，会在后续的更新中逐步删除掉。

---

<strong>更新时间：</strong>

更早的提交，不记得时间了。

删除了1000余非人名。 -2017.08.08

删除了5000余非人名。 -2017.11.25

新增了18万日文人名。 -2017.12.17

删除了1500余非人名（主要是日文地名）。 -2017.12.30

删除了约3万余非人名、或低频人名。 -2018.11.04

删除了2600余非人名、或低频人名。 -2019.04.15

删除了约1万余非人名、或低频人名。 -2019.07.27

将文件移动到文件夹。 -2019.10.21

---

@萌名NameMoe 整理

2019.10.21
