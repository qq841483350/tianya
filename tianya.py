#encoding:utf-8
"天涯部落帖子自动发布"
import urllib,urllib2,cookielib
def tianya():
    header={
        "Host":"passport.tianya.cn",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; rv:41.0) Gecko/20100101 Firefox/41.0",
        "Referer":"http://www.tianya.cn/"
    }
    cookie=cookielib.CookieJar()
    opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    urllib2.install_opener(opener)

    login_data={
        "fowardURL":"http://groups.tianya.cn/list-182732-1.shtml",
        "method":"name",
        "vwriter":"liyt@jy1898.com",
        "vpassword":"jy18980916",
        "rmflag":"1",
        "submit":"登陆"
    }
    login_url="https://passport.tianya.cn/login?from=index&_goto=login&returnURL=http://www.tianya.cn"
    login_data=urllib.urlencode(login_data)
    request=urllib2.Request(url=login_url,data=login_data,headers=header)
    html=urllib2.urlopen(request).read()
    if "登录中" in html:
        print u'登陆成功'
    else:
        print html

    header={
        "Host":"groups.tianya.cn",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; rv:41.0) Gecko/20100101 Firefox/41.0",
        "Referer":"http://groups.tianya.cn/group_post_article.jsp?item=182732",
        "Cookie":"time=ct=1446530080.103; __auc=92dfcc7314fda537d3981bd9ac2; __guid=302892053; __ptime=1446530080762; Hm_lvt_bc5755e0609123f78d0e816bf7dee255=1446170660,1446174671,1446429454,1446518369; __guid2=302892053; Hm_lvt_80579b57bf1b16bdf88364b13221a8bd=1446526132; __utma=22245310.1937553957.1442548556.1442548556.1442548556.1; __utmz=22245310.1442548556.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; bc_ds_w=d12_196; __cid=57; JSESSIONID=abcCZmeFCgLBV6egknldv; __visit=wpopa%3D1132; Hm_lpvt_bc5755e0609123f78d0e816bf7dee255=1446530081; ty_msg=1446530046753_105833480_0_0_0_0_0_0_0_0_0_0_0; ds_ids=VwY_BNf_sdg_vEu_Ej3_wdt_lYX; vip=310391165%3D0; Hm_lpvt_80579b57bf1b16bdf88364b13221a8bd=1446526829; __u_a=v2.3.1; hb_new=1446517921000; __asc=2163b84c150cbd523b99990af43; temp=k=630223861&s=&t=1446529612&b=95527c1f64f23b276261aca924805498&ct=1446529612&et=1449121612; sso=r=1137745902&sid=&wsid=930D99A1C9F89F81872BDE9F2F9EE122; user=w=%u60a6%u9001%u5065%u5eb7%u6559%u6388&id=105833480&f=1; right=web4=n&portal=n; temp4=rm=7a5d1a34b1944364ff7db7b228c79440; ds_exp=10"
    }
    cookie=cookielib.CookieJar()
    opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    urllib2.install_opener(opener)
    wz_data={
        "itemId":"182732",
        "title":"HPV病毒有哪些类型？",
        "content":"HPV病毒有哪些类型？",
        "bScore":"true",
        "comeFrom":"0",
        "classId":"0",
        "bOriginal":"true"
    }
    wz_url="http://groups.tianya.cn/api?method=group.article.insertArticle"
    wz_data=urllib.urlencode(wz_data)
    request=urllib2.Request(url=wz_url,data=wz_data,headers=header)
    html=urllib2.urlopen(request).read()
    if "帖子发布成功" in html:
        print u'帖子发布成功'
    else:
        print html
if __name__=="__main__":
    tianya()
