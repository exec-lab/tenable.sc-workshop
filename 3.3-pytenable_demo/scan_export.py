# coding:utf-8
# @Time    : 2019-06-10 13:58
# @Author  : baozhibo
# @File    : sc.py
# @Software: PyCharm
# @Revision: shawn


from tenable.sc import TenableSC
from pprint import pprint
import time
import getpass
import logging
#logging.basicConfig(level=logging.DEBUG)


#sc = TenableSC("hkdemo.show-what.com")
#sc.login('scan', '111')
sc = TenableSC("192.168.0.70")
username = input('Input Username: ')  # 按提示输入用户名
password = getpass.getpass('Input Password: ')  # 按提示输入密码(密码不会显示在命令行输出)
sc.login(username, password)

global scdict
# for vuln in sc.analysis.scan(1):
#    pprint(vuln)

# plugins = sc.plugins.list(filter=('name', 'like', 'java'))
# for plugin in plugins:
#    pprint(plugin)


'''
创建扫描
传入参数任务名称，目标ip，'repo id'=2, 'policy id'=1000001
name = scan_export
target_args = list
'''

def CreatNewScan():
    scdict = sc.scans.create(name='scan_export', repo=1,
                             policy_id=1000002, targets=[input('Input target IPs: ')])
    
    #scdict = sc.scans.create('scan_export', 2, policy_id=1000027, targets=['192.168.0.51']) #默认param写法，较简单但不易理解
    print(scdict['id'])
    return scdict


'''
启动扫描，根据创建扫描返回的dict的id，启动扫描。
扫描完成后删除active scan和scan result
'''


def LaunchScan(sdict):
    running = sc.scans.launch(int(sdict['id']))
    print('The Active Scan ID is {}.'.format(int(sdict['id'])))
    print('The Scan Result ID is {}.'.format(running['scanResult']['id']))
    while True:
        time.sleep(10)
        scan = sc.scan_instances.details(int(running['scanResult']['id']))
        pprint(scan['status'])
        if scan['status'] == 'Completed':
            with open('/Users/xxu/Downloads/result.zip', 'wb') as fobj:
                sc.scan_instances.export_scan(
                    int(running['scanResult']['id']), fobj)
            details = sc.analysis.scan(int(sdict['id']))
            pprint 
            sc.scans.delete(int(sdict['id']))
            sc.scan_instances.delete(int(running['scanResult']['id']))
        #    sc.logout() #可以在此处
        #    with open('log.log', 'a') as resu:
        #        for vule in details:
        #            resu.writelines(vule)
        #            pprint(vule)
            break #此处如不加break会见到以下两种情况的错误
            '''
            情况1) 当sc.logout()写在while loop内
            requests.exceptions.SSLError: HTTPSConnectionPool(host='192.168.0.51', port=443): Max retries exceeded with url: /rest/scanResult/290 (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate in certificate chain (_ssl.c:1056)')))
            情况2）当sc.logout()写在__name__内
            tenable.errors.APIError: None:403 {"type":"regular","response":"","error_code":147,"error_msg":"Scan Result get failed.\nScan Result #290 does not exist.\n","warnings":[],"timestamp":1563814621}
            '''

#logout
#sc.logout() #当sc.logout()用在def之外任何地方会出现错误
'''
requests.exceptions.SSLError: HTTPSConnectionPool(host='192.168.0.51', port=443): Max retries exceeded with url: /rest/scan (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate in certificate chain (_ssl.c:1056)')))
'''


'''
查询扫描状态
'''

if __name__ == '__main__':
    sc_dict = CreatNewScan()
    LaunchScan(sc_dict)
    sc.logout()
 
