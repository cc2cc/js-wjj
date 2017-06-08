#coding=utf-8
import requests
import time
import sys
import json
import re
import urllib
from bs4 import BeautifulSoup
s=requests.session()
Cookies={ 
'PHPSESSID':'k13eejp4ag3rld9uvj65keg634',
'_gscu_932476488':'95265805ix8fiv13', 
'_gscbrs_932476488':'1'
}
s.cookies = requests.utils.cookiejar_from_dict(Cookies)
def lase(uid):
    
    # url='http://www.jswjj.gov.cn/office_new/eo_comm_zxnrxs.php?eo_comm_zxnrxs_biaoshi=www&eo_comm_zxnrxs_xsfs=op&eo_comm_zxnrxs_gjz=&eo_comm_zxnrxs_lmid=id100000027285&eo_comm_zxnrxs_wzid=100000027210'
    url='http://www.jswjj.gov.cn/office_new/eo_comm_zxnrxs.php'
    header={
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:50.0) Gecko/20100101 Firefox/50.0',
    'Content-Type': 'application/x-www-form-urlencoded'
    }
    # print urllib.quote(u'显示'.encode('gb2312'))
    payload={
'eo_comm_zxnrxs_biaoshi':'www',
'eo_comm_zxnrxs_xsfs':'op',
'eo_comm_zxnrxs_wzid':uid,
'eo_comm_zxnrxs_SubmitButton': u'显示'.encode('gb2312')
    }
    try:
        req=s.post(url,data=payload,headers=header,allow_redirects=False)
        req.encoding = 'gb2312'
        # print req.text
    except Exception, e:
        print Exception,":",e
        return uid
    if req.status_code!=200:
        print req.status_code
        log(uid+'\n','200.txt')
        return uid
    if 'X-UA-Compatible' in req.text:
        if (u'徐才' in req.text) or (u'才厚'  in req.text) or (u'周永'  in req.text) or (u'永康'  in req.text) or (u'薄熙'  in req.text) or (u'熙来'  in req.text) or (u'郭伯'  in req.text) or (u'伯雄'  in req.text):
            t_url='http://www.jswjj.gov.cn/office_new/eo_comm_zxnrxs.php?eo_comm_zxnrxs_biaoshi=www&eo_comm_zxnrxs_xsfs=op&eo_comm_zxnrxs_gjz=&eo_comm_zxnrxs_wzid='+uid
            result='[!]'+t_url+'\n'
            print result
            log(result,'have.txt')
        else:
            result='[*]'+uid+'\n'
            print result
            log(result,'no.txt')
    else:
        print '[!]check cookie'+uid
        exit()
        
def log(str,file):
    with open(file, 'a+') as f:
        f.write(str)
if __name__=='__main__':
    fuck=['徐才厚','周永康','薄熙来','郭伯雄']
    filepath='result_5.txt'
    with open(filepath,'r') as infile:
        for line in infile:
            uid = line.replace("\n", "").split('=')[-1]
            lase(uid)



