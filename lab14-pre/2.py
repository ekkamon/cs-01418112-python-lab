provinces = {
    'central': ['Bangkok', 'Samut Prakan', 'Nonthaburi', 'Samut Sakhon', 'Ayutthaya', 'Pathum Thani'],
    'northern': ['Chiang Mai', 'Chiang Rai', 'Lamphun', 'Lampang', 'Mae Hong Son', 'Nan'],
    'northeastern': ['Roi Et', 'Chaiyaphum', 'Loei', 'Nong Khai', 'Sakon Nakhon', 'Surin'],
    'southern': ['Surat Thani', 'Krabi', 'Phuket', 'Yala', 'Songkhla', 'Narathiwat']
}

def is_in_provice_data(province, region):
    if region not in provinces:
        return False
    
    if province not in provinces[region]:
        return False
    
    return True

def main():
    while True:
        data = str(input())
        
        if data == '':
            break
        
        province, region = data.split(':')
        
        print('Yes' if is_in_provice_data(province, region) else 'No')
        
        
main()