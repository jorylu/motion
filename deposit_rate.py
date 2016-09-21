#encoding:UTF-8
#恒丰银行  没有零存整取
#浦发银行 无存本取息
import requests #__version__ = 2.3.0 这里直接使用session，因为要先登陆 
from bs4 import BeautifulSoup #__version__ = 4.3.2
from lxml import etree
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from pymongo import MongoClient
mc=MongoClient("localhost",27017)
db=mc.test0
s=requests.session()
def cs():
    db.bank.save(
        {"银行":bank,"协定存款":xd,"活期":hq,"定活两便1年":dh1,"定活两便3月":dh03,"定活两便6月":dh06,
        "通知存款1天":tz1,"通知存款7天":tz7,"定期3月":dq03,"定期6月":dq06,"定期1年":dq1,"定期2年":dq2,"定期3年":dq3,"定期5年":dq5,
        "零存整取1年":lc1,"零存整取3年":lc3,"零存整取5年":lc5}
        )



#01央行
def b01():
    global hq
    global dq03
    global dq06
    global dq1
    global dq2
    global dq3
    global dq5
    global lc1
    global lc3
    global lc5
    global dh03
    global dh03
    global dh06
    global dh1
    global xd
    global tz1
    global tz7
    global bank
    bank="央行"
    r=s.get("http://www.pbc.gov.cn/zhengcehuobisi/125207/125213/125440/125838/125888/2968982/index.html").content
    html=etree.HTML(r)
    rq="".join(html.xpath("//tbody[10]/tr[last()]/td[1]//text()")).strip()
    hq="".join(html.xpath("//tbody[10]/tr[last()]/td[2]//text()")).strip()
    dq03="".join(html.xpath("//tbody[10]/tr[last()]/td[3]//text()")).strip()
    dq06="".join(html.xpath("//tbody[10]/tr[last()]/td[4]//text()")).strip()
    dq1="".join(html.xpath("//tbody[10]/tr[last()]/td[5]//text()")).strip()
    dq2="".join(html.xpath("//tbody[10]/tr[last()]/td[6]//text()")).strip()
    dq3="".join(html.xpath("//tbody[10]/tr[last()]/td[7]//text()")).strip()
    dq5="".join(html.xpath("//tbody[10]/tr[last()]/td[8]//text()")).strip()
    lc1="-"
    lc3="-"
    lc5="-"
    dh03="-"
    dh06="-"
    dh1="-"
    xd="-"
    tz1="-"
    tz7="-"
    cs()
    

    
#中行
def b02():
    global hq
    global dq03
    global dq06
    global dq1
    global dq2
    global dq3
    global dq5
    global lc1
    global lc3
    global lc5
    global dh03
    global dh03
    global dh06
    global dh1
    global xd
    global tz1
    global tz7
    global bank
    bank="中国银行"
    r=s.get("http://www.bankofchina.com/fimarkets/lilv/fd31/201510/t20151023_5824963.html").content
    html=etree.HTML(r)
    hq="".join(html.xpath("//table/tbody/tr[3]/td[2]/text()")).strip()
    dq03="".join(html.xpath("//table/tbody/tr[6]/td[2]/text()")).strip()
    dq06="".join(html.xpath("//table/tbody/tr[7]/td[2]/text()")).strip()
    dq1="".join(html.xpath("//table/tbody/tr[8]/td[2]/text()")).strip()
    dq2="".join(html.xpath("//table/tbody/tr[9]/td[2]/text()")).strip()
    dq3="".join(html.xpath("//table/tbody/tr[10]/td[2]/text()")).strip()
    dq5="".join(html.xpath("//table/tbody/tr[11]/td[2]/text()")).strip()
    lc1="".join(html.xpath("//table/tbody/tr[13]/td[2]/text()")).strip()
    lc3="".join(html.xpath("//table/tbody/tr[14]/td[2]/text()")).strip()
    lc5="".join(html.xpath("//table/tbody/tr[15]/td[2]/text()")).strip()
    dh03=0.6*float(dq03)
    dh06=0.6*float(dq06)
    dh1=0.6*float(dq1)
    xd="".join(html.xpath("//table/tbody/tr[17]/td[2]/text()")).strip()
    tz1="".join(html.xpath("//table/tbody/tr[19]/td[2]/text()")).strip()
    tz7="".join(html.xpath("//table/tbody/tr[20]/td[2]/text()")).strip()
    cs()



#农行
def b03():
    global hq
    global dq03
    global dq06
    global dq1
    global dq2
    global dq3
    global dq5
    global lc1
    global lc3
    global lc5
    global dh03
    global dh03
    global dh06
    global dh1
    global xd
    global tz1
    global tz7
    global bank
    bank="农业银行"
    r=s.get("http://www.abchina.com/cn/PersonalServices/Quotation/bwbll/201511/t20151126_807920.htm").content
    html=etree.HTML(r)
    hq="".join(html.xpath("//table/tbody/tr[3]/td[2]/text()")).strip()
    dq03="".join(html.xpath("//table/tbody/tr[6]/td[2]/text()")).strip()
    dq06="".join(html.xpath("//table/tbody/tr[7]/td[2]/text()")).strip()
    dq1="".join(html.xpath("//table/tbody/tr[8]/td[2]/text()")).strip()
    dq2="".join(html.xpath("//table/tbody/tr[9]/td[2]/text()")).strip()
    dq3="".join(html.xpath("//table/tbody/tr[10]/td[2]/text()")).strip()
    dq5="".join(html.xpath("//table/tbody/tr[11]/td[2]/text()")).strip()
    lc1="".join(html.xpath("//table/tbody/tr[13]/td[2]/text()")).strip()
    lc3="".join(html.xpath("//table/tbody/tr[14]/td[2]/text()")).strip()
    lc5="".join(html.xpath("//table/tbody/tr[15]/td[2]/text()")).strip()
    dh03=0.6*float(dq03)
    dh06=0.6*float(dq06)
    dh1=0.6*float(dq1)
    xd="".join(html.xpath("//table/tbody/tr[17]/td[2]/text()")).strip()
    tz1="".join(html.xpath("//table/tbody/tr[19]/td[2]/text()")).strip()
    tz7="".join(html.xpath("//table/tbody/tr[20]/td[2]/text()")).strip()
    cs()



#工商
def b04():
    global hq
    global dq03
    global dq06
    global dq1
    global dq2
    global dq3
    global dq5
    global lc1
    global lc3
    global lc5
    global dh03
    global dh03
    global dh06
    global dh1
    global xd
    global tz1
    global tz7
    global bank
    bank="工商银行"    
    r=s.get("http://www.icbc.com.cn/ICBCDynamicSite2/other/rmbdeposit.aspx").content
    html=etree.HTML(r)
    #rq="".join(html.xpath("/html/body/form/table/tbody/tr/td/table[3]/tbody/tr/td[2]/text()")).strip()
    hq="".join(html.xpath("//table/tbody/tr[3]/td[2]/text()")).strip()
    dq03="".join(html.xpath("//table/tbody/tr[6]/td[2]/text()")).strip()
    dq06="".join(html.xpath("//table/tbody/tr[7]/td[2]/text()")).strip()
    dq1="".join(html.xpath("//table/tbody/tr[8]/td[2]/text()")).strip()
    dq2="".join(html.xpath("//table/tbody/tr[9]/td[2]/text()")).strip()
    dq3="".join(html.xpath("//table/tbody/tr[10]/td[2]/text()")).strip()
    dq5="".join(html.xpath("//table/tbody/tr[11]/td[2]/text()")).strip()
    lc1="".join(html.xpath("//table/tbody/tr[13]/td[2]/text()")).strip()
    lc3="".join(html.xpath("//table/tbody/tr[14]/td[2]/text()")).strip()
    lc5="".join(html.xpath("//table/tbody/tr[15]/td[2]/text()")).strip()
    dh03=0.6*float(dq03)
    dh06=0.6*float(dq06)
    dh1=0.6*float(dq1)
    xd="".join(html.xpath("//table/tbody/tr[17]/td[2]/text()")).strip()
    tz1="".join(html.xpath("//table/tbody/tr[19]/td[2]/text()")).strip()
    tz7="".join(html.xpath("//table/tbody/tr[20]/td[2]/text()")).strip()
    cs()


#建设银行  要取到最新的网址才行
def b05():
    global hq
    global dq03
    global dq06
    global dq1
    global dq2
    global dq3
    global dq5
    global lc1
    global lc3
    global lc5
    global dh03
    global dh03
    global dh06
    global dh1
    global xd
    global tz1
    global tz7
    global bank
    bank="建设银行"
    r=s.get("http://ccb.com/cn/personal/interest/rmbdeposit.html").content
    html=etree.HTML(r)
    #只要最新的日期
    link1="".join(html.xpath("//*[@id='_list_page']/div[1]/select/option[2]/@value")).strip()
    print link1
    link=str("http://ccb.com/cn/personal/interest/")+str(link1)+str(".html")
    r1=s.get(link).content
    html=etree.HTML(r1)
    hq="".join(html.xpath("//table/tbody/tr[3]/td[2]/text()")).strip()
    dq03="".join(html.xpath("//table/tbody/tr[6]/td[2]/text()")).strip()
    dq06="".join(html.xpath("//table/tbody/tr[7]/td[2]/text()")).strip()
    dq1="".join(html.xpath("//table/tbody/tr[8]/td[2]/text()")).strip()
    dq2="".join(html.xpath("//table/tbody/tr[9]/td[2]/text()")).strip()
    dq3="".join(html.xpath("//table/tbody/tr[10]/td[2]/text()")).strip()
    dq5="".join(html.xpath("//table/tbody/tr[11]/td[2]/text()")).strip()
    lc1="".join(html.xpath("//table/tbody/tr[13]/td[2]/text()")).strip()
    lc3="".join(html.xpath("//table/tbody/tr[14]/td[2]/text()")).strip()
    lc5="".join(html.xpath("//table/tbody/tr[15]/td[2]/text()")).strip()
    dh03=0.6*float(dq03)
    dh06=0.6*float(dq06)
    dh1=0.6*float(dq1)
    xd="——"
    tz1="".join(html.xpath("//table/tbody/tr[18]/td[2]/text()")).strip()
    tz7="".join(html.xpath("//table/tbody/tr[19]/td[2]/text()")).strip()
    cs()



#交通银行
def b06():
    global hq
    global dq03
    global dq06
    global dq1
    global dq2
    global dq3
    global dq5
    global lc1
    global lc3
    global lc5
    global dh03
    global dh03
    global dh06
    global dh1
    global xd
    global tz1
    global tz7
    global bank
    bank="交通银行"
    r=s.get("http://www.bankcomm.com/BankCommSite/getRMBDepositRateDate.do").content
    html=etree.HTML(r)
    hq="".join(html.xpath("//tbody/tr[5]/td[2]/div/div/span[last()]/text()")).strip()
    dq03="".join(html.xpath("//tbody/tr[8]/td[2]/div/div/span[last()]/text()")).strip()
    dq06="".join(html.xpath("//tbody/tr[9]/td[2]/div/div/span[last()]/text()")).strip()
    dq1="".join(html.xpath("//tbody/tr[10]/td[2]/div/div/span[last()]/text()")).strip()
    dq2="".join(html.xpath("//tbody/tr[11]/td[2]/div/div/span[last()]/text()")).strip()
    dq3="".join(html.xpath("//tbody/tr[12]/td[2]/div/div/span[last()]/text()")).strip()
    dq5="".join(html.xpath("//tbody/tr[13]/td[2]/div/div/span[last()]/text()")).strip()
    lc1="".join(html.xpath("//tbody/tr[15]/td[2]/div/div/span[last()]/text()")).strip()
    lc3="".join(html.xpath("//tbody/tr[16]/td[2]/div/div/span[last()]/text()")).strip()
    lc5="".join(html.xpath("//tbody/tr[17]/td[2]/div/div/span[last()]/text()")).strip()
    dh03=0.6*float(dq03)
    dh06=0.6*float(dq06)
    dh1=0.6*float(dq1)
    xd="".join(html.xpath("//tbody/tr[19]/td[2]/div/div/span[last()]/text()")).strip()
    tz1="".join(html.xpath("//tbody/tr[21]/td[2]/div/div/span[last()]/text()")).strip()
    tz7="".join(html.xpath("//tbody/tr[22]/td[2]/div/div/span[last()]/text()")).strip()
    cs()

#邮政储蓄银行
def b07():
    global hq
    global dq03
    global dq06
    global dq1
    global dq2
    global dq3
    global dq5
    global lc1
    global lc3
    global lc5
    global dh03
    global dh03
    global dh06
    global dh1
    global xd
    global tz1
    global tz7
    global bank
    bank="邮政储蓄银行"
    r=s.get("http://www.psbc.com/cn/CorporateBanking/yewuzhinan/XXSJfabu/956.html").content
    html=etree.HTML(r)
    hq="".join(html.xpath("//tbody/tr[3]/td[last()]//text()")).strip()
    dq03="".join(html.xpath("//tbody/tr[6]/td[last()]//text()")).strip()
    dq06="".join(html.xpath("//tbody/tr[7]/td[last()]//text()")).strip()
    dq1="".join(html.xpath("//tbody/tr[8]/td[last()]//text()")).strip()
    dq2="".join(html.xpath("//tbody/tr[9]/td[last()]//text()")).strip()
    dq3="".join(html.xpath("//tbody/tr[10]/td[last()]//text()")).strip()
    dq5="".join(html.xpath("//tbody/tr[11]/td[last()]//text()")).strip()
    lc1="".join(html.xpath("//tbody/tr[13]/td[last()]//text()")).strip()
    lc3="".join(html.xpath("//tbody/tr[14]/td[last()]//text()")).strip()
    lc5="".join(html.xpath("//tbody/tr[15]/td[last()]//text()")).strip()
    dh03=0.6*float(dq03)
    dh06=0.6*float(dq06)
    dh1=0.6*float(dq1)
    xd="".join(html.xpath("//tbody/tr[17]/td[last()]//text()")).strip()
    tz1="".join(html.xpath("//tbody/tr[19]/td[last()]//text()")).strip()
    tz7="".join(html.xpath("//tbody/tr[20]/td[last()]//text()")).strip()
    cs()
    

#招商银行(零存整取 整存零取 存本取息 三个都一样)
def b08():
    global hq
    global dq03
    global dq06
    global dq1
    global dq2
    global dq3
    global dq5
    global lc1
    global lc3
    global lc5
    global dh03
    global dh03
    global dh06
    global dh1
    global xd
    global tz1
    global tz7
    global bank
    bank="招商银行"
    r=s.get("http://www.cmbchina.com/CmbWebPubInfo/InterestRate.aspx?chnl=ckrate").content
    html=etree.HTML(r)
    #真的是自己会加tbody标签所以自己要看下源文件
    hq="".join(html.xpath("//table[@class='tablecontent']/tr[1]/td[2]//text()")).strip()
    dq03="".join(html.xpath("//table[@class='tablecontent']/tr[5]/td[2]//text()")).strip()
    dq06="".join(html.xpath("//table[@class='tablecontent']/tr[6]/td[2]//text()")).strip()
    dq1="".join(html.xpath("//table[@class='tablecontent']/tr[7]/td[2]//text()")).strip()
    dq2="".join(html.xpath("//table[@class='tablecontent']/tr[8]/td[2]//text()")).strip()
    dq3="".join(html.xpath("//table[@class='tablecontent']/tr[9]/td[2]//text()")).strip()
    dq5="".join(html.xpath("//table[@class='tablecontent']/tr[10]/td[2]//text()")).strip()
    lc1="".join(html.xpath("//table[@class='tablecontent']/tr[11]/td[2]//text()")).strip()
    lc3="".join(html.xpath("//table[@class='tablecontent']/tr[12]/td[2]//text()")).strip()
    lc5="".join(html.xpath("//table[@class='tablecontent']/tr[13]/td[2]//text()")).strip()
    dh03=0.6*float(dq03)
    dh06=0.6*float(dq06)
    dh1=0.6*float(dq1)
    xd="-"
    tz1="".join(html.xpath("//table[@class='tablecontent']/tr[2]/td[2]//text()")).strip()
    tz7="".join(html.xpath("//table[@class='tablecontent']/tr[3]/td[2]//text()")).strip()
    cs()

#浦发银行 无存本取息
def b09():
    global hq
    global dq03
    global dq06
    global dq1
    global dq2
    global dq3
    global dq5
    global lc1
    global lc3
    global lc5
    global dh03
    global dh03
    global dh06
    global dh1
    global xd
    global tz1
    global tz7
    global bank
    bank="浦发银行"
    r=s.get("http://per.spdb.com.cn/rate_query/201511/t20151119_23933.shtml").content
    html=etree.HTML(r)
    #真的是自己会加tbody标签所以自己要看下源文
    
    hq="".join(html.xpath('//*[@id="tableid"]/tbody/tr[1]/td[4]/text()')).strip()
    dq03="".join(html.xpath('//*[@id="tableid"]/tbody/tr[2]/td[4]/text()')).strip()
    dq06="".join(html.xpath('//*[@id="tableid"]/tbody/tr[3]/td[4]/text()')).strip()
    dq1="".join(html.xpath('//*[@id="tableid"]/tbody/tr[4]/td[4]/text()')).strip()
    dq2="".join(html.xpath('//*[@id="tableid"]/tbody/tr[5]/td[4]/text()')).strip()
    dq3="".join(html.xpath('//*[@id="tableid"]/tbody/tr[6]/td[4]/text()')).strip()
    dq5="".join(html.xpath('//*[@id="tableid"]/tbody/tr[7]/td[4]/text()')).strip()
    lc1="".join(html.xpath('//*[@id="tableid"]/tbody/tr[8]/td[4]/text()')).strip()
    lc3="".join(html.xpath('//*[@id="tableid"]/tbody/tr[9]/td[4]/text()')).strip()
    lc5="".join(html.xpath('//*[@id="tableid"]/tbody/tr[10]/td[4]/text()')).strip()
    dh03=0.6*float(dq03)
    dh06=0.6*float(dq06)
    dh1=0.6*float(dq1)
    xd="-"
    tz1="".join(html.xpath('//*[@id="tableid"]/tbody/tr[15]/td[4]/text()')).strip()
    tz7="".join(html.xpath('//*[@id="tableid"]/tbody/tr[16]/td[4]/text()')).strip()
    cs()



#中信银行    被ban了
def b10():
    global hq
    global dq03
    global dq06
    global dq1
    global dq2
    global dq3
    global dq5
    global lc1
    global lc3
    global lc5
    global dh03
    global dh03
    global dh06
    global dh1
    global xd
    global tz1
    global tz7
    global bank
    bank="中信银行"
    header={
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Host':'bank.ecitic.com',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }
    r=s.get("http://bank.ecitic.com/efinan/index.shtml",headers=header).content
    html=etree.HTML(r)
    #真的是自己会加tbody标签所以自己要看下源文
    
    hq="".join(html.xpath("//div[@class='sideleft']/table[1]/tr[2]/td[2]//text()")).strip()
    dq03="".join(html.xpath("//div[@class='sideleft']/table[1]/tr[5]/td[2]//text()")).strip()
    dq06="".join(html.xpath("//div[@class='sideleft']/table[1]/tr[6]/td[2]//text()")).strip()
    dq1="".join(html.xpath("//div[@class='sideleft']/table[1]/tr[7]/td[2]//text()")).strip()
    dq2="".join(html.xpath("//div[@class='sideleft']/table[1]/tr[8]/td[2]//text()")).strip()
    dq3="".join(html.xpath("//div[@class='sideleft']/table[1]/tr[9]/td[2]//text()")).strip()
    dq5="".join(html.xpath("//div[@class='sideleft']/table[1]/tr[10]/td[2]//text()")).strip()
    lc1="".join(html.xpath("//div[@class='sideleft']/table[1]/tr[12]/td[2]//text()")).strip()
    lc3="".join(html.xpath("//div[@class='sideleft']/table[1]/tr[13]/td[2]//text()")).strip()
    lc5="".join(html.xpath("//div[@class='sideleft']/table[1]/tr[14]/td[2]//text()")).strip()
    dh03=0.6*float(dq03)
    dh06=0.6*float(dq06)
    dh1=0.6*float(dq1)
    xd="-"
    tz1="".join(html.xpath("//div[@class='sideleft']/table[1]/tr[17]/td[2]//text()")).strip()
    tz7="".join(html.xpath("//div[@class='sideleft']/table[1]/tr[18]/td[2]//text()")).strip()
    cs()


 
    
#华夏银行
def b11():
    global hq
    global dq03
    global dq06
    global dq1
    global dq2
    global dq3
    global dq5
    global lc1
    global lc3
    global lc5
    global dh03
    global dh03
    global dh06
    global dh1
    global xd
    global tz1
    global tz7
    global bank
    bank="华夏银行"
    r=s.get("http://www.hxb.com.cn/home/cn/clientServ/jinrong/lilvhuilv/list.shtml").content
    html=etree.HTML(r)
    #真的是自己会加tbody标签所以自己要看下源文件
    hq="".join(html.xpath('//*[@id="1"]/div/table/tbody/tr[2]/td[2]/p/text()')).strip()
    dq03="".join(html.xpath('//*[@id="1"]/div/table/tbody/tr[4]/td[2]/p/text()')).strip()
    dq06="".join(html.xpath('//*[@id="1"]/div/table/tbody/tr[5]/td[2]/p/text()')).strip()
    dq1="".join(html.xpath('//*[@id="1"]/div/table/tbody/tr[6]/td[2]/p/text()')).strip()
    dq2="".join(html.xpath('//*[@id="1"]/div/table/tbody/tr[7]/td[2]/p/text()')).strip()
    dq3="".join(html.xpath('//*[@id="1"]/div/table/tbody/tr[8]/td[2]/p/text()')).strip()
    dq5="".join(html.xpath('//*[@id="1"]/div/table/tbody/tr[9]/td[2]/p/text()')).strip()
    lc1="".join(html.xpath('//*[@id="1"]/div/table/tbody/tr[11]/td[2]/p/text()')).strip()
    lc3="".join(html.xpath('//*[@id="1"]/div/table/tbody/tr[12]/td[2]/p/text()')).strip()
    lc5="".join(html.xpath('//*[@id="1"]/div/table/tbody/tr[13]/td[2]/p/text()')).strip()
    dh03=0.6*float(dq03)
    dh06=0.6*float(dq06)
    dh1=0.6*float(dq1)
    xd="-"
    tz1="".join(html.xpath('//*[@id="1"]/div/table/tbody/tr[17]/td[3]/p/text()')).strip()
    tz7="".join(html.xpath('//*[@id="1"]/div/table/tbody/tr[18]/td[3]/p/text()')).strip()
    cs()


#兴业银行
def b12():
    global hq
    global dq03
    global dq06
    global dq1
    global dq2
    global dq3
    global dq5
    global lc1
    global lc3
    global lc5
    global dh03
    global dh03
    global dh06
    global dh1
    global xd
    global tz1
    global tz7
    global bank
    bank="兴业银行"
    r=s.get("http://www.cib.com.cn/cn/personal/saving/rates/index.html").content
    html=etree.HTML(r)
    #真的是自己会加tbody标签所以自己要看下源文件
    hq="".join(html.xpath('//*[@id="content"]/div[2]/div[2]/table/tbody/tr[6]/td[2]/text()')).strip()
    dq03="".join(html.xpath('//*[@id="content"]/div[2]/div[2]/table/tbody/tr[11]/td[2]/text()')).strip()
    dq06="".join(html.xpath('//*[@id="content"]/div[2]/div[2]/table/tbody/tr[12]/td[2]/text()')).strip()
    dq1="".join(html.xpath('//*[@id="content"]/div[2]/div[2]/table/tbody/tr[13]/td[2]/text()')).strip()
    dq2="".join(html.xpath('//*[@id="content"]/div[2]/div[2]/table/tbody/tr[14]/td[2]/text()')).strip()
    dq3="".join(html.xpath('//*[@id="content"]/div[2]/div[2]/table/tbody/tr[15]/td[2]/text()')).strip()
    dq5="".join(html.xpath('//*[@id="content"]/div[2]/div[2]/table/tbody/tr[16]/td[2]/text()')).strip()
    lc1="".join(html.xpath('//*[@id="content"]/div[2]/div[2]/table/tbody/tr[18]/td[2]/text()')).strip()
    lc3="".join(html.xpath('//*[@id="content"]/div[2]/div[2]/table/tbody/tr[19]/td[2]/text()')).strip()
    lc5="".join(html.xpath('//*[@id="content"]/div[2]/div[2]/table/tbody/tr[20]/td[2]/text()')).strip()
    dh03=0.6*float(dq03)
    dh06=0.6*float(dq06)
    dh1=0.6*float(dq1)
    xd="-"
    tz1="".join(html.xpath('//*[@id="content"]/div[2]/div[2]/table/tbody/tr[23]/td[2]/text()')).strip()
    tz7="".join(html.xpath('//*[@id="content"]/div[2]/div[2]/table/tbody/tr[24]/td[2]/text()')).strip()
    cs()
#民生银行  picture


#光大银行
def b14():
    global hq
    global dq03
    global dq06
    global dq1
    global dq2
    global dq3
    global dq5
    global lc1
    global lc3
    global lc5
    global dh03
    global dh03
    global dh06
    global dh1
    global xd
    global tz1
    global tz7
    global bank
    bank="光大银行"
    r=s.get("http://www.cebbank.com/site/ygzx/cdll/index.html").content
    html=etree.HTML(r)
    link1="".join(html.xpath('//*[@id="sl"]/option[2]/@value')).strip()
    link=u"http://www.cebbank.com"+link1
    r1=s.get(link).content
    html=etree.HTML(r1)
    hq="".join(html.xpath('//table/tbody/tr[2]/td[2]/text()')).strip()
    dq03="".join(html.xpath('//table/tbody/tr[5]/td[2]/text()')).strip()
    dq06="".join(html.xpath('//table/tbody/tr[6]/td[2]/text()')).strip()
    dq1="".join(html.xpath('//table/tbody/tr[7]/td[2]/text()')).strip()
    dq2="".join(html.xpath('//table/tbody/tr[8]/td[2]/text()')).strip()
    dq3="".join(html.xpath('//table/tbody/tr[9]/td[2]/text()')).strip()
    dq5="".join(html.xpath('//table/tbody/tr[10]/td[2]/text()')).strip()
    lc1="".join(html.xpath('//table/tbody/tr[12]/td[2]/text()')).strip()
    lc3="".join(html.xpath('//table/tbody/tr[13]/td[2]/text()')).strip()
    lc5="".join(html.xpath('//table/tbody/tr[14]/td[2]/text()')).strip()
    dh03=0.6*float(dq03)
    dh06=0.6*float(dq06)
    dh1=0.6*float(dq1)
    xd="-"
    tz1="".join(html.xpath('//table/tbody/tr[18]/td[2]/text()')).strip()
    tz7="".join(html.xpath('//table/tbody/tr[19]/td[2]/text()')).strip()
    cs()
    
#平安银行
def b15():
    global hq
    global dq03
    global dq06
    global dq1
    global dq2
    global dq3
    global dq5
    global lc1
    global lc3
    global lc5
    global dh03
    global dh03
    global dh06
    global dh1
    global xd
    global tz1
    global tz7
    global bank
    bank="平安银行"
    r=s.get("http://bank.pingan.com/geren/cunkuanlilv/index.shtml").content
    html=etree.HTML(r)
    hq="".join(html.xpath("//table[@style='table-layout:fixed;']/tr[2]/td[2]/text()")).strip()
    dq03="".join(html.xpath("//table[@style='table-layout:fixed;']/tr[4]/td[2]/text()")).strip()
    dq06="".join(html.xpath("//table[@style='table-layout:fixed;']/tr[5]/td[2]/text()")).strip()
    dq1="".join(html.xpath("//table[@style='table-layout:fixed;']/tr[6]/td[2]/text()")).strip()
    dq2="".join(html.xpath("//table[@style='table-layout:fixed;']/tr[7]/td[2]/text()")).strip()
    dq3="".join(html.xpath("//table[@style='table-layout:fixed;']/tr[8]/td[2]/text()")).strip()
    dq5="".join(html.xpath("//table[@style='table-layout:fixed;']/tr[9]/td[2]/text()")).strip()
    lc1="".join(html.xpath("//table[@style='table-layout:fixed;']/tr[11]/td[2]/text()")).strip()
    lc3="".join(html.xpath("//table[@style='table-layout:fixed;']/tr[12]/td[2]/text()")).strip()
    lc5="-"
    dh03="".join(html.xpath("//table[@style='table-layout:fixed;']/tr[14]/td[2]/text()")).strip()
    dh06="".join(html.xpath("//table[@style='table-layout:fixed;']/tr[15]/td[2]/text()")).strip()
    dh1="".join(html.xpath("//table[@style='table-layout:fixed;']/tr[16]/td[2]/text()")).strip()
    xd="-"
    tz1="".join(html.xpath("//table[@style='table-layout:fixed;']/tr[18]/td[2]/text()")).strip()
    tz7="".join(html.xpath("//table[@style='table-layout:fixed;']/tr[19]/td[2]/text()")).strip()
    cs()
#广发银行
def b16():
    global hq
    global dq03
    global dq06
    global dq1
    global dq2
    global dq3
    global dq5
    global lc1
    global lc3
    global lc5
    global dh03
    global dh03
    global dh06
    global dh1
    global xd
    global tz1
    global tz7
    global bank
    bank="广发银行"
    r=s.get("http://www.cgbchina.com.cn/showCHYDepositRate.gsp").content
    html=etree.HTML(r)
    hq="".join(html.xpath('//table[@class="second_tb"]/tr[2]/td[2]/text()')).strip()
    dq03="".join(html.xpath('//table[@class="second_tb"]/tr[5]/td[2]/text()')).strip()
    dq06="".join(html.xpath('//table[@class="second_tb"]/tr[6]/td[2]/text()')).strip()
    dq1="".join(html.xpath('//table[@class="second_tb"]/tr[7]/td[2]/text()')).strip()
    dq2="".join(html.xpath('//table[@class="second_tb"]/tr[8]/td[2]/text()')).strip()
    dq3="".join(html.xpath('//table[@class="second_tb"]/tr[9]/td[2]/text()')).strip()
    dq5="".join(html.xpath('//table[@class="second_tb"]/tr[10]/td[2]/text()')).strip()
    lc1="".join(html.xpath('//table[@class="second_tb"]/tr[12]/td[2]/text()')).strip()
    lc3="".join(html.xpath('//table[@class="second_tb"]/tr[13]/td[2]/text()')).strip()
    lc5="".join(html.xpath('//table[@class="second_tb"]/tr[14]/td[2]/text()')).strip()
    dh03="".join(html.xpath('//table[@class="second_tb"]/tr[16]/td[2]/text()')).strip()
    dh06="".join(html.xpath('//table[@class="second_tb"]/tr[17]/td[2]/text()')).strip()
    dh1="".join(html.xpath('//table[@class="second_tb"]/tr[18]/td[2]/text()')).strip()
    xd="".join(html.xpath('//table[@class="second_tb"]/tr[19]/td[2]/text()')).strip()
    tz1="".join(html.xpath('//table[@class="second_tb"]/tr[21]/td[2]/text()')).strip()
    tz7="".join(html.xpath('//table[@class="second_tb"]/tr[22]/td[2]/text()')).strip()
    cs()
    

#浙商银行
def b17():
    global hq
    global dq03
    global dq06
    global dq1
    global dq2
    global dq3
    global dq5
    global lc1
    global lc3
    global lc5
    global dh03
    global dh03
    global dh06
    global dh1
    global xd
    global tz1
    global tz7
    global bank
    bank="浙商银行"
    r=s.get("http://www.czbank.com/czbank/html/170.html").content
    html=etree.HTML(r)
    hq="".join(html.xpath('//table[@bordercolor="#efecec"]/tbody/tr[4]/td[2]/strong/text()')).strip()
    dq03="".join(html.xpath('//table[@bordercolor="#efecec"]/tbody/tr[7]/td[2]/strong/text()')).strip()
    dq06="".join(html.xpath('//table[@bordercolor="#efecec"]/tbody/tr[8]/td[2]/strong/text()')).strip()
    dq1="".join(html.xpath('//table[@bordercolor="#efecec"]/tbody/tr[9]/td[2]/strong/text()')).strip()
    dq2="".join(html.xpath('//table[@bordercolor="#efecec"]/tbody/tr[10]/td[2]/strong/text()')).strip()
    dq3="".join(html.xpath('//table[@bordercolor="#efecec"]/tbody/tr[11]/td[2]/strong/text()')).strip()
    dq5="".join(html.xpath('//table[@bordercolor="#efecec"]/tbody/tr[12]/td[2]/strong/text()')).strip()
    lc1="".join(html.xpath('//table[@bordercolor="#efecec"]/tbody/tr[14]/td[2]/strong/text()')).strip()
    lc3="".join(html.xpath('//table[@bordercolor="#efecec"]/tbody/tr[15]/td[2]/strong/text()')).strip()
    lc5="".join(html.xpath('//table[@bordercolor="#efecec"]/tbody/tr[16]/td[2]/strong/text()')).strip()
    dh03=0.6*float(dq03)
    dh06=0.6*float(dq06)
    dh1=0.6*float(dq1)
    xd="".join(html.xpath('//table[@bordercolor="#efecec"]/tbody/tr[18]/td[2]/strong/text()')).strip()
    tz1="".join(html.xpath('//table[@bordercolor="#efecec"]/tbody/tr[20]/td[2]/strong/text()')).strip()
    tz7="".join(html.xpath('//table[@bordercolor="#efecec"]/tbody/tr[21]/td[2]/strong/text()')).strip()
    cs()

#恒丰银行  没有零存整取
def b18():
    global hq
    global dq03
    global dq06
    global dq1
    global dq2
    global dq3
    global dq5
    global lc1
    global lc3
    global lc5
    global dh03
    global dh03
    global dh06
    global dh1
    global xd
    global tz1
    global tz7
    global bank
    bank="恒丰银行"
    r=s.get('http://www.hfbank.com.cn/ucms/hfyh/jsp/gryw/cdkll_ckll.jsp').content
    html=etree.HTML(r)
    hq="".join(html.xpath('//td[@class="noBor"][1]/text()')).strip()
    dq03="".join(html.xpath('//td[@class="noBor"][3]/text()')).strip()
    dq06="".join(html.xpath('//td[@class="noBor"][4]/text()')).strip()
    dq1="".join(html.xpath('//td[@class="noBor"][5]/text()')).strip()
    dq2="".join(html.xpath('//td[@class="noBor"][6]/text()')).strip()
    dq3="".join(html.xpath('//td[@class="noBor"][7]/text()')).strip()
    dq5="".join(html.xpath('//td[@class="noBor"][8]/text()')).strip()
    lc1="".join(html.xpath('//td[@class="noBor"][15]/text()')).strip()
    lc3="".join(html.xpath('//td[@class="noBor"][16]/text()')).strip()
    lc5="".join(html.xpath('//td[@class="noBor"][17]/text()')).strip()
    dh03="-"
    dh06="-"
    dh1="-"
    xd="".join(html.xpath('//td[@class="noBor"][25]/text()')).strip()
    tz1="".join(html.xpath('//td[@class="noBor"][21]/text()')).strip()
    tz7="".join(html.xpath('//td[@class="noBor"][22]/text()')).strip()
    cs()
#渤海银行
def b19():
    global hq
    global dq03
    global dq06
    global dq1
    global dq2
    global dq3
    global dq5
    global lc1
    global lc3
    global lc5
    global dh03
    global dh03
    global dh06
    global dh1
    global xd
    global tz1
    global tz7
    global bank
    bank="渤海银行"
    r=s.get('http://www.cbhb.com.cn/bhbank/S101/jinronggongju/rmbdk/index.htm').content
    html=etree.HTML(r)
    hq="".join(html.xpath('//table[@class="MsoNormalTable"][1]/tbody[2]/tr[1]/td[2]/p/span/text()')).strip()
    dq03="".join(html.xpath('//table[@class="MsoNormalTable"][1]/tbody[2]/tr[4]/td[2]/p/span/text()')).strip()
    dq06="".join(html.xpath('//table[@class="MsoNormalTable"][1]/tbody[2]/tr[5]/td[2]/p/span/text()')).strip()
    dq1="".join(html.xpath('//table[@class="MsoNormalTable"][1]/tbody[2]/tr[6]/td[2]/p/span/text()')).strip()
    dq2="".join(html.xpath('//table[@class="MsoNormalTable"][1]/tbody[2]/tr[7]/td[2]/p/span/text()')).strip()
    dq3="".join(html.xpath('//table[@class="MsoNormalTable"][1]/tbody[2]/tr[8]/td[2]/p/span/text()')).strip()
    dq5="".join(html.xpath('//table[@class="MsoNormalTable"][1]/tbody[2]/tr[9]/td[2]/p/span/text()')).strip()
    lc1="".join(html.xpath('//table[@class="MsoNormalTable"][1]/tbody[2]/tr[11]/td[2]/p/span/text()')).strip()
    lc3="".join(html.xpath('//table[@class="MsoNormalTable"][1]/tbody[2]/tr[12]/td[2]/p/span/text()')).strip()
    lc5="".join(html.xpath('//table[@class="MsoNormalTable"][1]/tbody[2]/tr[13]/td[2]/p/span/text()')).strip()
    dh03=0.6*float(dq03)
    dh06=0.6*float(dq06)
    dh1=0.6*float(dq1)
    xd="-"
    tz1="".join(html.xpath('//table[@class="MsoNormalTable"][1]/tbody[2]/tr[16]/td[2]/p/span/text()')).strip()
    tz7="".join(html.xpath('//table[@class="MsoNormalTable"][1]/tbody[2]/tr[17]/td[2]/p/span/text()')).strip()
    cs()

#南京银行
def b20():
    global hq
    global dq03
    global dq06
    global dq1
    global dq2
    global dq3
    global dq5
    global lc1
    global lc3
    global lc5
    global dh03
    global dh03
    global dh06
    global dh1
    global xd
    global tz1
    global tz7
    global bank
    bank="南京银行"
    r=s.get("http://www.njcb.com.cn/njcb/index/khfw3/jrxx84/ckll/420655/416892/index.html").content
    html=etree.HTML(r)
    link1="".join(html.xpath('//option[2]/@value')).strip()
    link=u"http://www.njcb.com.cn/"+link1
    r1=s.get(link).content
    html1=etree.HTML(r1)
    hq="".join(html.xpath('//div[@id="news_content"]//tr[2]/td[2]/p/span/span/text()')).strip()
    dq03="".join(html.xpath('//div[@id="news_content"]//tr[5]/td[2]/p/span/span/text()')).strip()
    dq06="".join(html.xpath('//div[@id="news_content"]//tr[6]/td[2]/p/span/span/text()')).strip()
    dq1="".join(html.xpath('//div[@id="news_content"]//tr[7]/td[2]/p/span/span/text()')).strip()
    dq2="".join(html.xpath('//div[@id="news_content"]//tr[8]/td[2]/p/span/span/text()')).strip()
    dq3="".join(html.xpath('//div[@id="news_content"]//tr[9]/td[2]/p/span/span/text()')).strip()
    dq5="".join(html.xpath('//div[@id="news_content"]//tr[10]/td[2]/p/span/span/text()')).strip()
    lc1="".join(html.xpath('//div[@id="news_content"]//tr[12]/td[2]/p/span/span/text()')).strip()
    lc3="".join(html.xpath('//div[@id="news_content"]//tr[13]/td[2]/p/span/span/text()')).strip()
    lc5="".join(html.xpath('//div[@id="news_content"]//tr[14]/td[2]/p/span/span/text()')).strip()
    dh03=0.6*float(dq03)
    dh06=0.6*float(dq06)
    dh1=0.6*float(dq1)
    xd="".join(html.xpath('//div[@id="news_content"]//tr[24]/td[2]/p/span/span/text()')).strip()
    tz1="".join(html.xpath('//div[@id="news_content"]//tr[26]/td[2]/p/span/span/text()')).strip()
    tz7="".join(html.xpath('//div[@id="news_content"]//tr[27]/td[2]/p/span/span/text()')).strip()
    cs()


#宁波银行 被ban了加了个头搞定
def b21():
    global hq
    global dq03
    global dq06
    global dq1
    global dq2
    global dq3
    global dq5
    global lc1
    global lc3
    global lc5
    global dh03
    global dh03
    global dh06
    global dh1
    global xd
    global tz1
    global tz7
    global bank
    bank="宁波银行"
    header={
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Connection':'keep-alive',
    'Cookie':'_trs_uv=lzu_352_it1c2z2w; Hm_lvt_8b9480950a6cadd80a66f238d3e4542e=1473762402,1474187647; Hm_lpvt_8b9480950a6cadd80a66f238d3e4542e=1474187659',
    'Host':'www.nbcb.com.cn',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }
    r=s.get('http://www.nbcb.com.cn/shortcut/deposit_rates',headers=header).content
    html=etree.HTML(r)
    hq="".join(html.xpath('//table[2]/tbody/tr[2]/td[2]/text()')).strip()
    dq03="".join(html.xpath('//table[2]/tbody/tr[5]/td[2]/text()')).strip()
    dq06="".join(html.xpath('//table[2]/tbody/tr[6]/td[2]/text()')).strip()
    dq1="".join(html.xpath('//table[2]/tbody/tr[7]/td[2]/text()')).strip()
    dq2="".join(html.xpath('//table[2]/tbody/tr[8]/td[2]/text()')).strip()
    dq3="".join(html.xpath('//table[2]/tbody/tr[9]/td[2]/text()')).strip()
    dq5="".join(html.xpath('//table[2]/tbody/tr[10]/td[2]/text()')).strip()
    lc1="".join(html.xpath('//table[2]/tbody/tr[12]/td[2]/text()')).strip()
    lc3="".join(html.xpath('//table[2]/tbody/tr[13]/td[2]/text()')).strip()
    lc5="".join(html.xpath('//table[2]/tbody/tr[14]/td[2]/text()')).strip()
    dh03=0.6*float(dq03)
    dh06=0.6*float(dq06)
    dh1=0.6*float(dq1)
    xd="-"
    tz1="".join(html.xpath('//table[2]/tbody/tr[17]/td[2]/text()')).strip()
    tz7="".join(html.xpath('//table[2]/tbody/tr[18]/td[2]/text()')).strip()
    cs()

#北京银行
def b22():
    global hq
    global dq03
    global dq06
    global dq1
    global dq2
    global dq3
    global dq5
    global lc1
    global lc3
    global lc5
    global dh03
    global dh03
    global dh06
    global dh1
    global xd
    global tz1
    global tz7
    global bank
    bank="北京银行"
    r=s.get('http://www.bankofbeijing.com.cn/personal/rmbck_lv.html').content
    html=etree.HTML(r)
    hq="".join(html.xpath('//tr[9]/td[2]/text()')).strip()
    dq03="".join(html.xpath('//tr[12]/td[2]/text()')).strip()
    dq06="".join(html.xpath('//tr[13]/td[2]/text()')).strip()
    dq1="".join(html.xpath('//tr[14]/td[2]/text()')).strip()
    dq2="".join(html.xpath('//tr[15]/td[2]/text()')).strip()
    dq3="".join(html.xpath('//tr[16]/td[2]/text()')).strip()
    dq5="".join(html.xpath('//tr[17]/td[2]/text()')).strip()
    lc1="".join(html.xpath('//tr[19]/td[2]/text()')).strip()
    lc3="".join(html.xpath('//tr[20]/td[2]/text()')).strip()
    lc5="".join(html.xpath('//tr[21]/td[2]/text()')).strip()
    dh03=0.6*float(dq03)
    dh06=0.6*float(dq06)
    dh1=0.6*float(dq1)
    xd="-"
    tz1="".join(html.xpath('//tr[24]/td[2]/text()')).strip()
    tz7="".join(html.xpath('//tr[25]/td[2]/text()')).strip()
    cs()



#包商银行
def b23():
    global hq
    global dq03
    global dq06
    global dq1
    global dq2
    global dq3
    global dq5
    global lc1
    global lc3
    global lc5
    global dh03
    global dh03
    global dh06
    global dh1
    global xd
    global tz1
    global tz7
    global bank
    bank="包商银行"
    r=s.get('http://www.bsb.com.cn/grjr/cdll/201604/t20160413_533988.html').content
    html=etree.HTML(r)
    hq="".join(html.xpath('//*[@id="content"]/div/div/div/div/div/table/tbody/tr/td/table/tbody/tr[7]/td[4]/p/span/text()')).strip()
    dq03="".join(html.xpath('//*[@id="content"]/div/div/div/div/div/table/tbody/tr/td/table/tbody/tr[10]/td[4]/p/span/text()')).strip()
    dq06="".join(html.xpath('//*[@id="content"]/div/div/div/div/div/table/tbody/tr/td/table/tbody/tr[11]/td[4]/p/span/text()')).strip()
    dq1="".join(html.xpath('//*[@id="content"]/div/div/div/div/div/table/tbody/tr/td/table/tbody/tr[12]/td[4]/p/span/text()')).strip()
    dq2="".join(html.xpath('//*[@id="content"]/div/div/div/div/div/table/tbody/tr/td/table/tbody/tr[13]/td[4]/p/span/text()')).strip()
    dq3="".join(html.xpath('//*[@id="content"]/div/div/div/div/div/table/tbody/tr/td/table/tbody/tr[14]/td[4]/p/span/text()')).strip()
    dq5="".join(html.xpath('//*[@id="content"]/div/div/div/div/div/table/tbody/tr/td/table/tbody/tr[15]/td[4]/p/span/text()')).strip()
    lc1="".join(html.xpath('//*[@id="content"]/div/div/div/div/div/table/tbody/tr/td/table/tbody/tr[17]/td[4]/p/span/text()')).strip()
    lc3="".join(html.xpath('//*[@id="content"]/div/div/div/div/div/table/tbody/tr/td/table/tbody/tr[18]/td[4]/p/span/text()')).strip()
    lc5="".join(html.xpath('//*[@id="content"]/div/div/div/div/div/table/tbody/tr/td/table/tbody/tr[19]/td[4]/p/span/text()')).strip()
    dh03=0.6*float(dq03)
    dh06=0.6*float(dq06)
    dh1=0.6*float(dq1)
    xd="".join(html.xpath('//*[@id="content"]/div/div/div/div/div/table/tbody/tr/td/table/tbody/tr[21]/td[4]/p/span/text()')).strip()
    tz1="".join(html.xpath('//*[@id="content"]/div/div/div/div/div/table/tbody/tr/td/table/tbody/tr[23]/td[4]/p/span/text()')).strip()
    tz7="".join(html.xpath('//*[@id="content"]/div/div/div/div/div/table/tbody/tr/td/table/tbody/tr[24]/td[4]/p/span/text()')).strip()
    cs()
    
#江苏银行(图片) def b24():

#上海银行
def b25():
    r1=s.get('http://www.bankofshanghai.com/')
    r=s.get('http://www.bankofshanghai.com/WebServlet').content
    html=etree.HTML(r)
    hq="".join(html.xpath('//*[@id="workForm"]/div/div/table/tbody/tr[1]/td/table[1]/tbody/tr[4]/td[5]/div/text()')).strip()
    




#徽商银行
def b26():
    global hq
    global dq03
    global dq06
    global dq1
    global dq2
    global dq3
    global dq5
    global lc1
    global lc3
    global lc5
    global dh03
    global dh03
    global dh06
    global dh1
    global xd
    global tz1
    global tz7
    global bank
    bank="徽商银行"
    r=s.get('http://www.hsbank.com.cn/extend/rmbsavequery.esp').content
    html=etree.HTML(r)
    hq="".join(html.xpath('/html/body/form/center/table[1]/tr[3]/td[2]/text()'))
    dq03="".join(html.xpath('/html/body/form/center/table[1]/tr[6]/td[2]/text()'))
    dq06="".join(html.xpath('/html/body/form/center/table[1]/tr[7]/td[2]/text()'))
    dq1="".join(html.xpath('/html/body/form/center/table[1]/tr[8]/td[2]/text()'))
    dq2="".join(html.xpath('/html/body/form/center/table[1]/tr[9]/td[2]/text()'))
    dq3="".join(html.xpath('/html/body/form/center/table[1]/tr[10]/td[2]/text()'))
    dq5="".join(html.xpath('/html/body/form/center/table[1]/tr[11]/td[2]/text()'))
    lc1="".join(html.xpath('/html/body/form/center/table[1]/tr[13]/td[2]/text()'))
    lc3="".join(html.xpath('/html/body/form/center/table[1]/tr[14]/td[2]/text()'))
    lc5="".join(html.xpath('/html/body/form/center/table[1]/tr[15]/td[2]/text()'))
    dh03=0.6*float(dq03)
    dh06=0.6*float(dq06)
    dh1=0.6*float(dq1)
    xd="".join(html.xpath('/html/body/form/center/table[1]/tr[17]/td[2]/text()'))
    tz1="".join(html.xpath('/html/body/form/center/table[1]/tr[19]/td[2]/text()'))
    tz7="".join(html.xpath('/html/body/form/center/table[1]/tr[20]/td[2]/text()'))
    cs()

#盛京银行
def b27():
    global hq
    global dq03
    global dq06
    global dq1
    global dq2
    global dq3
    global dq5
    global lc1
    global lc3
    global lc5
    global dh03
    global dh03
    global dh06
    global dh1
    global xd
    global tz1
    global tz7
    global bank
    bank="盛京银行"
    r=s.get('http://www.shengjingbank.com.cn/sy/bjtd/cdkll/index.shtml').content
    html=etree.HTML(r)
    hq="".join(html.xpath('/html/body/div[4]/div/div[4]/table/tbody/tr[2]/td[2]/text()'))
    dq03="".join(html.xpath('/html/body/div[4]/div/div[4]/table/tbody/tr[5]/td[2]/text()'))
    dq06="".join(html.xpath('/html/body/div[4]/div/div[4]/table/tbody/tr[6]/td[2]/text()'))
    dq1="".join(html.xpath('/html/body/div[4]/div/div[4]/table/tbody/tr[7]/td[2]/text()'))
    dq2="".join(html.xpath('/html/body/div[4]/div/div[4]/table/tbody/tr[8]/td[2]/text()'))
    dq3="".join(html.xpath('/html/body/div[4]/div/div[4]/table/tbody/tr[9]/td[2]/text()'))
    dq5="".join(html.xpath('/html/body/div[4]/div/div[4]/table/tbody/tr[10]/td[2]/text()'))
    lc1="".join(html.xpath('/html/body/div[4]/div/div[4]/table/tbody/tr[12]/td[2]/text()'))
    lc3="".join(html.xpath('/html/body/div[4]/div/div[4]/table/tbody/tr[13]/td[2]/text()'))
    lc5="".join(html.xpath('/html/body/div[4]/div/div[4]/table/tbody/tr[14]/td[2]/text()'))
    dh03=0.6*float(dq03)
    dh06=0.6*float(dq06)
    dh1=0.6*float(dq1)
    xd="".join(html.xpath('/html/body/div[4]/div/div[4]/table/tbody/tr[16]/td[2]/text()'))
    tz1="".join(html.xpath('/html/body/div[4]/div/div[4]/table/tbody/tr[18]/td[2]/text()'))
    tz7="".join(html.xpath('/html/body/div[4]/div/div[4]/table/tbody/tr[19]/td[2]/text()'))
    cs()

#广州银行
def b28():
    global hq
    global dq03
    global dq06
    global dq1
    global dq2
    global dq3
    global dq5
    global lc1
    global lc3
    global lc5
    global dh03
    global dh03
    global dh06
    global dh1
    global xd
    global tz1
    global tz7
    global bank
    bank="广州银行"

    r=s.get('http://www.gzcb.com.cn/flbz/ckllb/index.shtml').content
    html=etree.HTML(r)
    hq="".join(html.xpath('//*[@id="SwitchContent1"]/span/table/tbody/tr[3]/td[2]/p/span/text()')).strip()
    dq03="".join(html.xpath('//*[@id="SwitchContent1"]/span/table/tbody/tr[6]/td[2]/p/span/text()')).strip()
    dq06="".join(html.xpath('//*[@id="SwitchContent1"]/span/table/tbody/tr[7]/td[2]/p/span/text()')).strip()
    dq1="".join(html.xpath('//*[@id="SwitchContent1"]/span/table/tbody/tr[8]/td[2]/p/span/text()')).strip()
    dq2="".join(html.xpath('//*[@id="SwitchContent1"]/span/table/tbody/tr[9]/td[2]/p/span/text()')).strip()
    dq3="".join(html.xpath('//*[@id="SwitchContent1"]/span/table/tbody/tr[10]/td[2]/p/span/text()')).strip()
    dq5="".join(html.xpath('//*[@id="SwitchContent1"]/span/table/tbody/tr[11]/td[2]/p/span/text()')).strip()
    lc1="".join(html.xpath('//*[@id="SwitchContent1"]/span/table/tbody/tr[13]/td[2]/p/span/text()')).strip()
    lc3="".join(html.xpath('//*[@id="SwitchContent1"]/span/table/tbody/tr[14]/td[2]/p/span/text()')).strip()
    lc5="".join(html.xpath('//*[@id="SwitchContent1"]/span/table/tbody/tr[15]/td[2]/p/span/text()')).strip()
    dh03=0.6*float(dq03)
    dh06=0.6*float(dq06)
    dh1=0.6*float(dq1)
    xd="".join(html.xpath('//*[@id="SwitchContent1"]/span/table/tbody/tr[17]/td[2]/p/span/text()')).strip()
    tz1="".join(html.xpath('//*[@id="SwitchContent1"]/span/table/tbody/tr[19]/td[2]/p/span/text()')).strip()
    tz7="".join(html.xpath('//*[@id="SwitchContent1"]/span/table/tbody/tr[20]/td[2]/p/span/text()')).strip()
    cs()

#天津银行
def b29():
    global hq
    global dq03
    global dq06
    global dq1
    global dq2
    global dq3
    global dq5
    global lc1
    global lc3
    global lc5
    global dh03
    global dh03
    global dh06
    global dh1
    global xd
    global tz1
    global tz7
    global bank
    bank="天津银行"
    r=s.get('http://www.bank-of-tianjin.com.cn/grjr/bjfw/ckll/268298.shtml').content
    html=etree.HTML(r)
    hq="".join(html.xpath('/html/body/div[4]/div/table/tbody/tr[5]/td[2]/div/text()')).strip()
    dq03="".join(html.xpath('/html/body/div[4]/div/table/tbody/tr[8]/td[2]/div/text()')).strip()
    dq06="".join(html.xpath('/html/body/div[4]/div/table/tbody/tr[9]/td[2]/div/text()')).strip()
    dq1="".join(html.xpath('/html/body/div[4]/div/table/tbody/tr[10]/td[2]/div/text()')).strip()
    dq2="".join(html.xpath('/html/body/div[4]/div/table/tbody/tr[11]/td[2]/div/text()')).strip()
    dq3="".join(html.xpath('/html/body/div[4]/div/table/tbody/tr[12]/td[2]/div/text()')).strip()
    dq5="".join(html.xpath('/html/body/div[4]/div/table/tbody/tr[13]/td[2]/div/text()')).strip()
    lc1="".join(html.xpath('/html/body/div[4]/div/table/tbody/tr[15]/td[2]/div/text()')).strip()
    lc3="".join(html.xpath('/html/body/div[4]/div/table/tbody/tr[16]/td[2]/div/text()')).strip()
    lc5="".join(html.xpath('/html/body/div[4]/div/table/tbody/tr[17]/td[2]/div/text()')).strip()
    dh03=0.6*float(dq03)
    dh06=0.6*float(dq06)
    dh1=0.6*float(dq1)
    xd="".join(html.xpath('/html/body/div[4]/div/table/tbody/tr[19]/td[2]/div/text()')).strip()
    tz1="".join(html.xpath('/html/body/div[4]/div/table/tbody/tr[21]/td[2]/div/text()')).strip()
    tz7="".join(html.xpath('/html/body/div[4]/div/table/tbody/tr[22]/td[2]/div/text()')).strip()
    cs()
    
#花旗银行 (图片)
def b30():
    r=s.get('https://www.citibank.com.cn/sim/chinese/static/rates_fees.htm').content
    html=etree.HTML(r)
    hq="".join(html.xpath('/html/body/div[4]/div/table/tbody/tr[5]/td[2]/div/text()')).strip()

#青岛银行
def b31():
    global hq
    global dq03
    global dq06
    global dq1
    global dq2
    global dq3
    global dq5
    global lc1
    global lc3
    global lc5
    global dh03
    global dh03
    global dh06
    global dh1
    global xd
    global tz1
    global tz7
    global bank
    bank="青岛银行"
    r=s.get('http://www.qdccb.com/cyfw/cdkll/rmbckll/index.shtml').content
    html=etree.HTML(r)
    hq="".join(html.xpath('/html/body/div[4]/div[3]/div[1]/table[1]/tbody/tr[3]/td[2]/text()')).strip().replace("%","")
    dq03="".join(html.xpath('/html/body/div[4]/div[3]/div[1]/table[1]/tbody/tr[6]/td[2]/text()')).strip().replace("%","")
    dq06="".join(html.xpath('/html/body/div[4]/div[3]/div[1]/table[1]/tbody/tr[7]/td[2]/text()')).strip().replace("%","")
    dq1="".join(html.xpath('/html/body/div[4]/div[3]/div[1]/table[1]/tbody/tr[8]/td[2]/text()')).strip().replace("%","")
    dq2="".join(html.xpath('/html/body/div[4]/div[3]/div[1]/table[1]/tbody/tr[9]/td[2]/text()')).strip().replace("%","")
    dq3="".join(html.xpath('/html/body/div[4]/div[3]/div[1]/table[1]/tbody/tr[10]/td[2]/text()')).strip().replace("%","")
    dq5="".join(html.xpath('/html/body/div[4]/div[3]/div[1]/table[1]/tbody/tr[11]/td[2]/text()')).strip().replace("%","")
    lc1="".join(html.xpath('/html/body/div[4]/div[3]/div[1]/table[1]/tbody/tr[13]/td[2]/text()')).strip().replace("%","")
    lc3="".join(html.xpath('/html/body/div[4]/div[3]/div[1]/table[1]/tbody/tr[14]/td[2]/text()')).strip().replace("%","")
    lc5="".join(html.xpath('/html/body/div[4]/div[3]/div[1]/table[1]/tbody/tr[15]/td[2]/text()')).strip().replace("%","")
    dh03=0.6*float(dq03)
    dh06=0.6*float(dq06)
    dh1=0.6*float(dq1)
    xd="-"
    tz1="".join(html.xpath('/html/body/div[4]/div[3]/div[1]/table[1]/tbody/tr[18]/td[2]/text()')).strip().replace("%","")
    tz7="".join(html.xpath('/html/body/div[4]/div[3]/div[1]/table[1]/tbody/tr[19]/td[2]/text()')).strip().replace("%","")
    cs()

#齐鲁银行
def b32():
    global hq
    global dq03
    global dq06
    global dq1
    global dq2
    global dq3
    global dq5
    global lc1
    global lc3
    global lc5
    global dh03
    global dh03
    global dh06
    global dh1
    global xd
    global tz1
    global tz7
    global bank
    bank="齐鲁银行"
    r=s.get('http://www.qlbchina.com/jsp/new/common/neirong.jsp?content=/CMS5_G20306002Resource?info=2295982;res=c1444391104124_0').content
    html=etree.HTML(r)
    hq="".join(html.xpath('/html/body/div[1]/table/tbody/tr[4]/td[2]/p/span/text()')).strip()
    dq03="".join(html.xpath('/html/body/div[1]/table/tbody/tr[6]/td[2]/p/span/text()')).strip()
    dq06="".join(html.xpath('/html/body/div[1]/table/tbody/tr[7]/td[2]/p/span/text()')).strip()
    dq1="".join(html.xpath('/html/body/div[1]/table/tbody/tr[8]/td[2]/p/span/text()')).strip()
    dq2="".join(html.xpath('/html/body/div[1]/table/tbody/tr[9]/td[2]/p/span/text()')).strip()
    dq3="".join(html.xpath('/html/body/div[1]/table/tbody/tr[10]/td[2]/p/span/text()')).strip()
    dq5="".join(html.xpath('/html/body/div[1]/table/tbody/tr[11]/td[2]/p/span/text()')).strip()
    lc1="".join(html.xpath('/html/body/div[1]/table/tbody/tr[13]/td[2]/p/span/text()')).strip()
    lc3="".join(html.xpath('/html/body/div[1]/table/tbody/tr[14]/td[2]/p/span/text()')).strip()
    lc5="".join(html.xpath('/html/body/div[1]/table/tbody/tr[15]/td[2]/p/span/text()')).strip()
    dh03=0.6*float(dq03)
    dh06=0.6*float(dq06)
    dh1=0.6*float(dq1)
    xd="-"
    tz1="".join(html.xpath('/html/body/div[1]/table/tbody/tr[19]/td[2]/p/span/text()')).strip()
    tz7="".join(html.xpath('/html/body/div[1]/table/tbody/tr[20]/td[2]/p/span/text()')).strip()
    cs()

#湖北银行
def b33():
    global hq
    global dq03
    global dq06
    global dq1
    global dq2
    global dq3
    global dq5
    global lc1
    global lc3
    global lc5
    global dh03
    global dh03
    global dh06
    global dh1
    global xd
    global tz1
    global tz7
    global bank
    bank="湖北银行"
    r=s.get('http://www.hubeibank.cn/cn/kjfw/cdkllxx/241.html').content
    html=etree.HTML(r)
    hq="".join(html.xpath('//*[@id="contentDiv"]/table/tbody/tr[2]/td[2]/text()')).strip()
    dq03="".join(html.xpath('//*[@id="contentDiv"]/table/tbody/tr[3]/td[2]/text()')).strip()
    dq06="".join(html.xpath('//*[@id="contentDiv"]/table/tbody/tr[4]/td[2]/text()')).strip()
    dq1="".join(html.xpath('//*[@id="contentDiv"]/table/tbody/tr[5]/td[2]/text()')).strip()
    dq2="".join(html.xpath('//*[@id="contentDiv"]/table/tbody/tr[6]/td[2]/text()')).strip()
    dq3="".join(html.xpath('//*[@id="contentDiv"]/table/tbody/tr[7]/td[2]/text()')).strip()
    dq5="".join(html.xpath('//*[@id="contentDiv"]/table/tbody/tr[8]/td[2]/text()')).strip()
    lc1="".join(html.xpath('//*[@id="contentDiv"]/table/tbody/tr[9]/td[2]/text()')).strip()
    lc3="".join(html.xpath('//*[@id="contentDiv"]/table/tbody/tr[10]/td[2]/text()')).strip()
    lc5="".join(html.xpath('//*[@id="contentDiv"]/table/tbody/tr[11]/td[2]/text()')).strip()
    dh03=0.6*float(dq03)
    dh06=0.6*float(dq06)
    dh1=0.6*float(dq1)
    xd="".join(html.xpath('//*[@id="contentDiv"]/table/tbody/tr[13]/td[2]/text()')).strip()
    tz1="".join(html.xpath('//*[@id="contentDiv"]/table/tbody/tr[14]/td[2]/text()')).strip()
    tz7="".join(html.xpath('//*[@id="contentDiv"]/table/tbody/tr[15]/td[2]/text()')).strip()
    cs()

#武汉农村商业银行(图片)
#汉口银行（图片）
#郑州银行
def b36():
    global hq
    global dq03
    global dq06
    global dq1
    global dq2
    global dq3
    global dq5
    global lc1
    global lc3
    global lc5
    global dh03
    global dh03
    global dh06
    global dh1
    global xd
    global tz1
    global tz7
    global bank
    bank="郑州银行"
    r=s.get('http://www.zzbank.cn/ck.html').content
    html=etree.HTML(r)
    hq="".join(html.xpath('//*[@id="mainBox"]/div[5]/div/div[2]/div/div/div[1]/div/table/tbody/tr[7]/td[3]/text()')).strip()
    dq03="".join(html.xpath('//*[@id="mainBox"]/div[5]/div/div[2]/div/div/div[1]/div/table/tbody/tr[10]/td[3]/text()')).strip()
    dq06="".join(html.xpath('//*[@id="mainBox"]/div[5]/div/div[2]/div/div/div[1]/div/table/tbody/tr[11]/td[3]/text()')).strip()
    dq1="".join(html.xpath('//*[@id="mainBox"]/div[5]/div/div[2]/div/div/div[1]/div/table/tbody/tr[12]/td[3]/text()')).strip()
    dq2="".join(html.xpath('//*[@id="mainBox"]/div[5]/div/div[2]/div/div/div[1]/div/table/tbody/tr[13]/td[3]/text()')).strip()
    dq3="".join(html.xpath('//*[@id="mainBox"]/div[5]/div/div[2]/div/div/div[1]/div/table/tbody/tr[14]/td[3]/text()')).strip()
    dq5="".join(html.xpath('//*[@id="mainBox"]/div[5]/div/div[2]/div/div/div[1]/div/table/tbody/tr[15]/td[3]/text()')).strip()
    lc1="".join(html.xpath('//*[@id="mainBox"]/div[5]/div/div[2]/div/div/div[1]/div/table/tbody/tr[17]/td[3]/text()')).strip()
    lc3="".join(html.xpath('//*[@id="mainBox"]/div[5]/div/div[2]/div/div/div[1]/div/table/tbody/tr[18]/td[3]/text()')).strip()
    lc5="".join(html.xpath('//*[@id="mainBox"]/div[5]/div/div[2]/div/div/div[1]/div/table/tbody/tr[19]/td[3]/text()')).strip()
    dh03=0.6*float(dq03)
    dh06=0.6*float(dq06)
    dh1=0.6*float(dq1)
    xd="".join(html.xpath('//*[@id="mainBox"]/div[5]/div/div[2]/div/div/div[1]/div/table/tbody/tr[21]/td[3]/text()')).strip()
    tz1="".join(html.xpath('//*[@id="mainBox"]/div[5]/div/div[2]/div/div/div[1]/div/table/tbody/tr[23]/td[3]/text()')).strip()
    tz7="".join(html.xpath('//*[@id="mainBox"]/div[5]/div/div[2]/div/div/div[1]/div/table/tbody/tr[24]/td[3]/text()')).strip()
    cs()
#长沙银行
def b37():
    global hq
    global dq03
    global dq06
    global dq1
    global dq2
    global dq3
    global dq5
    global lc1
    global lc3
    global lc5
    global dh03
    global dh03
    global dh06
    global dh1
    global xd
    global tz1
    global tz7
    global bank
    bank="长沙银行"
    r=s.get('http://www.cscb.cn/investmentFinancing/ratelist/depositrate/content_3394.html').content
    html=etree.HTML(r)
    hq="".join(html.xpath('//*[@id="zoom"]/table/tbody/tr[2]/td[4]/p/span[1]/text()')).strip()
    dq03="".join(html.xpath('//*[@id="zoom"]/table/tbody/tr[3]/td[4]/p/span[1]/text()')).strip()
    dq06="".join(html.xpath('//*[@id="zoom"]/table/tbody/tr[4]/td[3]/p/span[1]/text()')).strip()
    dq1="".join(html.xpath('//*[@id="zoom"]/table/tbody/tr[5]/td[3]/p/span[1]/text()')).strip()
    dq2="".join(html.xpath('//*[@id="zoom"]/table/tbody/tr[6]/td[3]/p/span[1]/text()')).strip()
    dq3="".join(html.xpath('//*[@id="zoom"]/table/tbody/tr[7]/td[3]/p/span[1]/text()')).strip()
    dq5="".join(html.xpath('//*[@id="zoom"]/table/tbody/tr[8]/td[3]/p/span[1]/text()')).strip()
    lc1="".join(html.xpath('//*[@id="zoom"]/table/tbody/tr[9]/td[4]/p/span[1]/text()')).strip()
    lc3="".join(html.xpath('//*[@id="zoom"]/table/tbody/tr[10]/td[4]/p/span[1]/text()')).strip()
    lc5="-"
    dh03=0.6*float(dq03)
    dh06=0.6*float(dq06)
    dh1=0.6*float(dq1) 
    xd="-"
    tz1="".join(html.xpath('//*[@id="zoom"]/table/tbody/tr[13]/td[4]/p/span[1]/text()')).strip()
    tz7="".join(html.xpath('//*[@id="zoom"]/table/tbody/tr[14]/td[3]/p/span[1]/text()')).strip()
    cs()
#华融湘江银行
def b38():
    global hq
    global dq03
    global dq06
    global dq1
    global dq2
    global dq3
    global dq5
    global lc1
    global lc3
    global lc5
    global dh03
    global dh03
    global dh06
    global dh1
    global xd
    global tz1
    global tz7
    global bank
    bank="华融湘江银行"
    r=s.get('http://www.hrxjbank.com.cn/246/248/286/content_4311.html').content
    html=etree.HTML(r)
    hq="".join(html.xpath('//table[@style="TEXT-ALIGN: center; WIDTH: 649px; BORDER-COLLAPSE: collapse; HEIGHT: 502px"]/tbody/tr[2]/td[3]/text()')).strip()
    dq03="".join(html.xpath('//table[@style="TEXT-ALIGN: center; WIDTH: 649px; BORDER-COLLAPSE: collapse; HEIGHT: 502px"]/tbody/tr[5]/td[3]/text()')).strip()
    dq06="".join(html.xpath('//table[@style="TEXT-ALIGN: center; WIDTH: 649px; BORDER-COLLAPSE: collapse; HEIGHT: 502px"]/tbody/tr[6]/td[3]/text()')).strip()
    dq1="".join(html.xpath('//table[@style="TEXT-ALIGN: center; WIDTH: 649px; BORDER-COLLAPSE: collapse; HEIGHT: 502px"]/tbody/tr[7]/td[3]/text()')).strip()
    dq2="".join(html.xpath('//table[@style="TEXT-ALIGN: center; WIDTH: 649px; BORDER-COLLAPSE: collapse; HEIGHT: 502px"]/tbody/tr[8]/td[3]/text()')).strip()
    dq3="".join(html.xpath('//table[@style="TEXT-ALIGN: center; WIDTH: 649px; BORDER-COLLAPSE: collapse; HEIGHT: 502px"]/tbody/tr[9]/td[3]/text()')).strip()
    dq5="".join(html.xpath('//table[@style="TEXT-ALIGN: center; WIDTH: 649px; BORDER-COLLAPSE: collapse; HEIGHT: 502px"]/tbody/tr[10]/td[3]/text()')).strip()
    lc1="".join(html.xpath('//table[@style="TEXT-ALIGN: center; WIDTH: 649px; BORDER-COLLAPSE: collapse; HEIGHT: 502px"]/tbody/tr[12]/td[3]/text()')).strip()
    lc3="".join(html.xpath('//table[@style="TEXT-ALIGN: center; WIDTH: 649px; BORDER-COLLAPSE: collapse; HEIGHT: 502px"]/tbody/tr[13]/td[3]/text()')).strip()
    lc5="".join(html.xpath('//table[@style="TEXT-ALIGN: center; WIDTH: 649px; BORDER-COLLAPSE: collapse; HEIGHT: 502px"]/tbody/tr[14]/td[3]/text()')).strip()
    dh03=0.6*float(dq03)
    dh06=0.6*float(dq06)
    dh1=0.6*float(dq1)
    xd="".join(html.xpath('//table[@style="TEXT-ALIGN: center; WIDTH: 649px; BORDER-COLLAPSE: collapse; HEIGHT: 502px"]/tbody/tr[17]/td[3]/text()')).strip()
    tz1="".join(html.xpath('//table[@style="TEXT-ALIGN: center; WIDTH: 649px; BORDER-COLLAPSE: collapse; HEIGHT: 502px"]/tbody/tr[19]/td[3]/text()')).strip()
    tz7="".join(html.xpath('//table[@style="TEXT-ALIGN: center; WIDTH: 649px; BORDER-COLLAPSE: collapse; HEIGHT: 502px"]/tbody/tr[20]/td[3]/text()')).strip()
    cs()

#西安银行
def b39():
    global hq
    global dq03
    global dq06
    global dq1
    global dq2
    global dq3
    global dq5
    global lc1
    global lc3
    global lc5
    global dh03
    global dh03
    global dh06
    global dh1
    global xd
    global tz1
    global tz7
    global bank
    bank="西安银行"
    r=s.get('http://www.xacbank.com/icms/static/xacbank/zh/3ud5d2lv/raf5pw9d/xfbkdb47/205012/content/40288d8b4f5f6df5014f670987e50068.html').content
    html=etree.HTML(r)
    hq="".join(html.xpath('/html/body/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[2]/td[3]/p/span/text()')).strip()
    dq03="".join(html.xpath('/html/body/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[5]/td[3]/p/span/text()')).strip()
    dq06="".join(html.xpath('/html/body/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[6]/td[3]/p/span/text()')).strip()
    dq1="".join(html.xpath('/html/body/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[7]/td[3]/p/span/text()')).strip()
    dq2="".join(html.xpath('/html/body/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[8]/td[3]/p/span/text()')).strip()
    dq3="".join(html.xpath('/html/body/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[9]/td[3]/p/span/text()')).strip()
    dq5="".join(html.xpath('/html/body/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[10]/td[3]/p/span/text()')).strip()
    lc1="".join(html.xpath('/html/body/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[12]/td[3]/p/span/text()')).strip()
    lc3="".join(html.xpath('/html/body/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[13]/td[3]/p/span/text()')).strip()
    lc5="".join(html.xpath('/html/body/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[14]/td[3]/p/span/text()')).strip()
    dh03=0.6*float(dq03)
    dh06=0.6*float(dq06)
    dh1=0.6*float(dq1)
    xd="".join(html.xpath('/html/body/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[16]/td[3]/p/span/text()')).strip()
    tz1="".join(html.xpath('/html/body/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[18]/td[3]/p/span/text()')).strip()
    tz7="".join(html.xpath('/html/body/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[19]/td[3]/p/span/text()')).strip()
    cs()
# 长安银行
def b40():
    global hq
    global dq03
    global dq06
    global dq1
    global dq2
    global dq3
    global dq5
    global lc1
    global lc3
    global lc5
    global dh03
    global dh03
    global dh06
    global dh1
    global xd
    global tz1
    global tz7
    global bank
    bank="长安银行"
    r=s.get('http://www.ccabchina.com/index/cklv.htm').content
    html=etree.HTML(r)
    hq="".join(html.xpath('//*[@id="vsb_content"]/table/tbody/tr[6]/td[4]/span/text()')).strip()
    dq03="".join(html.xpath('//*[@id="vsb_content"]/table/tbody/tr[9]/td[4]/span/text()')).strip()
    dq06="".join(html.xpath('//*[@id="vsb_content"]/table/tbody/tr[10]/td[4]/span/text()')).strip()
    dq1="".join(html.xpath('//*[@id="vsb_content"]/table/tbody/tr[11]/td[4]/span/text()')).strip()
    dq2="".join(html.xpath('//*[@id="vsb_content"]/table/tbody/tr[12]/td[4]/span/text()')).strip()
    dq3="".join(html.xpath('//*[@id="vsb_content"]/table/tbody/tr[13]/td[4]/span/text()')).strip()
    dq5="".join(html.xpath('//*[@id="vsb_content"]/table/tbody/tr[14]/td[4]/span/text()')).strip()
    lc1="".join(html.xpath('//*[@id="vsb_content"]/table/tbody/tr[16]/td[4]/span/text()')).strip()
    lc3="".join(html.xpath('//*[@id="vsb_content"]/table/tbody/tr[17]/td[4]/span/text()')).strip()
    lc5="".join(html.xpath('//*[@id="vsb_content"]/table/tbody/tr[18]/td[4]/span/text()')).strip()
    dh03=0.6*float(dq03)
    dh06=0.6*float(dq06)
    dh1=0.6*float(dq1)
    xd="".join(html.xpath('//*[@id="vsb_content"]/table/tbody/tr[20]/td[4]/span/text()')).strip()
    tz1="".join(html.xpath('//*[@id="vsb_content"]/table/tbody/tr[22]/td[4]/span/text()')).strip()
    tz7="".join(html.xpath('//*[@id="vsb_content"]/table/tbody/tr[23]/td[4]/span/text()')).strip()
    cs()

#昆仑银行    
def b41():
    global hq
    global dq03
    global dq06
    global dq1
    global dq2
    global dq3
    global dq5
    global lc1
    global lc3
    global lc5
    global dh03
    global dh03
    global dh06
    global dh1
    global xd
    global tz1
    global tz7
    global bank
    bank="昆仑银行"
    r=s.get('http://www.klb.cn/eportal/ui?pageId=491117').content
    html=etree.HTML(r)
    hq="".join(html.xpath('//input[@id="cklv_S1_0_Y_01"]/@value')).strip()
    dq03="".join(html.xpath('//input[@id="cklv_T1_3_M_01"]/@value')).strip()
    dq06="".join(html.xpath('//input[@id="cklv_T1_6_M_01"]/@value')).strip()
    dq1="".join(html.xpath('//input[@id="cklv_T1_1_Y_01"]/@value')).strip()
    dq2="".join(html.xpath('//input[@id="cklv_T1_2_Y_01"]/@value')).strip()
    dq3="".join(html.xpath('//input[@id="cklv_T1_3_Y_01"]/@value')).strip()
    dq5="".join(html.xpath('//input[@id="cklv_T1_5_Y_01"]/@value')).strip()
    lc1="".join(html.xpath('//input[@id="cklv_T2_1_Y_01"]/@value')).strip()
    lc3="".join(html.xpath('//input[@id="cklv_T2_3_Y_01"]/@value')).strip()
    lc5="".join(html.xpath('//input[@id="cklv_T2_5_Y_01"]/@value')).strip()
    dh03=0.6*float(dq03)
    dh06=0.6*float(dq06)
    dh1=0.6*float(dq1)
    xd="-"
    tz1="".join(html.xpath('//input[@id="cklv_T5_1_D_01"]/@value')).strip()
    tz7="".join(html.xpath('//input[@id="cklv_T5_7_D_01"]/@value')).strip()
    cs()
   
#哈尔滨银行
def b42():
    global hq
    global dq03
    global dq06
    global dq1
    global dq2
    global dq3
    global dq5
    global lc1
    global lc3
    global lc5
    global dh03
    global dh03
    global dh06
    global dh1
    global xd
    global tz1
    global tz7
    global bank
    bank="哈尔滨银行"
    r=s.get('http://www.hrbcb.com.cn/index.do?method=saver').content
    html=etree.HTML(r)
    hq="".join(html.xpath('//table[@width="745"]/tr[3]/td[2]/text()')).strip()
    dq03="".join(html.xpath('//table[@width="745"]/tr[6]/td[2]/text()')).strip()
    dq06="".join(html.xpath('//table[@width="745"]/tr[7]/td[2]/text()')).strip()
    dq1="".join(html.xpath('//table[@width="745"]/tr[8]/td[2]/text()')).strip()
    dq2="".join(html.xpath('//table[@width="745"]/tr[9]/td[2]/text()')).strip()
    dq3="".join(html.xpath('//table[@width="745"]/tr[10]/td[2]/text()')).strip()
    dq5="".join(html.xpath('//table[@width="745"]/tr[11]/td[2]/text()')).strip()
    lc1="".join(html.xpath('//table[@width="745"]/tr[13]/td[2]/text()')).strip()
    lc3="".join(html.xpath('//table[@width="745"]/tr[14]/td[2]/text()')).strip()
    lc5="".join(html.xpath('//table[@width="745"]/tr[15]/td[2]/text()')).strip()
    dh03=0.6*float(dq03)
    dh06=0.6*float(dq06)
    dh1=0.6*float(dq1)
    xd="-"
    tz1="".join(html.xpath('//table[@width="745"]/tr[18]/td[2]/text()')).strip()
    tz7="".join(html.xpath('//table[@width="745"]/tr[19]/td[2]/text()')).strip()
    cs()
    
    

#龙江银行
def b43():
    global hq
    global dq03
    global dq06
    global dq1
    global dq2
    global dq3
    global dq5
    global lc1
    global lc3
    global lc5
    global dh03
    global dh03
    global dh06
    global dh1
    global xd
    global tz1
    global tz7
    global bank
    bank="龙江银行"
    r=s.get('http://www.lj-bank.com/list.php?tid=16').content
    html=etree.HTML(r)
    hq="".join(html.xpath('//div[@class="sc_news_con2"]/table/tbody/tr[2]/td[2]/p/text()')).strip()
    dq03="".join(html.xpath('//div[@class="sc_news_con2"]/table/tbody/tr[5]/td[2]/p/text()')).strip()
    dq06="".join(html.xpath('//div[@class="sc_news_con2"]/table/tbody/tr[6]/td[2]/p/text()')).strip()
    dq1="".join(html.xpath('//div[@class="sc_news_con2"]/table/tbody/tr[7]/td[2]/p/text()')).strip()
    dq2="".join(html.xpath('//div[@class="sc_news_con2"]/table/tbody/tr[8]/td[2]/p/text()')).strip()
    dq3="".join(html.xpath('//div[@class="sc_news_con2"]/table/tbody/tr[9]/td[2]/p/text()')).strip()
    dq5="".join(html.xpath('//div[@class="sc_news_con2"]/table/tbody/tr[10]/td[2]/p/text()')).strip()
    lc1="".join(html.xpath('//div[@class="sc_news_con2"]/table/tbody/tr[12]/td[2]/p/text()')).strip()
    lc3="".join(html.xpath('//div[@class="sc_news_con2"]/table/tbody/tr[13]/td[2]/p/text()')).strip()
    lc5="".join(html.xpath('//div[@class="sc_news_con2"]/table/tbody/tr[14]/td[2]/p/text()')).strip()
    dh03=0.6*float(dq03)
    dh06=0.6*float(dq06)
    dh1=0.6*float(dq1)
    xd="".join(html.xpath('//div[@class="sc_news_con2"]/table/tbody/tr[16]/td[2]/p/text()')).strip()
    tz1="".join(html.xpath('//div[@class="sc_news_con2"]/table/tbody/tr[18]/td[2]/p/text()')).strip()
    tz7="".join(html.xpath('//div[@class="sc_news_con2"]/table/tbody/tr[19]/td[2]/p/text()')).strip()
    cs()
#杭州银行（需要伪装一下）
def b44():
    global hq
    global dq03
    global dq06
    global dq1
    global dq2
    global dq3
    global dq5
    global lc1
    global lc3
    global lc5
    global dh03
    global dh03
    global dh06
    global dh1
    global xd
    global tz1
    global tz7
    global bank
    bank="杭州银行"
    header={
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Cookie':'Hm_lvt_a1e1555cbc42019e8f16a6b443b18c3e=1474180724',
    'Host':'www.hzbank.com.cn',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }
    r=s.get('http://www.hzbank.com.cn/lcgj/cdll/rmbckjzllb/index.shtml',headers=header).content
    html=etree.HTML(r)
    hq="".join(html.xpath('//div[@class="newsDetail"]//table/tbody/tr[4]/td[2]/p/text()')).strip()
    dq03="".join(html.xpath('//div[@class="newsDetail"]//table/tbody/tr[7]/td[2]/p/text()')).strip()
    dq06="".join(html.xpath('//div[@class="newsDetail"]//table/tbody/tr[8]/td[2]/p/text()')).strip()
    dq1="".join(html.xpath('//div[@class="newsDetail"]//table/tbody/tr[9]/td[2]/p/text()')).strip()
    dq2="".join(html.xpath('//div[@class="newsDetail"]//table/tbody/tr[10]/td[2]/p/text()')).strip()
    dq3="".join(html.xpath('//div[@class="newsDetail"]//table/tbody/tr[11]/td[2]/p/text()')).strip()
    dq5="".join(html.xpath('//div[@class="newsDetail"]//table/tbody/tr[12]/td[2]/p/text()')).strip()
    lc1="".join(html.xpath('//div[@class="newsDetail"]//table/tbody/tr[14]/td[2]/p/text()')).strip()
    lc3="".join(html.xpath('//div[@class="newsDetail"]//table/tbody/tr[15]/td[2]/p/text()')).strip()
    lc5="".join(html.xpath('//div[@class="newsDetail"]//table/tbody/tr[16]/td[2]/p/text()')).strip()
    dh03=0.6*float(dq03)
    dh06=0.6*float(dq06)
    dh1=0.6*float(dq1)
    xd="".join(html.xpath('//div[@class="newsDetail"]//table/tbody/tr[18]/td[2]/p/text()')).strip()
    tz1="".join(html.xpath('//div[@class="newsDetail"]//table/tbody/tr[20]/td[2]/p/text()')).strip()
    tz7="".join(html.xpath('//div[@class="newsDetail"]//table/tbody/tr[21]/td[2]/p/text()')).strip()
    cs()
    


#南昌银行(江西银行)
def b45():
    global hq
    global dq03
    global dq06
    global dq1
    global dq2
    global dq3
    global dq5
    global lc1
    global lc3
    global lc5
    global dh03
    global dh03
    global dh06
    global dh1
    global xd
    global tz1
    global tz7
    global bank
    bank="南昌银行"
    r=s.get('http://www.jx-bank.com/nccbank/zh_CN/home/jrsj/1382.html').content
    html=etree.HTML(r)
    hq="".join(html.xpath('//td[@class="newscontent"]/table/tbody/tr[4]/td[2]//text()')).strip()
    dq03="".join(html.xpath('//td[@class="newscontent"]/table/tbody/tr[7]/td[2]//text()')).strip()
    dq06="".join(html.xpath('//td[@class="newscontent"]/table/tbody/tr[8]/td[2]//text()')).strip()
    dq1="".join(html.xpath('//td[@class="newscontent"]/table/tbody/tr[9]/td[2]//text()')).strip()
    dq2="".join(html.xpath('//td[@class="newscontent"]/table/tbody/tr[10]/td[2]//text()')).strip()
    dq3="".join(html.xpath('//td[@class="newscontent"]/table/tbody/tr[11]/td[2]//text()')).strip()
    dq5="".join(html.xpath('//td[@class="newscontent"]/table/tbody/tr[12]/td[2]//text()')).strip()
    lc1="".join(html.xpath('//td[@class="newscontent"]/table/tbody/tr[14]/td[2]//text()')).strip()
    lc3="".join(html.xpath('//td[@class="newscontent"]/table/tbody/tr[15]/td[2]//text()')).strip()
    lc5="".join(html.xpath('//td[@class="newscontent"]/table/tbody/tr[16]/td[2]//text()')).strip()
    dh03=0.6*float(dq03)
    dh06=0.6*float(dq06)
    dh1=0.6*float(dq1)
    xd="".join(html.xpath('//td[@class="newscontent"]/table/tbody/tr[18]/td[2]//text()')).strip()
    tz1="".join(html.xpath('//td[@class="newscontent"]/table/tbody/tr[20]/td[2]//text()')).strip()
    tz7="".join(html.xpath('//td[@class="newscontent"]/table/tbody/tr[21]/td[2]//text()')).strip()
    cs()
    
#九江银行
def b46():
    global hq
    global dq03
    global dq06
    global dq1
    global dq2
    global dq3
    global dq5
    global lc1
    global lc3
    global lc5
    global dh03
    global dh03
    global dh06
    global dh1
    global xd
    global tz1
    global tz7
    global bank
    bank="九江银行"
    r=s.get('http://www.jjccb.com/portal/zh_CN/home/announcements/2977.html').content
    html=etree.HTML(r)
    hq="".join(html.xpath('//table[@class="MsoNormalTable"]/tbody/tr[3]/td[2]/p/span/font/text()')).strip()
    dq03="".join(html.xpath('//table[@class="MsoNormalTable"]/tbody/tr[6]/td[2]/p/span/font/text()')).strip()
    dq06="".join(html.xpath('//table[@class="MsoNormalTable"]/tbody/tr[7]/td[2]/p/span/font/text()')).strip()
    dq1="".join(html.xpath('//table[@class="MsoNormalTable"]/tbody/tr[8]/td[2]/p/span/font/text()')).strip()
    dq2="".join(html.xpath('//table[@class="MsoNormalTable"]/tbody/tr[9]/td[2]/p/span/font/text()')).strip()
    dq3="".join(html.xpath('//table[@class="MsoNormalTable"]/tbody/tr[10]/td[2]/p/span/font/text()')).strip()
    dq5="".join(html.xpath('//table[@class="MsoNormalTable"]/tbody/tr[11]/td[2]/p/span/font/text()')).strip()
    lc1="".join(html.xpath('//table[@class="MsoNormalTable"]/tbody/tr[13]/td[2]/p/span/font/text()')).strip()
    lc3="".join(html.xpath('//table[@class="MsoNormalTable"]/tbody/tr[14]/td[2]/p/span/font/text()')).strip()
    lc5="".join(html.xpath('//table[@class="MsoNormalTable"]/tbody/tr[15]/td[2]/p/span/font/text()')).strip()
    dh03=0.6*float(dq03)
    dh06=0.6*float(dq06)
    dh1=0.6*float(dq1)
    xd="-"
    tz1="".join(html.xpath('//table[@class="MsoNormalTable"]/tbody/tr[17]/td[2]/p/span/font/text()')).strip()
    tz7="".join(html.xpath('//table[@class="MsoNormalTable"]/tbody/tr[18]/td[2]/p/span/font/text()')).strip()
    cs()
    print hq
    print dq03
    print dq06
    print dq1
    print dq2
    print dq3
    print dq5
    print lc1
    print lc3
    print lc5
    print dh03
    print dh06
    print dh1
    print xd
    print tz1
    print tz7
   

#富滇银行  图片
#泉州银行
def b48():
    global hq
    global dq03
    global dq06
    global dq1
    global dq2
    global dq3
    global dq5
    global lc1
    global lc3
    global lc5
    global dh03
    global dh03
    global dh06
    global dh1
    global xd
    global tz1
    global tz7
    global bank
    bank="泉州银行"
    r=s.get('http://www.qzccbank.com/cn/gjx/ckll/272.html').content
    html=etree.HTML(r)
    hq="".join(html.xpath('/html/body/div[2]/div/div[2]/div[2]/div/table/tbody/tr[3]/td[2]/text()')).strip()
    dq03="".join(html.xpath('/html/body/div[2]/div/div[2]/div[2]/div/table/tbody/tr[6]/td[2]/text()')).strip()
    dq06="".join(html.xpath('/html/body/div[2]/div/div[2]/div[2]/div/table/tbody/tr[7]/td[2]/text()')).strip()
    dq1="".join(html.xpath('/html/body/div[2]/div/div[2]/div[2]/div/table/tbody/tr[8]/td[2]/text()')).strip()
    dq2="".join(html.xpath('/html/body/div[2]/div/div[2]/div[2]/div/table/tbody/tr[9]/td[2]/text()')).strip()
    dq3="".join(html.xpath('/html/body/div[2]/div/div[2]/div[2]/div/table/tbody/tr[10]/td[2]/text()')).strip()
    dq5="".join(html.xpath('/html/body/div[2]/div/div[2]/div[2]/div/table/tbody/tr[11]/td[2]/text()')).strip()
    lc1="".join(html.xpath('/html/body/div[2]/div/div[2]/div[2]/div/table/tbody/tr[13]/td[2]/text()')).strip()
    lc3="".join(html.xpath('/html/body/div[2]/div/div[2]/div[2]/div/table/tbody/tr[14]/td[2]/text()')).strip()
    lc5="-"
    dh03=0.6*float(dq03)
    dh06=0.6*float(dq06)
    dh1=0.6*float(dq1)
    xd="".join(html.xpath('/html/body/div[2]/div/div[2]/div[2]/div/table/tbody/tr[16]/td[2]/text()')).strip()
    tz1="".join(html.xpath('/html/body/div[2]/div/div[2]/div[2]/div/table/tbody/tr[18]/td[2]/text()')).strip()
    tz7="".join(html.xpath('/html/body/div[2]/div/div[2]/div[2]/div/table/tbody/tr[19]/td[2]/text()')).strip()
    cs()



#大连银行
def b49():
    global hq
    global dq03
    global dq06
    global dq1
    global dq2
    global dq3
    global dq5
    global lc1
    global lc3
    global lc5
    global dh03
    global dh03
    global dh06
    global dh1
    global xd
    global tz1
    global tz7
    global bank
    bank="大连银行"
    r=s.get('http://www.bankofdl.com/jsp/common/neirong.jsp?content=/CMS5_G20306002Resource?info=358182;res=c1462268849144_0').content
    html=etree.HTML(r)
    hq="".join(html.xpath('/html/body/div/table/tbody/tr[3]/td[2]/p/span/text()')).strip()
    dq03="".join(html.xpath('/html/body/div/table/tbody/tr[6]/td[2]/p/span/text()')).strip()
    dq06="".join(html.xpath('/html/body/div/table/tbody/tr[7]/td[2]/p/span/text()')).strip()
    dq1="".join(html.xpath('/html/body/div/table/tbody/tr[8]/td[2]/p/span/text()')).strip()
    dq2="".join(html.xpath('/html/body/div/table/tbody/tr[9]/td[2]/p/span/text()')).strip()
    dq3="".join(html.xpath('/html/body/div/table/tbody/tr[10]/td[2]/p/span/text()')).strip()
    dq5="".join(html.xpath('/html/body/div/table/tbody/tr[11]/td[2]/p/span/text()')).strip()
    lc1="".join(html.xpath('/html/body/div/table/tbody/tr[13]/td[2]/p/span/text()')).strip()
    lc3="".join(html.xpath('/html/body/div/table/tbody/tr[14]/td[2]/p/span/text()')).strip()
    lc5="".join(html.xpath('/html/body/div/table/tbody/tr[15]/td[2]/p/span/text()')).strip()
    dh03=0.6*float(dq03)
    dh06=0.6*float(dq06)
    dh1=0.6*float(dq1)
    xd="-"
    tz1="".join(html.xpath('/html/body/div/table/tbody/tr[19]/td[2]/p/span/text()')).strip()
    tz7="".join(html.xpath('/html/body/div/table/tbody/tr[20]/td[2]/p/span/text()')).strip()
    cs()
#东莞银行
def b50():
    global hq
    global dq03
    global dq06
    global dq1
    global dq2
    global dq3
    global dq5
    global lc1
    global lc3
    global lc5
    global dh03
    global dh03
    global dh06
    global dh1
    global xd
    global tz1
    global tz7
    global bank
    bank="东莞银行"
    r=s.get('http://www.dongguanbank.cn/Channel/62360').content
    html=etree.HTML(r)
    #print r真实好用自己知道要取得是不是在这里面，script标签的内容可以通过替换获得好方便
    txt="".join(html.xpath('//script[7]//text()')).strip().replace("';","&").replace("= '","&")
    hq=txt.split("&")[1]
    dq03=txt.split("&")[3]
    dq06=txt.split("&")[5]
    dq1=txt.split("&")[7]
    dq2=txt.split("&")[9]
    dq3=txt.split("&")[11]
    dq5=txt.split("&")[13]
    lc1=txt.split("&")[15]
    lc3=txt.split("&")[17]
    lc5=txt.split("&")[19]
    dh03="-"
    dh06="-"
    dh1="-"
    xd=txt.split("&")[21]
    tz1=txt.split("&")[23]
    tz7=txt.split("&")[25]
    cs()

b01()
b02()
b03()
b04()
b05()
b06()
b07()
b08()
b09()
b10()
b11()
b12()

b14()
b15()
b16()
b17()
b18()
b19()
b20()
b21()
b22()
b23()


b26()
b27()
b28()
b29()

b31()
b32()
b33()


b36()
b37()
b38()
b39()
b40()
b41()
b42()
b43()
b44()
b45()
b46()

b48()
b49()
b50()





