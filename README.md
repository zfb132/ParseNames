## 解析人名
基于Python3 环境编写代码，需要创建对应版本的虚拟环境并安装`pymysql`库  
修改配置文件的名字为`config.py`并改为自己的配置信息  
输入`python3 main.py`运行代码 
## 中文人名语料库
业余项目“萌名（一个基于语料库技术的取名工具）”的副产品。不定期更新。只删词，不加词。</br>
可用于中文分词、人名识别。

<strong>中文常见人名（Chinese_Names_Corpus）</strong></br>
120万。从亿级人名语料中提取。删除了罕见姓氏、和带生僻字的人名。随机删除了部分名人姓名（一点点小私心）。清洗后仍存有少量badcase。

<strong>中文古代人名（Ancient_Names_Corpus）</strong></br>
25万。多个人名词典汇总。删除了罕见姓氏、和带生僻字的人名。清洗后仍存有少量badcase。

<strong>日文人名（Japanese_Names_Corpus）</strong></br>
18万。从维基百科中提取。删除了罕见姓氏、和带生僻字的人名。清洗后仍存有少量badcase。</br>
数据清洗过程相见，“[日本人名数据清洗分享](https://github.com/wainshine/Chinese-Names-Corpus/issues/4)”。

<strong>翻译人名（English_Cn_Name_Corpus）</strong></br>
48万。多个人名词典汇总。删除了翻译人名常用字之外的人名。混有少量西化中文人名，如“李伯恩”。清洗后仍存有少量badcase，尤其是英文地名。

<strong>中文姓氏（Chinese_Family_Name）</strong></br>
1千。从亿级人名语料中提取。删除了罕见姓氏，复姓只保留了“欧阳”。

<strong>中文称呼（Chinese_Relationship）</strong></br>
5千。称呼词根。多个人名词典汇总。删除了部分带贬义的称呼。</br>
18万。中文称呼。多个人名词典汇总。清洗后仍存有大量badcase。

<strong>成语词典（ChengYu_Corpus）</strong></br>
5万。多个成语词典汇总。清洗后仍存有少量badcase。

---

<strong>更新时间：</strong>

更早的提交，不记得时间了。

删除了1000余非人名。 -2017.08.08

删除了5000余非人名。 -2017.11.25

新增了18万日文人名。 -2017.12.17

删除了1500余非人名（主要是日文地名）。 -2017.12.30

删除了约3万余非人名、或低频人名。 -2018.11.4

---

@萌名 整理

2018.11.04
