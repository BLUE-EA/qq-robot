import requests
from bs4 import BeautifulSoup


def get_search_url(name='月亮与六便士'):
    s = requests.session()
    s.keep_alive = False
    url = 'https://www.zjkhuiyu.com/search.php?q=' + name
    response = s.get(url)
    search_soup = BeautifulSoup(response.text)
    item = search_soup.select_one('div[class="ans_list"] a')
    return item.get('href')


def get_article():
    url = get_search_url()
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    p_list = soup.select(
        '''div[id="wrap"] 
        div[class="wrap container"] 
        div[class="main"] 
        article 
        div[id="article-article"] 
        div[data-desc="article"] 
        p''')
    str = ''
    flag = False
    for item in p_list:
        txt = item.text.strip()
        if is_num_start(txt) and flag is False:
            flag = True
            str += txt + '\n'
        elif is_num_start(txt) is False and flag:
            str += item.text + '\n'
        elif is_num_start(txt) and flag:
            break
    return str


def is_num_start(str):
    return str[0] in '0123456789'


def get_article1(name):
    f = open('../resource/article/' + name + '.txt', encoding='utf-8')
    content = f.readline()
    while content:
        print(content)
        content = f.readline()


def search_by_baidu(city):
    url = f'https://www.baidu.com/s?wd={city}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'Cookie': 'BIDUPSID=694A60428A63A7D5550D50795089276D; PSTM=1655693484; BAIDUID=694A60428A63A7D591762D35B63DE45F:FG=1; BD_UPN=12314753; BDUSS=UZyZ09LU0R1RU5oRkFPNXY4R0tmZkZNd2FmTFJGNFlxcEMyfi1Kdncyc01HdGxpSVFBQUFBJCQAAAAAAAAAAAEAAAB1nlIk08a358rAvec2eQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAyNsWIMjbFia; BDUSS_BFESS=UZyZ09LU0R1RU5oRkFPNXY4R0tmZkZNd2FmTFJGNFlxcEMyfi1Kdncyc01HdGxpSVFBQUFBJCQAAAAAAAAAAAEAAAB1nlIk08a358rAvec2eQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAyNsWIMjbFia; BA_HECTOR=0g812l258505802h0h8gkvh21hcpp1817; ZFY=zyj1dZSDyBOaB5AUuqfKL:BN3w:Abtr6xv6FhqXbwTtOA:C; BAIDUID_BFESS=694A60428A63A7D591762D35B63DE45F:FG=1; BD_HOME=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; BD_CK_SAM=1; PSINO=7; BDRCVFR[30tQLoY7sAT]=mk3SLVN4HKm; sugstore=0; Hm_lvt_aec699bb6442ba076c8981c6dc490771=1657091737,1657270921,1657528081,1657608225; Hm_lpvt_aec699bb6442ba076c8981c6dc490771=1657608225; COOKIE_SESSION=8_0_9_9_7_4_0_0_9_4_1_0_10724_0_0_0_1657606463_0_1657608231|9#328047_8_1656382815|3; shifen[1407265_91638]=1657608255; BDSFRCVID=jp8OJexroG06W-oDzjLz8diotmKK0gOTDYrEOwXPsp3LGJLVcVPrEG0PtOVzGoFbI1odogKK3gOTH4AF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; BDSFRCVID_BFESS=jp8OJexroG06W-oDzjLz8diotmKK0gOTDYrEOwXPsp3LGJLVcVPrEG0PtOVzGoFbI1odogKK3gOTH4AF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; BCLID=8870764031421673407; H_BDCLCKID_SF=tbPD_CtMJDt3eJbGq6_a-n0eqxby26n8BRR9aJ5nJDobeIjRBPnU2bkB3M73h6OZ5DojBJrKQpP-HJ715loUMPAP5p3AhTo-tIbhKl0MLUjlbb0xyUQYXTD-yMnMBMPe52OnaIbp3fAKftnOM46JehL3346-35543bRTLnLy5KJtMDF4e5KajTcXDHRabK6aKC5bL6rJabC3SfjcXU6q2bDeQN0qLKry3TQB2pPy5nTofb6oyT3JXp0vWq54WbbvLT7johRTWqR4HUQMKxonDh83XnjE0-RlKeKDWbbO5hvvhn3O3MAMLfKmDloOW-TB5bbPLUQF5l8-sq0x0bOte-bQXH_EJjkHtRk8oDDQKt8_HRjYbb__-P4DeNDqBxRZ56bHWh0MJf0VDpbuMxvpe-0thpOLBMPj52OnKUT-3l7boMJRK5bdQUIT3xbpQnj43bRTLp7CMq3osRoVDtnfhP-UyNbMWh37Jg6lMKoaMp78jR093JO4y4Ldj4oxJpOJ5JbMopCafD_WhCD6ejKaePDyqx5Ka43tHD7yWCkKJqTcOR59K4nnD5KiqfnRhtTr3RbbBR72alvvhb3O3MOZKxLg5n7Tbb8eBgvZ2UQJQfJKsq0x0bOc3RI1hPjaB6oy5IOMahkb5h7xOKbqQlPK5JkgMx6MqpQJQeQ-5KQN3KJmfbL9bT3YjjTXeaKDt5FHtR3aQ5rtKRTffjrnhPF3MRObXP6-hnjy3b4q-56O3Pc88-F9b-ro5-uUyN3MWh3Ry6r42-39LPO2hpRjyxv4-pKrK4oxJpOJBacEKb7IKqIaDnbvbURvDP-g3-AJ3x5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIE3-oJqCD2MCD43f; BCLID_BFESS=8870764031421673407; H_BDCLCKID_SF_BFESS=tbPD_CtMJDt3eJbGq6_a-n0eqxby26n8BRR9aJ5nJDobeIjRBPnU2bkB3M73h6OZ5DojBJrKQpP-HJ715loUMPAP5p3AhTo-tIbhKl0MLUjlbb0xyUQYXTD-yMnMBMPe52OnaIbp3fAKftnOM46JehL3346-35543bRTLnLy5KJtMDF4e5KajTcXDHRabK6aKC5bL6rJabC3SfjcXU6q2bDeQN0qLKry3TQB2pPy5nTofb6oyT3JXp0vWq54WbbvLT7johRTWqR4HUQMKxonDh83XnjE0-RlKeKDWbbO5hvvhn3O3MAMLfKmDloOW-TB5bbPLUQF5l8-sq0x0bOte-bQXH_EJjkHtRk8oDDQKt8_HRjYbb__-P4DeNDqBxRZ56bHWh0MJf0VDpbuMxvpe-0thpOLBMPj52OnKUT-3l7boMJRK5bdQUIT3xbpQnj43bRTLp7CMq3osRoVDtnfhP-UyNbMWh37Jg6lMKoaMp78jR093JO4y4Ldj4oxJpOJ5JbMopCafD_WhCD6ejKaePDyqx5Ka43tHD7yWCkKJqTcOR59K4nnD5KiqfnRhtTr3RbbBR72alvvhb3O3MOZKxLg5n7Tbb8eBgvZ2UQJQfJKsq0x0bOc3RI1hPjaB6oy5IOMahkb5h7xOKbqQlPK5JkgMx6MqpQJQeQ-5KQN3KJmfbL9bT3YjjTXeaKDt5FHtR3aQ5rtKRTffjrnhPF3MRObXP6-hnjy3b4q-56O3Pc88-F9b-ro5-uUyN3MWh3Ry6r42-39LPO2hpRjyxv4-pKrK4oxJpOJBacEKb7IKqIaDnbvbURvDP-g3-AJ3x5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIE3-oJqCD2MCD43f; H_PS_PSSID=26350; baikeVisitId=3957ee06-5415-42f4-8d87-663feb663b28; H_PS_645EC=d0bc03C1Bt25qpIcIp+qctrvuAOfrV7taAWDtpJjsx8Fv425ONn0YBb/fFxUyaDrN0Qz+wdgbng; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BDSVRTM=0'
    }
    response = requests.get(url, headers=headers)
    txt = response.text
    print(txt)
    soup = BeautifulSoup(response.text)
    item = soup.select_one('''#wrapper
                            #wrapper_wrapper
                            #content_left
                            .result-op''')
    return item.get('mu')


if __name__ == '__main__':
    search_by_baidu('广东深圳天气')
