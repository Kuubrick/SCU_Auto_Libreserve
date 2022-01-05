import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3754.400 QQBrowser/10.5.4034.400'
}
list_url = [
    'http://lib.scu.edu.cn:8088/reservation_myaccount/%E5%B7%A5%E5%AD%A6%E9%A6%86',
    'http://lib.scu.edu.cn:8088/reservation_myaccount/%E6%B1%9F%E5%AE%89%E9%A6%86',
    'http://lib.scu.edu.cn:8088/reservation_myaccount/%E6%96%87%E7%90%86%E9%A6%86',
    'http://lib.scu.edu.cn:8088/reservation_myaccount/%E5%8C%BB%E5%AD%A6%E9%A6%86'
]
list_dic_lib = [
    {
        'str': 'gongxue',
        'lib': '工学馆'
    },
    {
        'str': 'jiangan',
        'lib': '江安馆'
    },
    {
        'str': 'wenli',
        'lib': '文理馆'
    },
    {
        'str': 'yixue',
        'lib': '医学馆'
    },
]
hint_info = []


def make_lib_resv(stid, pwd, lib):
    stid = int(stid)
    # pwd = int(pwd)
    lib = int(lib)
    login_data = {
        'form_id': 'studentlogin',
        'academic': stid,
        'passwd': pwd,
        'op': '登录'
    }
    s = requests.Session()
    s.headers.update(headers)

    # print('您好，您的学号为：' + str(stid))
    # hint_info.append('您好，您的学号为：' + str(stid))
    res = s.post('http://lib.scu.edu.cn:8088/student/login?from=reservation', data=login_data)
    if '用户登录' in res.text:
        print('用户名或密码错误，如果您确定无误，可能是网络问题，请稍后重试...')
        hint_info.append('用户名或密码错误，如果您确定无误，可能是网络问题，请稍后重试...')
        return
    ret = s.get('http://lib.scu.edu.cn:8088/reservation')
    print('您好,' + get_name(ret)[0])
    hint_info.append('您好,' + get_name(ret)[0])
    if '您已在馆' in ret.text:
        num_lib = is_in_lib(ret)
        print('您已在' + list_dic_lib[num_lib]['lib'])
        hint_info.append('您已在' + list_dic_lib[num_lib]['lib'])
        return
    if '不在预约时间' in ret.text:
        hint_info.append('不在预约时间')
        print('不在预约时间')
        return
    if '您已预约' in ret.text:
        reserved_num = is_reserved(ret)
        print('您已预约' + list_dic_lib[reserved_num]['lib'])
        hint_info.append('您已预约' + list_dic_lib[reserved_num]['lib'])
        if reserved_num == lib:
            return
        else:
            hint_info.append('现在为您重新预约' + list_dic_lib[lib]['lib'] + '...')
            print('现在为您重新预约' + list_dic_lib[lib]['lib'] + '...')
            s.get(list_url[lib])
    else:
        ret_after_appointment = s.get(list_url[lib])
    is_succeed(s, lib)


def is_reserved(ret):
    i = 0
    tree = etree.HTML(ret.text)
    reserved = tree.xpath('//*[@id="yiyuyue"]/../@id')
    for dic in list_dic_lib:
        if dic['str'] in reserved[0]:
            return i
        else:
            i = i + 1
    return i


def is_succeed(session, lib):
    res = session.get('http://lib.scu.edu.cn:8088/reservation')
    if lib == is_reserved(res):
        hint_info.append(list_dic_lib[lib]['lib'] + '预约成功')
        print(list_dic_lib[lib]['lib'] + '预约成功')


def is_in_lib(res):
    tree = etree.HTML(res.text)
    for dict in list_dic_lib:
        xpath = '//*[@id="remander-' + dict['str'] + '"]/span/text()'
        if '您已在馆' in tree.xpath(xpath)[0]:
            return list_dic_lib.index(dict)
    return -1


def get_hint_info():
    str = ''
    for item in hint_info:
        str += item
        str += '\n'
    return str


def clean_hint_info():
    hint_info.clear()


def get_name(res):
    tree = etree.HTML(res.text)
    name = tree.xpath('//*[@id="account"]/div[1]/text()')
    return name


if __name__ == '__main__':
    stid = ''
    pwd = ''
    make_lib_resv(stid, pwd, lib=1)
    print(get_hint_info())
