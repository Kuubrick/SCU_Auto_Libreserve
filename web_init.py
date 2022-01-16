from pywebio.input import *
from pywebio.output import *
from libReserve import make_lib_resv
from libReserve import get_hint_info
from libReserve import clean_hint_info
from pywebio import start_server
from csvOperate import insert
from csvOperate import in_the_csv
from csvOperate import is_same_lib

list_libs = [
    {
        'label': '工学馆',
        'value': 0
    },
    {
        'label': '江安馆',
        'value': 1,
        'selected': True
    },
    {
        'label': '文理馆',
        'value': 2
    },
    {
        'label': '医学馆',
        'value': 3
    },
]


def web_init():
    inputs = input_group(
        label='请输入你的学号，图书馆密码并选择图书馆',
        inputs=[
            input(label="请输入你的学号：", type=TEXT, name='stid'),
            input(label="请输入你的密码：", type=PASSWORD, name='pwd'),
            select(label='请选择要固定预约的图书馆', options=list_libs, name='lib')
        ]
    )
    stid = inputs['stid']
    pwd = inputs['pwd']
    lib = inputs['lib']
    status = make_lib_resv(stid, pwd, lib)
    hint_info = get_hint_info()
    if status:
        insert(stid, pwd, lib)
        hint_info = get_hint_info() + '\n添加到数据库成功'
    put_info(hint_info)
    clean_hint_info()


if __name__ == '__main__':
    start_server(web_init, 5001)
