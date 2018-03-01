
-----------从Gitee（码云）迁移过来-----------

**该项目利用Scrapy框架爬取了亚马逊网站的商品信息，需要爬取的内容分布在两个界面：首页和落地页**

在首页爬取的内容为：落地页的链接（link）和商品标识码（ASIN，由于网址组合原因，已经知道，不需要在落地页爬取）。

跳转到落地页之后，爬取的内容包括：标题（title）、品牌（brand）、价格（price）、星数（star）、评论人数（num）、排名（rank）、产品描述（description）、
上市时间（date）。

部分爬取内容显示如下：
![爬取信息1](https://github.com/lxm909055383/Amazon/blob/master/img/1.png)
![爬取信息2](https://github.com/lxm909055383/Amazon/blob/master/img/2.png)
