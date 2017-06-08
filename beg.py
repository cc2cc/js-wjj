#coding=utf-8
import requests
import time
import sys
import json
import re
from bs4 import BeautifulSoup
s=requests.session()
Cookies={ 
'PHPSESSID':'rvetml90q5ffmut531bcu0rrr6',
'_gscs_932476488':'95199530vjt9p155', 
'_gscbrs_932476488':'1'
}
s.cookies = requests.utils.cookiejar_from_dict(Cookies)
def get_text(page):
    url='http://www.jswjj.gov.cn/main/www/www_xxmlxs.php?www_xxmlxs_bh=bhwj01-000000000000&www_xxmlxs_fs=c&www_xxmlxs_js=2&www_xxmlxs_namebl=%&www_xxmlxs_qsrqbl=&www_xxmlxs_jsrqbl=&www_xxmlxs_lxmcbl=&www_xxmlxs_diqubl=&www_xxmlxs_wenhaobl=&www_xxmlxs_PAGE=1&www_xxmlxs_fh=www_main.php&eo_comm_blcl_ghcsm1=eo_comm_xxmlxs_PAGE&eo_comm_blcl_ghcsz1='+page
    header={
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:50.0) Gecko/20100101 Firefox/50.0',
    }
    req=s.get(url,headers=header)
    req.encoding = 'gb2312'
    soup = BeautifulSoup(req.text,"lxml")
    test =soup.find_all(onclick=re.compile("window.open"))
    for x in test:
        # log(x.attrs['onclick']+'\n')
        log(x.attrs['onclick'].split("'")[1]+'\n')
        # print x.attrs['onclick'].split("'")[1]
    print page,len(test)
    
def log(str):
    with open('result_5.txt', 'a+') as f:
        f.write(str)
def lase():
    url='http://www.jswjj.gov.cn/office_new/eo_comm_zxnrxs.php'
    # url='http://www.jswjj.gov.cn/office_new/eo_comm_zxnrxs.php?eo_comm_zxnrxs_biaoshi=www&eo_comm_zxnrxs_xsfs=op&eo_comm_zxnrxs_gjz=&eo_comm_zxnrxs_lmid=id100000027285&eo_comm_zxnrxs_wzid=100000027210'
    header={
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:50.0) Gecko/20100101 Firefox/50.0',
    'Referer':'http://www.jswjj.gov.cn/office_new/eo_comm_zxnrxs.php?eo_comm_zxnrxs_biaoshi=www&eo_comm_zxnrxs_xsfs=op&eo_comm_zxnrxs_gjz=&eo_comm_zxnrxs_lmid=id100000027285&eo_comm_zxnrxs_wzid=100000027210'
    }
    payload='eo_comm_zxnrxs_biaoshi=www&eo_comm_zxnrxs_xsfs=op&eo_comm_zxnrxs_width=780&eo_comm_zxnrxs_lmxxid=0&eo_comm_zxnrxs_lmid=id100000027285&eo_comm_zxnrxs_wzid=100000027210&eo_comm_zxnrxs_xgyes=0&eo_comm_zxnrxs_lmmc=&eo_comm_zxnrxs_gjz=&eo_comm_zxnrxs_fh=&eo_comm_pgkj_rzid=100011849392&eo_comm_zxnrxs_SubmitButton=%CF%D4%CA%BE'
    req=s.post(url,payload)
    req.encoding = 'gb2312'
    print req.text
if __name__=='__main__':
    print '================================================================================'
    for x in range(4000,4645):
        get_text(str(x))
        time.sleep(0.5)
