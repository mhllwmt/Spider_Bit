params = {
    'username': 'lzx',
    'password': 'lzx',
    'lt': 'hello',
    'execution': 'e1s1',
    '_eventId': 'submit',
    'rmShown': '1'
}

# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
# Accept-Encoding: gzip, deflate, br
# Accept-Language: zh,zh-CN;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6
# Cache-Control: max-age=0
headers = {
    'Connection': 'keep-alive',
    # Content-Length: 144
    'Content-Type' : 'application/x-www-form-urlencoded',
    # 'Cookie': 'JSESSIONID=0000Z5OiZz5yzXJ6BX9WksMd6jF:18bicu090; __utma=158042917.1308993144.1581989584.1581989584.1581989584.1; __utmz=158042917.1581989584.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic',
    # 'Host': 'login.bit.edu.cn',
    'Origin': 'https://login.bit.edu.cn',
    'Referer': 'https://login.bit.edu.cn/cas/login?service=http%3A%2F%2Fgrdms.bit.edu.cn%2Fyjs%2Flogin_cas.jsp',
    # Sec-Fetch-Dest: document
    # Sec-Fetch-Mode: navigate
    # Sec-Fetch-Site: same-origin
    # Sec-Fetch-User: ?1
    # Upgrade-Insecure-Requests: 1
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
}

data1 = {
    'callCount': '1',
    'page': '/yjs/yanyuan/py/pyjxjh.do?method=stdSelectCourseEntry',
    'httpSessionId': 'E81CD39A779B5ACDED8F8A2ED4D50054',
    'scriptSessionId': 'CF3FFD6F0EB12036196DE1B5ACBFA5CB886',
    'c0-scriptName': 'YYPYCommonDWRController',
    'c0-methodName': 'getStdQxkcCourseList4Select',
    'c0-id': '0',
    'c0-param0': 'string:2019',
    'c0-e1': 'string:3120191031',
    'c0-e2': 'string:1',
    'c0-e3': 'string:YY000000000000000000000000726708',
    'c0-e4': 'string:YY000000000000000000000000726708',
    'c0-e5': 'string:%E7%A1%95%E5%A3%AB',
    'c0-e6': 'string:%E7%BB%9F%E6%8B%9B%E7%BB%9F%E5%88%86%E7%A0%94%E7%A9%B6%E7%94%9F',
    'c0-e7': 'string:2019',
    'c0-e8': 'string:%E6%97%A0',
    'c0-e9': 'string:',
    'c0-param1': 'Object_Object:{xh:reference:c0-e1, lb:reference:c0-e2, studentId:reference:c0-e3, id:reference:c0-e4, pycc:reference:c0-e5, xslb:reference:c0-e6, nj:reference:c0-e7, ldfs:reference:c0-e8, ptlx:reference:c0-e9}',
    'c0-e10': 'string:%25%E8%AE%A1%E7%AE%97%E6%9C%BA%E4%BB%BF%E7%9C%9F%25',
    'c0-param2': 'Object_Object:{t.kczwmc:reference:c0-e10}',
    'batchId': '0',
}

data2 = {
    'callCount': '1',
    'page': '/yjs/yanyuan/py/pyjxjh.do?method=stdSelectCourseEntry',
    'httpSessionId': 'E81CD39A779B5ACDED8F8A2ED4D50054',
    'scriptSessionId': '1D9986E84DE099F87FF0EB26880A73F4892',
    'c0-scriptName': 'YYPYCommonDWRController',
    'c0-methodName': 'pyJxjhSelectCourse',
    'c0-id': '0',
    'c0-e1': 'string:3120191031',
    'c0-e2': 'string:1',
    'c0-e3': 'string:YY000000000000000000000000726708',
    'c0-e4': 'string:YY000000000000000000000000726708',
    # 'c0-e5': 'string:%E7%A1%95%E5%A3%AB',
    # 'c0-e6': 'string:%E7%BB%9F%E6%8B%9B%E7%BB%9F%E5%88%86%E7%A0%94%E7%A9%B6%E7%94%9F',
    'c0-e7': 'string:2019',
    'c0-e8': 'string:%E6%97%A0',
    'c0-e9': 'string:',
    'c0-param0': 'Object_Object:{xh:reference:c0-e1, lb:reference:c0-e2, studentId:reference:c0-e3, id:reference:c0-e4, pycc:reference:c0-e5, xslb:reference:c0-e6, nj:reference:c0-e7, ldfs:reference:c0-e8, ptlx:reference:c0-e9}',
    'c0-e10': 'string:YY000000000000000000000000726708',
    'c0-e11': 'string:3120191031',
    'c0-e12': 'string:1',
    'c0-e13': 'string:2019',
    'c0-e14': 'string:%E7%AC%AC%E4%BA%8C%E5%AD%A6%E6%9C%9F',
    'c0-e15': 'string:2019-2-0601005',
    'c0-e16': 'string:0601005',
    'c0-e17': 'string:%EF%BC%88%E8%8B%B1%EF%BC%89%E8%AE%A1%E7%AE%97%E6%9C%BA%E4%B8%8E%E5%88%86%E5%B8%83%E5%BC%8F%E6%8E%A7%E5%88%B6%E7%B3%BB%E7%BB%9F',
    'c0-e18': 'string:',
    # 'c0-e19': 'string:%E8%AF%BE%E7%A8%8B%E6%80%A7%E8%B4%A8',
    # 'c0-e20': 'string:%E4%B8%93%E4%B8%9A%E8%AF%BE',
    # 'c0-e21': 'string:32',
    # 'c0-e22': 'string:2',
    'c0-e23': 'string:',
    'c0-param1': 'Object_Object:{studentId:reference:c0-e10, xh:reference:c0-e11, lb:reference:c0-e12, xn:reference:c0-e13, xq:reference:c0-e14, teachClassId:reference:c0-e15, kcdm:reference:c0-e16, kczwmc:reference:c0-e17, kcywmc:reference:c0-e18, kcxz:reference:c0-e19, kclb:reference:c0-e20, xs:reference:c0-e21, xf:reference:c0-e22, ksfs:reference:c0-e23}',
    'batchId': '7',
}