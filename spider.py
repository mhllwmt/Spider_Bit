import requests
from lxml import etree
import urllib
import time
from tools import get_info
from config import params, headers, data1, data2

class ScrapeBit:
    def __init__(self):
        # 成绩： http://grdms.bit.edu.cn/yjs/yanyuan/py/pychengji.do?method=enterChaxun
        self.log_url = 'https://login.bit.edu.cn/cas/login?service=http%3A%2F%2Fgrdms.bit.edu.cn%2Fyjs%2Flogin_cas.jsp'
        self.query_url = 'http://grdms.bit.edu.cn/yjs/dwr/call/plaincall/YYPYCommonDWRController.getStdPyjhCourseList4Select.dwr'

        self.session = requests.Session()
        self.username = None

    def login(self, username=None, password=None):
        username = input('请输入学号:\n>>>')
        password = input('请输入密码:\n>>>')

        self.username = username

        r = self.session.get(self.log_url).text
        response = etree.HTML(r)
        lt = response.xpath('//input[@name="lt"]')[0].get('value')
        params['username'] = username
        params['password'] = password
        params['lt'] = lt
        self.session.post(self.log_url, data=params, headers=headers)


    def course_query(self, name):
        name = urllib.parse.quote(name)
        data1['c0-e10'] = f'string:%25{name}%25'
        data1['c0-e1'] = f'string:{self.username}'

        r = self.session.post(self.query_url, data=data1).text
        info = get_info(r)
        for key, _ in data2.items():
            if key in info:
                data2[key] = info[key]
            if key in ['c0-e1', 'c0-e11']:
                data2[key] = f'string:{self.username}'
        return info

    def course_zc(self):
        url = 'http://grdms.bit.edu.cn/yjs/dwr/call/plaincall/YYPYCommonDWRController.pyJxjhSelectCourse.dwr'
        r = self.session.post(url, data=data2).text
        if 'success' in r:
            print("~~~SUCCESS~~~~")
            return True
        else:
            print(r.encode("utf-8").decode("unicode_escape"))
            return False

    def infinite_loop(self):
        print('请输入课程名称')
        name = input('>>>')
        info = self.course_query(name)
        course_name, teachers = urllib.parse.unquote(info["c0-e17"]),  urllib.parse.unquote(info["teachers"])
        print(f'course_name:{course_name}\n teachers:{teachers}')
        print(f'sum_number{info["sum"]} | left_number:{info["sum"] - info["online"]}')
        print("#"*50)
        flag = input("确定要注册这门课程嘛？Y/N\n>>>>")
        if flag == 'Y':
            while True:
                ttimes = 0
                while info["sum"] - info["online"] == 0:
                    time.sleep(5)
                    print(f"没有课啦。。。{ttimes}")
                    ttimes += 1
                    info = self.course_query(name)
                print("查询有余课。。。")
                times = 0
                while not self.course_zc() and times <= 10:
                    times += 1
                    time.sleep(5)
                    print(f"第{times}抢课失败")
                if times < 10:
                    break
        else:
            print("那么请重新开启吧，233，因为不能重新输入。。。课程名称默认爬取第一个")

if __name__ == '__main__':
    s = ScrapeBit()
    s.login()
    s.infinite_loop()
