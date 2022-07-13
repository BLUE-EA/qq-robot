import requests


def get_data():
    response = requests.get('http://bjb.yunwj.top/php/qq.php')
    data = response.text
    data_arr = data.split('【换行】')
    res = ''
    for i in range(1, data_arr.__len__() - 1):
        res += data_arr[i] + '\n'
    return res

if __name__ == '__main__':
    print(get_data())
