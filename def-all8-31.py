#encoding:UTF-8
import datetime 
import time
import requests #__version__ = 2.3.0 这里直接使用session，因为要先登陆 
from bs4 import BeautifulSoup #__version__ = 4.3.2
from lxml import etree
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
s=requests.session()
from pymongo import MongoClient
mc=MongoClient("localhost",27017)
db=mc.test0
from multiprocessing.dummy import Pool as ThreadPool
#print ArticleTitle,ArticlePubTime,ArticleFrom
def pd():
    spidertime=time.strftime('%m%d-%H%M', time.localtime())
    num1 = ArticleBody.count("融360")
    num2 = ArticleBody.count("网贷之家")
    num3 = ArticleBody.count("网贷天眼")
    num4 = ArticleBody.count("金评媒")
    num5 = ArticleBody.count("零壹财经")
    num6 = ArticleBody.count("的")
    if ("融360" in ArticleTitle.encode('utf-8')):
        haspoint = "yes"
    else:
        haspoint = "no"
    print "网贷之家"+str(num2)
    #print "haspoint"+haspoint,"ArticleTitle"+ArticleTitle,"好"+str(num1)
    db.test1.save(
        #{"haspoint": haspoint,"ArticleTitle":ArticleTitle,"spidertime":spidertime, "num": num}
        {"spidertime":spidertime,"媒体":MediaFrom,"haspoint":haspoint,"ArticleTitle":ArticleTitle,
        "ArticlePubTime":ArticlePubTime,"ArticleFrom":ArticleFrom,"link":link,"融360":num1,"网贷之家":num2,"网贷天眼":num3,"金评媒":num4,"零壹财经":num5,"的":num6}
    )
        #"ArticlePubTime":ArticlePubTime,"ArticleFrom":ArticleFrom,"link":link
    #return num

#和讯银行
def pq817():
    r = s.get('http://bank.hexun.com') #该页面进行登录，先获取一些信息
    bs = BeautifulSoup(r.content).find("div",attrs={"class":"part-l"}).find_all('a')
    n =range(0)
    global ArticlePubTime
    global ArticleFrom
    global ArticleTitle
    global link
    global ArticleBody
    global MediaFrom
    for i in bs:

        link=(i.get('href')).strip()
        title=(i.get_text())
        #print title
        #print link
        #print len(link)
        l=s.get(link)
        if BeautifulSoup(l.content).find("div",attrs={"class":"art_context"}) is None:
            continue
        else:   
            ArticleTitle=BeautifulSoup(l.content).find("div",attrs={"class":"layout mg articleName"}).find('h1').get_text()
            ArticlePubTime=BeautifulSoup(l.content).find("div",attrs={"class":"tip fl"}).find('span').get_text().strip()
            if BeautifulSoup(l.content).find("div",attrs={"class":"tip fl"}).find("a") is None:
    #先把span的text都取下来成列表，然后在分开取第二个值 bingo            
                ArticleFrom=BeautifulSoup(l.content).find("div",attrs={"class":"tip fl"}).get_text("|", strip=True)
                ArticleFrom=ArticleFrom.split("|")[1]
            else:
                ArticleFrom=BeautifulSoup(l.content).find("div",class_="tip fl").find("a").get_text().strip()
            global ArticleBody
            ArticleBody=BeautifulSoup(l.content).find("div",attrs={"class":"art_context"}).get_text().strip()

         #   str(n.append(i["href"])) +

            #for link in content:
            #    print (link.get('href')),(link.get_text())
            print ArticlePubTime
            print ArticleFrom
            MediaFrom="和讯银行"
            pd()
#和讯新闻
def pq816():
    global ArticlePubTime
    global ArticleFrom
    global ArticleTitle
    global ArticleBody
    global link
    global MediaFrom
    r = s.get('http://news.hexun.com/') #该页面进行登录，先获取一些信息
    bs = BeautifulSoup(r.content).find("div",attrs={"class":"l"}).find_all('a')
    n =range(0)
    for i in bs:
        link=(i.get('href')).strip()
        title=(i.get_text())
        print title
        print link
        #print len(link)
        l=s.get(link)
        if BeautifulSoup(l.content).find("div",attrs={"class":"art_context"}) is None:
            continue
        else:
            ArticleTitle=BeautifulSoup(l.content).find("div",attrs={"class":"layout mg articleName"}).find('h1').get_text()
            ArticlePubTime=BeautifulSoup(l.content).find("div",class_="tip fl").find('span').get_text()
            #ArticleFrom=BeautifulSoup(l.content).find("div",class_="tip fl").find('a').get_text()
            ArticleFrom=BeautifulSoup(l.content).find("div",class_="tip fl").get_text("$",strip=True).split("$")[1]
            ArticleBody=BeautifulSoup(l.content).find("div",attrs={"class":"art_context"}).get_text().strip()
            MediaFrom="和讯新闻"
            pd()
#和讯理财
def pq814():
    global ArticlePubTime
    global ArticleFrom
    global ArticleTitle
    global ArticleBody
    global link
    global MediaFrom
    r = s.get('http://money.hexun.com/') #该页面进行登录，先获取一些信息
    bs1=BeautifulSoup(r.content).find("div",attrs={"id":"news"}).find_all('a')
    bs2 = BeautifulSoup(r.content).find("div",attrs={"id":"tab01_con1"}).find_all('a')
    bs=bs1+bs2

    for i in bs:
        if len(i.get_text().strip())==0:
            continue
        else:
            link=(i.get('href')).strip()
            title=(i.get_text())
            #print link,title
            l=s.get(link)
            if BeautifulSoup(l.content).find("div",attrs={"class":"art_context"}) is None:
                continue
            else:
                ArticleTitle=BeautifulSoup(l.content).find("div",attrs={"class":"layout mg articleName"}).find('h1').get_text()
                ArticlePubTime=BeautifulSoup(l.content).find("div",class_="tip fl").find('span').get_text()
                #ArticleFrom=BeautifulSoup(l.content).find("div",class_="tip fl").find('a').get_text()
                ArticleFrom=BeautifulSoup(l.content).find("div",class_="tip fl").get_text("$",strip=True).split("$")[1]
                ArticleBody=BeautifulSoup(l.content).find("div",attrs={"class":"art_context"}).get_text().strip()
                MediaFrom="和讯理财"
                pd()
                
#和讯房产 分地域不要了
#和讯首页
def pq705():
    global ArticlePubTime
    global ArticleFrom
    global ArticleTitle
    global ArticleBody
    global link
    global MediaFrom
    r = s.get('http://www.hexun.com/') #该页面进行登录，先获取一些信息
    bs=BeautifulSoup(r.content).find("ul",attrs={"sizset":"54"}).find_all('a')
    for i in bs:
        if len(i.get_text().strip())==0:
            continue
        else:
            link=(i.get('href')).strip()
            title=(i.get_text())
            #print link,title
            l=s.get(link)
            if BeautifulSoup(l.content).find("div",attrs={"class":"art_context"}) is None:
                continue
            else:
                ArticleTitle=BeautifulSoup(l.content).find("div",attrs={"class":"layout mg articleName"}).find('h1').get_text()
                ArticlePubTime=BeautifulSoup(l.content).find("div",class_="tip fl").find('span').get_text()
                #ArticleFrom=BeautifulSoup(l.content).find("div",class_="tip fl").find('a').get_text()
                ArticleFrom=BeautifulSoup(l.content).find("div",class_="tip fl").get_text("$",strip=True).split("$")[1]
                ArticleBody=BeautifulSoup(l.content).find("div",attrs={"class":"art_context"}).get_text().strip()
                MediaFrom="和讯首页"
                print ArticleTitle,ArticlePubTime,ArticleFrom
                pd()
   

#凤凰财经
def pq201():
    global MediaFrom
    global ArticlePubTime
    global ArticleFrom
    global ArticleTitle
    global ArticleBody
    global link  
    MediaFrom="凤凰财经"
    #links=[]
    r = s.get('http://finance.ifeng.com').content
    html=etree.HTML(r)
    bs1=html.xpath("//div[@class='box_01']/div/div/h2/a")
    bs2=html.xpath("//div[@class='box_01']/div/div/ul/li/a")
    bs3=html.xpath("//div[@class='box_02']/ul/li/strong/a")
    bs4=html.xpath("//div[@class='box_02']/ul/li/a")
    bs=bs1+bs2+bs3+bs4
    for i in bs:
        link="".join(i.xpath("@href")).strip().replace("hhttp","http")
        #links.append(link)
        print link
       
        title="".join(i.xpath('text()')).strip()
        #print link,title
        l=s.get(link).content
        htm=etree.HTML(l)
        #if len("".join(htm.xpath("//span[@itemprop='publisher']/span/text()")))==0:
        #    continue
        #else:
        
        if len("".join(htm.xpath("//span[@itemprop='datePublished']/text()")).strip())>0:
            ArticleTitle="".join(htm.xpath("//h1[@id='artical_topic']/text()"))
            ArticleFrom="".join(htm.xpath("//span[@itemprop='publisher']/span/text()"))
            if len(ArticleFrom)==0:
                ArticleFrom="".join(htm.xpath("//span[@itemprop='publisher']/span/a/text()"))
            ArticlePubTime="".join(htm.xpath("//span[@itemprop='datePublished']/text()"))
            ArticleBody="".join(htm.xpath("//div[@id='main_content']//text()"))
            if len(ArticleBody)==0:
                ArticleBody="".join(htm.xpath("//div[@id='artical_sth2']//text()"))
            pd()
#凤凰理财
def pq302():
    global MediaFrom
    global ArticlePubTime
    global ArticleFrom
    global ArticleTitle
    global ArticleBody
    global link 
    MediaFrom="凤凰理财"
    #links=[]
    r = s.get('http://finance.ifeng.com/money').content
    html=etree.HTML(r)
    bs1=html.xpath("//div[@class='box_01']/h2/a")
    bs2=html.xpath("//div[@class='box_01']/div/h3/a")
    bs3=html.xpath("//div[@class='b_box']/div/div/div[2]/h3/a")
    bs4=html.xpath("//div[@class='b_box']/div/ul/li/a")
    bs=bs1+bs2+bs3+bs4
    for i in bs:
        link="".join(i.xpath("@href")).strip()
        title="".join(i.xpath('text()')).strip()
        l=s.get(link).content
        htm=etree.HTML(l)
        #if len("".join(htm.xpath("//span[@itemprop='publisher']/span/text()")))==0:
        #    continue
        #else:
        
        if len("".join(htm.xpath("//span[@itemprop='datePublished']/text()")).strip())>0:
            ArticleTitle="".join(htm.xpath("//h1[@id='artical_topic']/text()"))
            ArticleFrom="".join(htm.xpath("//span[@itemprop='publisher']/span/text()"))
            if len(ArticleFrom)==0:
                ArticleFrom="".join(htm.xpath("//span[@itemprop='publisher']/span/a/text()"))
            ArticlePubTime="".join(htm.xpath("//span[@itemprop='datePublished']/text()"))
            ArticleBody="".join(htm.xpath("//div[@id='main_content']//text()"))
            if len(ArticleBody)==0:
                ArticleBody="".join(htm.xpath("//div[@id='artical_sth2']//text()"))
            pd()


#搜狐财经
def pq202():
    global MediaFrom
    global ArticlePubTime
    global ArticleFrom
    global ArticleTitle
    global ArticleBody
    global link
    MediaFrom="搜狐财经"
    links=[]
    r = s.get('http://business.sohu.com').content
    html=etree.HTML(r)
    bs=html.xpath("//div[@id='myTab1_Content0']//a[@target='_blank']")
    for i in bs:
        link="".join(i.xpath("@href")).strip()
        title="".join(i.xpath('text()')).strip()
        print link,title
        
        l=s.get(link).content
        htm=etree.HTML(l)        
        ArticleTitle="".join(htm.xpath("//h1/text()"))
        ArticleFrom="".join(htm.xpath("//span[@id='media_span']/span/text()"))
        if ArticleFrom=="":
            ArticleFrom="".join(htm.xpath("//span[@class='writer']/a/text()"))
        ArticlePubTime="".join(htm.xpath("//div[@id='pubtime_baidu']/text()"))
        if ArticlePubTime=="":
            ArticlePubTime="".join(htm.xpath("//span[@id='pubtime_baidu']/text()"))
        ArticleBody="".join(htm.xpath("//div[@id='contentText']//text()"))
        pd()
#搜狐理财
def pq304():
    global MediaFrom
    global ArticlePubTime
    global ArticleFrom
    global ArticleTitle
    global ArticleBody
    global link
    MediaFrom="搜狐理财"
    links=[]
    r = s.get('http://money.sohu.com').content
    html=etree.HTML(r)
    bs1=html.xpath("//div[@class='newscont']//a[@class='h1']")
    bs2=html.xpath("//div[@class='newscont']//a[@class='h2']")
    bs=bs1+bs2
    #print bs
    
    for i in bs:
        link="".join(i.xpath("@href")).strip()
        title="".join(i.xpath('text()')).strip()
        print link,title
        
        l=s.get(link).content
        htm=etree.HTML(l)        
        ArticleTitle="".join(htm.xpath("//h1/text()"))
        ArticleFrom="".join(htm.xpath("//span[@id='media_span']/span/text()"))
        if ArticleFrom=="":
            ArticleFrom="".join(htm.xpath("//span[@class='writer']/a/text()"))
        ArticlePubTime="".join(htm.xpath("//div[@id='pubtime_baidu']/text()"))
        if ArticlePubTime=="":
            ArticlePubTime="".join(htm.xpath("//span[@id='pubtime_baidu']/text()"))
        ArticleBody="".join(htm.xpath("//div[@id='contentText']//text()"))
        pd()




#腾讯财经  ！！！不包括stock的文章（因为body源文件有点奇怪）
def pq203():
    global ArticlePubTime
    global ArticleFrom
    global ArticleTitle
    global ArticleBody
    global link 
    global MediaFrom
    MediaFrom="腾讯财经"
    links=[]
    r = s.get('http://finance.qq.com').content
    html=etree.HTML(r)
    bs=html.xpath("//div[@class='list yaowen']/div[2]/div[2]/div[1]/div/ul/li[@class='item one']/a")
    for i in bs:
        link="".join(i.get("href")).strip()
        l=s.get(link).content
        #print link
        htm=etree.HTML(l)


        ArticleTitle="".join(htm.xpath("//h1/text()")).strip()
        if len(ArticleTitle)==0:
            ArticleTitle="".join(htm.xpath("//h1/text()")).strip()
        #print link,ArticleTitle
        
        ArticleFrom="".join(htm.xpath("//span[@bosszone='jgname']/text()")).strip()
        if len(ArticleFrom)==0:
            ArticleFrom="".join(htm.xpath("//span[@bosszone='jgname']/a/text()")).strip()
        ArticlePubTime="".join(htm.xpath("//span[@class='pubTime article-time']/text()")).strip()
        if len(ArticlePubTime)==0:
            ArticlePubTime="".join(htm.xpath("//span[@class='a_time']/text()")).strip()
        ArticleBody="".join(htm.xpath("//div[@bosszone='content']//text()")).strip()
        #print link
        if len(ArticleFrom)!=0:
            pd()
#腾讯理财
def pq306():
    global ArticlePubTime
    global ArticleFrom
    global ArticleTitle
    global ArticleBody
    global link 
    global MediaFrom
    MediaFrom="腾讯理财"
    links=[]
    r = s.get('http://money.qq.com').content
    html=etree.HTML(r)
    bs1=html.xpath("//div[@class='first']/ul/li/a")
    bs2=html.xpath("//div[@class='sst second']/div/div/div/em/a")
    bs=bs1+bs2
    for i in bs:
        link="".join(i.get("href")).strip()
        #title="".join(i.get_text())
        l=s.get(link).content
        print link
        htm=etree.HTML(l)
        ArticleTitle="".join(htm.xpath("//h1/text()")).strip()
        if len(ArticleTitle)==0:
            ArticleTitle="".join(htm.xpath("//h1/text()")).strip()
        #print link,ArticleTitle
        
        ArticleFrom="".join(htm.xpath("//span[@bosszone='jgname']/text()")).strip()
        if len(ArticleFrom)==0:
            ArticleFrom="".join(htm.xpath("//span[@bosszone='jgname']/a/text()")).strip()
        ArticlePubTime="".join(htm.xpath("//span[@class='pubTime article-time']/text()")).strip()
        if len(ArticlePubTime)==0:
            ArticlePubTime="".join(htm.xpath("//span[@class='a_time']/text()")).strip()
        ArticleBody="".join(htm.xpath("//div[@bosszone='content']//text()")).strip()
        print ArticleBody,ArticlePubTime
        #print ArticleTitle,ArticlePubTime,ArticleFrom
        if len(ArticleFrom.strip())!=0:
            pd()




#网易财经
def pq204():
    global MediaFrom
    global ArticlePubTime
    global ArticleFrom
    global ArticleTitle
    global ArticleBody
    global link
    MediaFrom="网易财经"
    links=[]
    r = s.get('http://money.163.com').content
    html=etree.HTML(r)
    bs1=html.xpath("//div[@class='topnews_first']/h2/a")
    bs2=html.xpath("//ul[@class='topnews_tag_list']/li/a")
    bs3=html.xpath("//ul[@class='topnews_list mb20']/li/a")
    bs=bs1+bs2+bs3
    #print bs
    for i in bs:
        #print i
        if len("".join(i.xpath('@href')).strip())>0:
            link="".join(i.xpath('@href')).strip()
            title="".join(i.xpath('text()')).strip()
            print link,title
            l=s.get(link).content
            htm=etree.HTML(l)
            ArticleTitle="".join(htm.xpath("//h1/text()")).strip()
            ArticleFrom="".join(htm.xpath("//div[@class='post_time_source']/a/text()")).strip()
            if len(ArticleFrom)==0:
                ArticleFrom="".join(htm.xpath("//div[@class='au_source']/text()")).strip()
            ArticlePubTime="".join(htm.xpath("//div[@class='post_time_source']/text()")).strip()
            if len(ArticlePubTime)==0:
                ArticlePubTime="".join(htm.xpath("//div[@class='vol_num']/p/text()")).strip()
            ArticleBody="".join(htm.xpath("//div[@class='para_main']//text()")).strip()
            if len(ArticleBody)==0:
                ArticleBody="".join(htm.xpath("//div[@class='post_text']//text()")).strip()
            #print link,ArticleTitle,ArticlePubTime,ArticleFrom
            if len(ArticleFrom) != 0:
                pd()
              
#网易理财
def pq308():
    global MediaFrom
    global ArticlePubTime
    global ArticleFrom
    global ArticleTitle
    global ArticleBody
    global link
    MediaFrom="网易理财"
    links=[]
    r = s.get('http://money.163.com/licai').content
    html=etree.HTML(r)
    bs1=html.xpath("//div[@class='fn_focus_news']/h2/a")
    bs2=html.xpath("//div[@class='fn_focus_news']/ul/li/a")
    bs=bs1+bs2
    #print bs
    for i in bs:
        #print i
        if len("".join(i.xpath('@href')).strip())>0:
            link="".join(i.xpath('@href')).strip()
            title="".join(i.xpath('text()')).strip()
            #print link,title
            l=s.get(link).content
            htm=etree.HTML(l)
            ArticleTitle="".join(htm.xpath("//h1/text()")).strip()
            ArticleFrom="".join(htm.xpath("//div[@class='post_time_source']/a/text()")).strip()
            if len(ArticleFrom)==0:
                ArticleFrom="".join(htm.xpath("//div[@class='au_source']/text()")).strip()
            ArticlePubTime="".join(htm.xpath("//div[@class='post_time_source']/text()")).strip()
            if len(ArticlePubTime)==0:
                ArticlePubTime="".join(htm.xpath("//div[@class='vol_num']/p/text()")).strip()
            ArticleBody="".join(htm.xpath("//div[@class='para_main']//text()")).strip()
            if len(ArticleBody)==0:
                ArticleBody="".join(htm.xpath("//div[@class='post_text']//text()")).strip()
            print link,ArticleTitle#,ArticlePubTime,ArticleFrom
            pd()


#新浪财经
def pq205():
    global ArticlePubTime
    global ArticleFrom
    global ArticleTitle
    global ArticleBody
    global link  
    global MediaFrom
    MediaFrom="新浪财经"
    
    r = s.get('http://finance.sina.com.cn').content
    html=etree.HTML(r)
    bs1=html.xpath("//div[@id='blk_hdline_01']//h3//a")
    bs2=html.xpath("//div[@id='blk_hdline_01']//p//a")
    bs3=html.xpath("//div[@id='fin_tabs0_c0']/div[2]//ul//li//a")
    bs=bs1+bs2+bs3
    for i in bs:
        link="".join(i.xpath("@href")).strip()
        title="".join(i.xpath("text()")).strip()
        #links.append(link)
        l=s.get(link).content
        print link,title
        htm=etree.HTML(l)
        if "".join(htm.xpath("//h1/text()"))=="":
            continue
        else:
            ArticleTitle="".join(htm.xpath("//h1/text()"))

            ArticlePubTime="".join(htm.xpath("//span[@class='time-source']/text()")).strip().replace("\n","").split(" ")[0]
            if len(ArticlePubTime)==0:
                ArticlePubTime="".join(htm.xpath("//span[@id='pub_date']/text()")).strip()
                print ArticlePubTime

            ArticleFrom="".join(htm.xpath("//div[@class='page-info']/span/span/a/text()"))
            if len(ArticleFrom)==0:
                ArticleFrom="".join(htm.xpath("//span[@id='media_name']/text()")).strip()
                if len(ArticleFrom)==0:
                    ArticleFrom="".join(htm.xpath("//span[@class='time-source']/text()")).strip().replace("\n","").replace(" ","")
                    if len(ArticleFrom)==0:
                        ArticleFrom="专栏"

            ArticleBody="".join(htm.xpath("//div[@id='artibody']//text()"))
            
            if len(ArticleBody)!=0:
                pd()

#新浪理财
def pq309():
    global ArticlePubTime
    global ArticleFrom
    global ArticleTitle
    global ArticleBody
    global link  
    global MediaFrom
    MediaFrom="新浪理财"
    
    r = s.get('http://finance.sina.com.cn/money/').content
    html=etree.HTML(r)
    bs1=html.xpath("//div[@id='subShowContent1_news1']/div/div/div/h2/a")
    bs2=html.xpath("//div[@id='subShowContent1_news2']/div/div/div/h2/a")
    bs3=html.xpath("//div[@id='subShowContent1_news3']/div/div/div/h2/a")
    bs4=html.xpath("//div[@id='subShowContent1_news4']/div/div/div/h2/a")
    bs=bs1+bs2+bs3+bs4
    for i in bs:
        link="".join(i.xpath("@href")).strip()
        title="".join(i.xpath("text()")).strip()
        #print link,title
        l=s.get(link).content
        print link,title
        htm=etree.HTML(l)
        ArticleTitle="".join(htm.xpath("//h1/text()"))

        ArticlePubTime="".join(htm.xpath("//span[@class='time-source']/text()")).strip().replace("\n","").split(" ")[0]
        if len(ArticlePubTime)==0:
            ArticlePubTime="".join(htm.xpath("//span[@id='pub_date']/text()")).strip()
            print ArticlePubTime

        ArticleFrom="".join(htm.xpath("//div[@class='page-info']/span/span/a/text()"))
        if len(ArticleFrom)==0:
            ArticleFrom="".join(htm.xpath("//span[@id='media_name']/text()")).strip()
            if len(ArticleFrom)==0:
                ArticleFrom="".join(htm.xpath("//span[@class='time-source']/text()")).strip().replace("\n","")
                if len(ArticleFrom)==0:
                    ArticleFrom="专栏"

        ArticleBody="".join(htm.xpath("//div[@id='artibody']//text()"))
        
        if len(ArticleBody)!=0:
            pd()


#东方财富网
def pq703():
    global ArticlePubTime
    global ArticleFrom
    global ArticleTitle
    global ArticleBody
    global link
    global MediaFrom
    r = s.get('http://www.eastmoney.com/') #该页面进行登录，先获取一些信息
    bs1=BeautifulSoup(r.content).find("div",class_="nmlist").find_all("a")
    bs2=BeautifulSoup(r.content).find("div",class_="nlist newsbbh1").find_all("a")
    bs=bs1+bs2
    for i in bs:
        link=i.get('href').strip()
        title=i.get_text().strip()
        #print title,link
        l=s.get(link)
        if BeautifulSoup(l.content).find("div",attrs={"class":"newsContent"}) is None:
            print link
            print u'这个是非文章url'
        else:
            ArticleTitle=BeautifulSoup(l.content).find('h1').get_text()
            #print link
            if BeautifulSoup(l.content).find("div",attrs={"class":"Info"}).find("div",class_="time") is None:
                ArticlePubTime=BeautifulSoup(l.content).find("div",attrs={"class":"Info"}).find("span").get_text().strip()
            else:
                ArticlePubTime=BeautifulSoup(l.content).find("div",attrs={"class":"Info"}).find("div",class_="time").get_text().strip()


            ArticleBody=BeautifulSoup(l.content).find("div",attrs={"id":"ContentBody"}).get_text().strip()
            link0="http://iguba.eastmoney.com/interf/reply.aspx?callback=jQuery183049486440794946285_1468306257505&action=infocode2topicid&infocode="
            link1=str(link0)+link.split(",")[1].split(".")[0]+u"&type=1&_=1468306257515"
            n=s.get(link1)
            
            d=eval(n.content.split("[")[1].split("]")[0]) #ArticleFrom
            cod=d['stockbar_code']
            po=d['post_id']
            link2=u'http://guba.eastmoney.com/news,' + str(cod) + u','+str(po) + u'.html'
            m=s.get(link2)
            if BeautifulSoup(m.content).find("div",attrs={"id":'zw_header'}) is None:
                ArticleFrom=u'东方财富网'
            else:
                ArticleFrom=BeautifulSoup(m.content).find("div",attrs={"id":'zw_header'}).get_text().strip()
            MediaFrom="东方财富网"
            #print ArticleTitle,ArticlePubTime,ArticleFrom
            pd()


#东方财富网--财经
def pq807():
    global ArticlePubTime
    global ArticleFrom
    global ArticleTitle
    global ArticleBody
    global link
    global MediaFrom
    r = s.get('http://finance.eastmoney.com/') #该页面进行登录，先获取一些信息
    bs = BeautifulSoup(r.content).find("div",attrs={"class":"importantNews"}).find_all('a')
    

    for i in bs:
        link=i.get('href').strip()
        title=i.get_text().strip()
        

    #n =s.get('http://iguba.eastmoney.com/interf/reply.aspx?callback=jQuery183049486440794946285_1468306257505&action=infocode2topicid&infocode=20160718648487086&type=1&_=1468306257515')
    #print n.content
        l=s.get(link)
        if BeautifulSoup(l.content).find("div",attrs={"class":"newsContent"}) is None:
            print link
            print u'这个是非文章url'
        else:
            ArticleTitle=BeautifulSoup(l.content).find('h1').get_text()
            #print link
            if BeautifulSoup(l.content).find("div",attrs={"class":"Info"}).find("div",class_="time") is None:
                ArticlePubTime=BeautifulSoup(l.content).find("div",attrs={"class":"Info"}).find("span").get_text().strip()
            else:
                ArticlePubTime=BeautifulSoup(l.content).find("div",attrs={"class":"Info"}).find("div",class_="time").get_text().strip()


            ArticleBody=BeautifulSoup(l.content).find("div",attrs={"id":"ContentBody"}).get_text().strip()
            link0="http://iguba.eastmoney.com/interf/reply.aspx?callback=jQuery183049486440794946285_1468306257505&action=infocode2topicid&infocode="
            link1=str(link0)+link.split(",")[1].split(".")[0]+u"&type=1&_=1468306257515"
            n=s.get(link1)
            
            d=eval(n.content.split("[")[1].split("]")[0]) #ArticleFrom
            cod=d['stockbar_code']
            po=d['post_id']
            link2=u'http://guba.eastmoney.com/news,' + str(cod) + u','+str(po) + u'.html'
            m=s.get(link2)
            if BeautifulSoup(m.content).find("div",attrs={"id":'zw_header'}) is None:
                ArticleFrom=u'东方财富网'
            else:
                ArticleFrom=BeautifulSoup(m.content).find("div",attrs={"id":'zw_header'}).get_text().strip()
            MediaFrom="东方财富网--财经"
            pd()

#东方财富网--理财
def pq808():
    global ArticlePubTime
    global ArticleFrom
    global ArticleTitle
    global ArticleBody
    global link
    global MediaFrom
    s = requests.session() #创建一个session对象
    r = s.get('http://money.eastmoney.com') #该页面进行登录，先获取一些信息
    bs = BeautifulSoup(r.content).find("div",attrs={"class":"column colspan-2"}).find_all('a')


    for i in bs:
        link=(i.get('href')).strip()
        title=(i.get_text())
        print title
    #    print link
    #    print len(link)

    #n =s.get('http://iguba.eastmoney.com/interf/reply.aspx?callback=jQuery183049486440794946285_1468306257505&action=infocode2topicid&infocode=20160718648487086&type=1&_=1468306257515')
    #print n.content
        l=s.get(link)
        if BeautifulSoup(l.content).find("div",attrs={"class":"newsContent"}) is None:
            print link
            print u'这个是非文章url'
        else:
            ArticleTitle=BeautifulSoup(l.content).find('h1').get_text()
            #print link
            if BeautifulSoup(l.content).find("div",attrs={"class":"Info"}).find("div",class_="time") is None:
                ArticlePubTime=BeautifulSoup(l.content).find("div",attrs={"class":"Info"}).find("span").get_text().strip()
            else:
                ArticlePubTime=BeautifulSoup(l.content).find("div",attrs={"class":"Info"}).find("div",class_="time").get_text().strip()


            ArticleBody=BeautifulSoup(l.content).find("div",attrs={"id":"ContentBody"}).get_text().strip()
            link0="http://iguba.eastmoney.com/interf/reply.aspx?callback=jQuery183049486440794946285_1468306257505&action=infocode2topicid&infocode="
            link1=str(link0)+link.split(",")[1].split(".")[0]+u"&type=1&_=1468306257515"
            n=s.get(link1)
            
            d=eval(n.content.split("[")[1].split("]")[0]) #ArticleFrom
            cod=d['stockbar_code']
            po=d['post_id']
            link2=u'http://guba.eastmoney.com/news,' + str(cod) + u','+str(po) + u'.html'
            m=s.get(link2)
            if BeautifulSoup(m.content).find("div",attrs={"id":'zw_header'}) is None:
                ArticleFrom=u'东方财富网'
            else:
                ArticleFrom=BeautifulSoup(m.content).find("div",attrs={"id":'zw_header'}).get_text().strip()
            MediaFrom="东方财富网--理财"
            pd()


#东方财富网--银行
def pq809():
    global ArticlePubTime
    global ArticleFrom
    global ArticleTitle
    global ArticleBody
    global link
    global MediaFrom
    r = s.get('http://bank.eastmoney.com') #该页面进行登录，先获取一些信息
    bs1 = BeautifulSoup(r.content).find("div",attrs={"class":"mainBull"}).find_all("a")
    bs2 = BeautifulSoup(r.content).find("div",attrs={"id":"News_yhdd"}).find_all("a")
    bs=bs1+bs2#bs.extend(bs2)

    for i in bs:
        link=(i.get('href')).strip()
        title=(i.get_text()).strip()
        print title

    #n =s.get('http://iguba.eastmoney.com/interf/reply.aspx?callback=jQuery183049486440794946285_1468306257505&action=infocode2topicid&infocode=20160718648487086&type=1&_=1468306257515')
    #print n.content
        l=s.get(link)
        if BeautifulSoup(l.content).find("div",attrs={"class":"newsContent"}) is None:
            print link
            print u'这个是非文章url'
        else:
            ArticleTitle=BeautifulSoup(l.content).find('h1').get_text()
            #print link
            if BeautifulSoup(l.content).find("div",attrs={"class":"Info"}).find("div",class_="time") is None:
                ArticlePubTime=BeautifulSoup(l.content).find("div",attrs={"class":"Info"}).find("span").get_text().strip()
            else:
                ArticlePubTime=BeautifulSoup(l.content).find("div",attrs={"class":"Info"}).find("div",class_="time").get_text().strip()


            ArticleBody=BeautifulSoup(l.content).find("div",attrs={"id":"ContentBody"}).get_text().strip()
            link0="http://iguba.eastmoney.com/interf/reply.aspx?callback=jQuery183049486440794946285_1468306257505&action=infocode2topicid&infocode="
            link1=str(link0)+link.split(",")[1].split(".")[0]+u"&type=1&_=1468306257515"
            n=s.get(link1)
            
            d=eval(n.content.split("[")[1].split("]")[0]) #ArticleFrom
            cod=d['stockbar_code']
            po=d['post_id']
            link2=u'http://guba.eastmoney.com/news,' + str(cod) + u','+str(po) + u'.html'
            m=s.get(link2)
            if BeautifulSoup(m.content).find("div",attrs={"id":'zw_header'}) is None:
                ArticleFrom=u'东方财富网'
            else:
                ArticleFrom=BeautifulSoup(m.content).find("div",attrs={"id":'zw_header'}).get_text().strip()
            MediaFrom="东方财富网--银行"
            pd()


#财经网
def pq701():
    global ArticlePubTime
    global ArticleFrom
    global ArticleTitle
    global ArticleBody
    global link
    global MediaFrom
    r = s.get('http://www.caijing.com.cn').content
    html=etree.HTML(r)
    html2=html.xpath("//ul[@class='jrtt_list']/li/a")
    html3=html.xpath("//div[@class='jrtt_w']/h4/a")
    html4=html.xpath("//ul[@class='yaowen_ul yaowen_ulli']/li/a")
    html1=html2+html3+html4
    for sel in html1:
        title = "".join(sel.xpath('text()')).replace("[","").replace("]","")
        link = "".join(sel.xpath('@href')).replace(" ","").strip()
        #tit=title.encode('utf-8')
        #print link
        if len(title)==0 or len(link)==0:
            continue
        l=s.get(link).content
        htm=etree.HTML(l)
        ArticleTitle="".join(htm.xpath("//h2/text()"))
        ArticlePubTime="".join(htm.xpath("//span[@id='pubtime_baidu']/text()"))
        ArticleFrom="".join(htm.xpath("//span[@id='source_baidu']/text()"))
        if len(ArticleFrom)==0:
            ArticleFrom="".join(htm.xpath("//span[@id='source_baidu']/a/text()"))
        ArticleBody="".join(htm.xpath("//div[@class='article-content']//text()"))
        MediaFrom="财经网"
        #print link
        #print ArticleBody
        #print ArticleFrom
        pd()


#财经网--产经
def pq801():
    global ArticlePubTime
    global ArticleFrom
    global ArticleTitle
    global ArticleBody
    global link
    global MediaFrom
    r = s.get('http://industry.caijing.com.cn').content
    html=etree.HTML(r)
    html2=html.xpath("//ul[@class='jrtt_list']/li/a")
    html3=html.xpath("//div[@class='jrtt_w']/h4/a")
    html4=html.xpath("//div[@class='yaowen']/ul/li/a")
    html1=html2+html3+html4
    for sel in html1:
        title = "".join(sel.xpath('text()')).replace("[","").replace("]","")
        link = "".join(sel.xpath('@href')).replace(" ","").strip()
        #tit=title.encode('utf-8')
        #print link
        if len(title)==0 or len(link)==0:
            continue
        l=s.get(link).content
        htm=etree.HTML(l)
        ArticleTitle="".join(htm.xpath("//h2/text()"))
        ArticlePubTime="".join(htm.xpath("//span[@id='pubtime_baidu']/text()"))
        ArticleFrom="".join(htm.xpath("//span[@id='source_baidu']/text()"))
        if len(ArticleFrom)==0:
            ArticleFrom="".join(htm.xpath("//span[@id='source_baidu']/a/text()"))
        ArticleBody="".join(htm.xpath("//div[@id='the_content']//text()"))
        #print link
        #print ArticleBody
        #print ArticleFrom
        MediaFrom="财经网--产经"
        pd()


#财经网--地产
def pq802():
    global ArticlePubTime
    global ArticleFrom
    global ArticleTitle
    global ArticleBody
    global link
    global MediaFrom
    r = s.get('http://estate.caijing.com.cn').content
    html=etree.HTML(r)
    html2=html.xpath("//ul[@class='jrtt_list']/li/a")
    html3=html.xpath("//div[@class='jrtt_w']/h4/a")
    html4=html.xpath("//div[@class='yaowen']/ul/li/a")
    html1=html2+html3+html4
    for sel in html1:
        title = "".join(sel.xpath('text()')).replace("[","").replace("]","")
        link = "".join(sel.xpath('@href')).replace(" ","").strip()
        #tit=title.encode('utf-8')
        #print link
        if len(title)==0 or len(link)==0:
            continue
        l=s.get(link).content
        htm=etree.HTML(l)
        if "".join(htm.xpath("//span[@id='pubtime_baidu']/text()")) is None:
            continue
        else:
            ArticleTitle="".join(htm.xpath("//h2/text()"))
            ArticlePubTime="".join(htm.xpath("//span[@id='pubtime_baidu']/text()"))
            ArticleFrom="".join(htm.xpath("//span[@id='source_baidu']/text()"))
            if len(ArticleFrom)==0:
                ArticleFrom="".join(htm.xpath("//span[@id='source_baidu']/a/text()"))
            ArticleBody="".join(htm.xpath("//div[@id='the_content']//text()"))
            #print link
            #print ArticleBody
            #print ArticleFrom
            MediaFrom="财经网--地产"
            pd()


#财经网--金融
def pq803():
    global ArticlePubTime
    global ArticleFrom
    global ArticleTitle
    global ArticleBody
    global link
    global MediaFrom
    r = s.get('http://finance.caijing.com.cn').content
    html=etree.HTML(r)
    html2=html.xpath("//div[@class='first_tout']//a")
    html3=html.xpath("//div[@class='finance_yaowen']//a")
    #html4=html.xpath("//div[@class='yaowen']/ul/li/a")
    html1=html2+html3
    for sel in html1:
        title = "".join(sel.xpath('text()')).replace("[","").replace("]","")
        link = "".join(sel.xpath('@href')).replace(" ","").strip()
        #tit=title.encode('utf-8')
        #print link
        if len(title)==0 or len(link)==0:
            continue
        l=s.get(link).content
        htm=etree.HTML(l)
        ArticleTitle="".join(htm.xpath("//h2/text()"))
        ArticlePubTime="".join(htm.xpath("//span[@id='pubtime_baidu']/text()"))
        ArticleFrom="".join(htm.xpath("//span[@id='source_baidu']/text()"))
        if len(ArticleFrom)==0:
            ArticleFrom="".join(htm.xpath("//span[@id='source_baidu']/a/text()"))
        ArticleBody="".join(htm.xpath("//div[@id='the_content']//text()"))
        #print link
        #print ArticleBody
        #print ArticleFrom
        MediaFrom="财经网--金融"
        pd()
#财新网
def pq702():
    global ArticlePubTime
    global ArticleFrom
    global ArticleTitle
    global ArticleBody
    global link
    global MediaFrom
    r = s.get('http://www.caixin.com')
    bs1=BeautifulSoup(r.content).find("div",class_="mi").find_all("dt")
    bs2=BeautifulSoup(r.content).find("div",class_="indexMainConmi").find("div",class_="recommendBox").find_all("dt")
    bs3=BeautifulSoup(r.content).find("div",class_="indexMainConmi").find("div",class_="recommendBox").find_all("li")

    bs=bs1+bs2+bs3
    #print bs
    for i in bs:
        link=i.find("a").get("href").replace("hhttp","http").strip()
        #title=i.find("a").get_text()
        print link
        l=s.get(link)
        if BeautifulSoup(l.content).find("div",class_="textbox") is None:
            continue
        else:
            ArticleTitle=BeautifulSoup(l.content).find("h1").get_text()
            ArticleFrom=BeautifulSoup(l.content).find("div",class_="artInfo").find("a").get_text()
            ArticlePubTime=BeautifulSoup(l.content).find("div",class_="artInfo").get_text().replace("来源于","").strip()
            ArticleBody=BeautifulSoup(l.content).find("div",class_="textbox").get_text().strip()
            MediaFrom="财新网"
            #print link
            #print ArticleTitle
            if len(ArticleTitle)!=0:
                pd()

#财新网--房产公司【应该算第九类】
def pq901():
    global ArticlePubTime
    global ArticleFrom
    global ArticleTitle
    global ArticleBody
    global link
    global MediaFrom
    r= s.get('http://companies.caixin.com/property/')
    bs=BeautifulSoup(r.content).find("div",class_="stitXtuwen_list").find_all("h4")
    for i in bs:
        title=i.find("a").get_text().strip()
        link=i.find("a").get("href").strip()
        #print link
        l=s.get(link)
        ArticleTitle=BeautifulSoup(l.content).find("h1").get_text()
        ArticleFrom=BeautifulSoup(l.content).find("div",class_="artInfo").find("a").get_text()
        ArticlePubTime=BeautifulSoup(l.content).find("div",class_="artInfo").get_text().replace("来源于","").strip()
        ArticleBody=BeautifulSoup(l.content).find("div",class_="textbox").get_text().strip()
        MediaFrom="财新网--房产公司"
        print link
        print ArticleTitle
        pd()

#财新网--公司???
#财新网--金融
def pq805():
    global ArticlePubTime
    global ArticleFrom
    global ArticleTitle
    global ArticleBody
    global link
    global MediaFrom
    r= s.get('http://finance.caixin.com/')
    bs1=BeautifulSoup(r.content).find("div",class_="topNews").find_all("dt")
    bs2=BeautifulSoup(r.content).find("div",class_="topNews").find_all("li")
    bs3=BeautifulSoup(r.content).find("div",class_="ywListCon").find_all("h4")
    bs=bs1+bs2+bs3
    #print bs
    for i in bs:
        link=i.find("a").get("href").strip()
        title=i.find("a").get_text().strip()
        print title
        l=s.get(link)
        if BeautifulSoup(l.content).find("h1").get_text() is None:
            continue
        else:
            ArticleTitle=BeautifulSoup(l.content).find("h1").get_text()
            ArticleFrom=BeautifulSoup(l.content).find("div",class_="artInfo").find("a").get_text()
            ArticlePubTime=BeautifulSoup(l.content).find("div",class_="artInfo").get_text().replace("来源于","").strip()
            ArticleBody=BeautifulSoup(l.content).find("div",class_="textbox").get_text().strip()
            MediaFrom="财新网--金融"
            print link
            print ArticleTitle
            pd()


#财新网--经济
def pq806():
    global ArticlePubTime
    global ArticleFrom
    global ArticleTitle
    global ArticleBody
    global link
    global MediaFrom
    r= s.get('http://economy.caixin.com/')
    bs1=BeautifulSoup(r.content).find("div",class_="topNews").find_all("dt")
    bs2=BeautifulSoup(r.content).find("div",class_="topNews").find_all("li")
    bs3=BeautifulSoup(r.content).find("div",class_="ywListCon").find_all("h4")
    bs=bs1+bs2+bs3
    print bs
    for i in bs:
        link=i.find("a").get("href").strip()
        title=i.find("a").get_text().strip()
        print title
        l=s.get(link)
        ArticleTitle=BeautifulSoup(l.content).find("h1").get_text()
        ArticleFrom=BeautifulSoup(l.content).find("div",class_="artInfo").find("a").get_text()
        ArticlePubTime=BeautifulSoup(l.content).find("div",class_="artInfo").get_text().replace("来源于","").strip()
        ArticleBody=BeautifulSoup(l.content).find("div",class_="textbox").get_text().strip()
        MediaFrom="财新网--金融"
        print link
        print ArticleTitle
        pd()

#中金在线 ### 有一个文章有乱码？？
def pq704():
    global ArticlePubTime
    global ArticleFrom
    global ArticleTitle
    global ArticleBody
    global link
    global MediaFrom
    r = s.get('http://www.cnfol.com').content
    html=etree.HTML(r)
    li1=html.xpath("//dd[@style='display: block;'][1]//a")
    #print li1
    for sel in li1:
        title="".join(sel.xpath('text()')).strip()
        link="".join(sel.xpath('@href')).strip()
        #print title,link
        if len(title)==0 or len(link)==0:
            continue
        l=s.get(link).content
        htm=etree.HTML(l)
        if len("".join(htm.xpath("//div[@id='Content']//text()")))!=0:
            ArticleTitle="".join(htm.xpath("//h1/text()"))
            ArticleFrom="".join(htm.xpath("//span[@id='source_baidu']/*/text()"))
            ArticlePubTime="".join(htm.xpath("//span[@id='pubtime_baidu']/text()"))
            ArticleBody="".join(htm.xpath("//div[@id='Content']//text()"))
            MediaFrom="中金在线"
            #print ArticleTitle,link
            pd()
#中金在线--财经
def pq810():
    global ArticlePubTime
    global ArticleFrom
    global ArticleTitle
    global ArticleBody
    global link
    global MediaFrom
    r = s.get('http://news.cnfol.com/')
    bs=BeautifulSoup(r.content).find("div",class_="Ml10 Fl W420").find_all("a")
    #print bs
    for i in bs:
        title=i.get_text().strip()
        link=i.get("href").strip()
        #print title,link
        l=s.get(link)
        if BeautifulSoup(l.content).find("span",attrs={"id":"source_baidu"}) is None:
            continue
        else:
            ArticleTitle=BeautifulSoup(l.content).find("h1").get_text()
            ArticleFrom=BeautifulSoup(l.content).find("span",attrs={"id":"source_baidu"}).get_text()
            ArticlePubTime=BeautifulSoup(l.content).find("span",attrs={"id":"pubtime_baidu"}).get_text()
            ArticleBody=BeautifulSoup(l.content).find("div",attrs={"id":"Content"}).get_text().strip()
            MediaFrom="中金在线--财经"
            #print ArticleTitle,ArticlePubTime,ArticleFrom
            pd()

#中金在线--房产
def pq811():
    global ArticlePubTime
    global ArticleFrom
    global ArticleTitle
    global ArticleBody
    global link
    global MediaFrom
    r = s.get('http://house.cnfol.com/')
    bs=BeautifulSoup(r.content).find("ul",class_="HLstUl Cf").find_all("a")
    #print bs
    for i in bs:
        title=i.get_text().strip()
        link=i.get("href").strip()
        #print title,link
        l=s.get(link)
        if BeautifulSoup(l.content).find("span",attrs={"id":"source_baidu"}) is None:
            continue
        else:
            ArticleTitle=BeautifulSoup(l.content).find("h1").get_text()
            ArticleFrom=BeautifulSoup(l.content).find("span",attrs={"id":"source_baidu"}).get_text()
            ArticlePubTime=BeautifulSoup(l.content).find("span",attrs={"id":"pubtime_baidu"}).get_text()
            ArticleBody=BeautifulSoup(l.content).find("div",attrs={"id":"Content"}).get_text().strip()
            MediaFrom="中金在线--房产"
            print ArticleTitle,ArticlePubTime,ArticleFrom
            pd()
#中金在线--理财
def pq812():
    global ArticlePubTime
    global ArticleFrom
    global ArticleTitle
    global ArticleBody
    global link
    global MediaFrom
    r = s.get('http://money.cnfol.com/')
    bs=BeautifulSoup(r.content).find("ul",class_="ALnkLst").find_all("a")
    #print bs
    for i in bs:
        title=i.get_text().strip()
        link=i.get("href").strip()
        #print title,link
        l=s.get(link)
        if BeautifulSoup(l.content).find("span",attrs={"id":"source_baidu"}) is None:
            continue
        else:
            ArticleTitle=BeautifulSoup(l.content).find("h1").get_text()
            ArticleFrom=BeautifulSoup(l.content).find("span",attrs={"id":"source_baidu"}).get_text()
            ArticlePubTime=BeautifulSoup(l.content).find("span",attrs={"id":"pubtime_baidu"}).get_text()
            ArticleBody=BeautifulSoup(l.content).find("div",attrs={"id":"Content"}).get_text().strip()
            MediaFrom="中金在线--理财"
            pd()

#中金在线--汽车


#金融界财经
def pq819():
    global ArticlePubTime
    global ArticleFrom
    global ArticleTitle
    global ArticleBody
    global link
    global MediaFrom
    r = s.get('http://finance.jrj.com.cn/') 
    bs=BeautifulSoup(r.content).find("div",class_="l1_top").find_all("a")
    for i in bs:
        if len(i.get_text().strip())==0:
            continue
        else:
            link=(i.get('href')).strip()
            title=(i.get_text()).strip()
            #print link,title
            l=s.get(link).content
            htm=etree.HTML(l)
            MediaFrom="金融界财经"
            ArticleTitle="".join(htm.xpath("//div[@class='titmain']/h1/text()")).strip()
            if len(ArticleTitle)==0:
                ArticleTitle="".join(htm.xpath("//div[@class='texttitbox']/h2//text()")).strip()
                #if len(ArticleTitle)==0:
                #   continue
            ArticlePubTime="".join(htm.xpath("//p[@class='inftop']/span[1]//text()")).strip()
            if len(ArticlePubTime)==0:
                ArticlePubTime="".join(htm.xpath("//span[@class='time']//text()")).strip()
            ArticleFrom="".join(htm.xpath("//p[@class='inftop']/span[2]/a//text()")).strip().replace("来源：",'')
            if len(ArticleFrom)==0:
                ArticleFrom="".join(htm.xpath("//span[@class='urladd']//text()")).strip().replace("来源：",'')
                if len(ArticleFrom)==0:
                    ArticleFrom="".join(htm.xpath("//p[@class='inftop']/span[2]/text()")).strip().replace("来源：",'')
            ArticleBody="".join(htm.xpath("//div[@class='texttit_m1']//text()")).strip()
            if len(ArticleBody)==0:
                ArticleBody="".join(htm.xpath("//sapn[@style='float:']//text()")).strip()
            #print ArticleTitle,ArticlePubTime,ArticleFrom#,ArticleBody
            if len(ArticleFrom)==0:
                continue
            else:
                pd()
#金融界理财
def pq818():
    global ArticlePubTime
    global ArticleFrom
    global ArticleTitle
    global ArticleBody
    global link
    global MediaFrom
    r = s.get('http://money.jrj.com.cn/').content
    html=etree.HTML(r)
    for i in html.xpath("//div[@class='lcpd-body']/div/div/a"):
        link=i.get('href').strip()
        #print link
        l=s.get(link).content
        htm=etree.HTML(l)
        MediaFrom="金融界理财"
        ArticleTitle="".join(htm.xpath("//div[@class='titmain']/h1/text()")).strip()
        if len(ArticleTitle)==0:
            ArticleTitle="".join(htm.xpath("//div[@class='texttitbox']/h2//text()")).strip()
            #if len(ArticleTitle)==0:
            #   continue
        ArticlePubTime="".join(htm.xpath("//p[@class='inftop']/span[1]//text()")).strip()
        if len(ArticlePubTime)==0:
            ArticlePubTime="".join(htm.xpath("//span[@class='time']//text()")).strip()
        ArticleFrom="".join(htm.xpath("//p[@class='inftop']/span[2]/a//text()")).strip().replace("来源：",'')
        if len(ArticleFrom)==0:
            ArticleFrom="".join(htm.xpath("//span[@class='urladd']//text()")).strip().replace("来源：",'')
            if len(ArticleFrom)==0:
                ArticleFrom="".join(htm.xpath("//p[@class='inftop']/span[2]/text()")).strip().replace("来源：",'')
        ArticleBody="".join(htm.xpath("//div[@class='texttit_m1']//text()")).strip()
        if len(ArticleBody)==0:
            ArticleBody="".join(htm.xpath("//sapn[@style='float:']//text()")).strip()
        #print ArticleTitle,ArticlePubTime,ArticleFrom#,ArticleBody
        if len(ArticleFrom)==0:
            continue
        else:
            pd()
#金融界首页
def pq706():
    global ArticlePubTime
    global ArticleFrom
    global ArticleTitle
    global ArticleBody
    global link
    global MediaFrom
    r = s.get('http://www.jrj.com.cn/') 
    bs1=BeautifulSoup(r.content).find("div",class_="jsmain01").find_all("a")
    bs2=BeautifulSoup(r.content).find("div",class_="text-main-center").find_all("a")
    bs=bs1+bs2
    for i in bs:
        title=i.get_text().strip()
        link=i.get("href").strip()
 
        #print link,title
        if len(title)==0:
            continue
        else:
            l=s.get(link).content
            htm=etree.HTML(l)
            MediaFrom="金融界首页"
            ArticleTitle="".join(htm.xpath("//div[@class='titmain']/h1/text()")).strip()
            if len(ArticleTitle)==0:
                ArticleTitle="".join(htm.xpath("//div[@class='texttitbox']/h2//text()")).strip()
                #if len(ArticleTitle)==0:
                #   continue
            ArticlePubTime="".join(htm.xpath("//p[@class='inftop']/span[1]//text()")).strip()
            if len(ArticlePubTime)==0:
                ArticlePubTime="".join(htm.xpath("//span[@class='time']//text()")).strip()
            ArticleFrom="".join(htm.xpath("//p[@class='inftop']/span[2]/a//text()")).strip().replace("来源：",'')
            if len(ArticleFrom)==0:
                ArticleFrom="".join(htm.xpath("//span[@class='urladd']//text()")).strip().replace("来源：",'')
                if len(ArticleFrom)==0:
                    ArticleFrom="".join(htm.xpath("//p[@class='inftop']/span[2]/text()")).strip().replace("来源：",'')
            ArticleBody="".join(htm.xpath("//div[@class='texttit_m1']//text()")).strip()
            if len(ArticleBody)==0:
                ArticleBody="".join(htm.xpath("//sapn[@style='float:']//text()")).strip()
            #print ArticleTitle,ArticlePubTime,ArticleFrom#,ArticleBody
            if len(ArticleFrom)==0:
                continue
            else:
                pd()

pq201()
pq202()
pq203()
pq204()            
pq205()
pq302()
pq304()
pq306()
pq308()
pq309()
pq701()
pq702()

#pq703()

pq704()
pq705()
pq706()
pq801()
pq802()
pq803()
pq901()
pq805()
pq806()
#pq807()
#pq808()
#pq809()
pq810()
pq811()
pq812()
pq814()
pq816()
pq817()
pq818()
pq819()
