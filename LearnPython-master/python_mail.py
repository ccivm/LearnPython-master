# _*_ coding: utf-8 _*_

"""
python发送邮件
"""

from time import sleep
import smtplib,json
from email.mime.text import MIMEText
from email.header import Header
import requests
from_addr=''   #邮件发送账号
to_addrs='1114795374@qq.com'   #接收邮件账号
qqCode=''   #授权码（这个要填自己获取到的）
smtp_server='smtp.qq.com'#固定写死


#配置服务器
stmp=smtplib.SMTP_SSL(smtp_server,smtp_port)
stmp.login(from_addr,qqCode)
header={
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
}
url=r"https://api.uomg.com/api/rand.qinghua?format=json"


_MAPPING = (u'零', u'一', u'二', u'三', u'四', u'五', u'六', u'七', u'八', u'九', u'十', u'十一', u'十二', u'十三', u'十四', u'十五', u'十六', u'十七',u'十八', u'十九')
_P0 = (u'', u'十', u'百', u'千',)
_S4 = 10 ** 4
def to_chinese4(num):
    assert (0 <= num and num < _S4)
    if num < 20:
        return _MAPPING[num]
    else:
        lst = []
        while num >= 10:
            lst.append(num % 10)
            num = num / 10
        lst.append(num)
        c = len(lst)  # 位数
        result = u''

        for idx, val in enumerate(lst):
            val = int(val)
            if val != 0:
                result += _P0[idx] + _MAPPING[val]
                if idx < c - 1 and lst[idx + 1] == 0:
                    result += u'零'
        return result[::-1]
#组装发送内容
for i in  range(1001):
    r=requests.post(url,headers=header)
    a=json.loads(r.content.decode())
    message = MIMEText(a["content"], 'plain', 'utf-8')   #发送的内容
    message['From'] = Header("小高的小猫咪在摸鱼", 'utf-8')   #发件人
    message['To'] = Header("小高", 'utf-8')   #收件人
    subject = '小高的一千零一夜第{}夜'.format(to_chinese4(i+1))
    message['Subject'] = Header(subject, 'utf-8')  #邮件标题

    try:
        stmp.sendmail(from_addr, to_addrs, message.as_string())
    except Exception as e:
        print ('邮件发送失败--' + str(e))
    print ('邮件发送成功',a["content"])
    sleep(5)