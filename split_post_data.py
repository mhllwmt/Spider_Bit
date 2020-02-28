import urllib

def split_post(sentences):
    for line in sentences.strip('\n').split('\n'):
        key, val = line.strip(' ').split(':',1)
        val = urllib.parse.unquote(val)
        print(f'\'{key}\': \'{val}\',')


with open('data.txt', encoding='utf', mode='r') as f:
    s = f.read()
split_post(s)
