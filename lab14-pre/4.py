provinces = {
    'central': ['Bangkok', 'Samut Prakan', 'Nonthaburi', 'Samut Sakhon', 'Ayutthaya', 'Pathum Thani'],
    'northern': ['Chiang Mai', 'Chiang Rai', 'Lamphun', 'Lampang', 'Mae Hong Son', 'Nan'],
    'northeastern': ['Roi Et', 'Chaiyaphum', 'Loei', 'Nong Khai', 'Sakon Nakhon', 'Surin'],
    'southern': ['Surat Thani', 'Krabi', 'Phuket', 'Yala', 'Songkhla', 'Narathiwat']
}

def main():
    while True:
        data = str(input())
        
        if data == '':
            break
        
        province, region = data.split(':')
        provinces[region].append(province)

main()
