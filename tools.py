import urllib
dc_map = {
    # 'JXBMC': 'c0-e2'
    'c0-e7': 'KKXN', # 2019
    'c0-e13': 'KKXN',
    'c0-e14': 'KKXQ', # 学期
    'c0-e15': 'TEACH_CLASS_ID',
    'c0-e16': 'KCDM', # 课程ID
    'c0-e17': 'KCZWMC', # name
    'teachers': 'SKJSXM',
    'locate': 'SKSJDD',
    'sum': 'RSXD', # 总数
    'online': 'SJSKRS', # 剩余
}

def get_info(sentences):
    dc = dict()
    s = ''
    for line in sentences.split('\n'):
        if 'var' in line:
            s = line
            break
    for item in s.split(';'):
        item = item.encode("utf-8").decode("unicode_escape")
        if '[' in item:
            dc['TEACH_CLASS_ID'] = item.split('=')[-1].strip('\"')
        elif '.' in item:
            key, val = item.split('.', 1)[1].split('=', 1)
            dc[key] = urllib.parse.quote(val.strip('\"'))

    info = dict()
    for key, val in dc_map.items():
        if 'c0' in key:
            info[key] = f'string:{dc[val]}'
        elif key in ['sum', 'online']:
             info[key] = int(dc[val])
        else:
            info[key] = dc[val]
    return info




if __name__ == '__main__':
    x = {'c0-e7': '2019', 'c0-e13': '2017'}
    with open('data.txt', 'r', encoding='utf') as f:
        sentences = f.read()
    y = get_info(sentences)
    x.update(y)
    # print(x)