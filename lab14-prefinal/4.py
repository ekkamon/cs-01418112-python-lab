def get_word(source, key):
    data = {}
    used = []

    i = 0
    for val in source:
        if i == len(key):
            break

        if val in used:
            continue
        
        data[key[i]] = val
        used.append(val)

        i += 1
        
    return data
            

def decode(word, encode_text):
    plain_text = ''

    for char in encode_text:
        plain_text += word[char] if char in word else char
            
    return plain_text

def main():
    source = str(input()).replace(' ', '')
    key = str(input())
    encode_text = str(input())
    
    word = get_word(source, key)
    
    print(decode(word, encode_text))
    
main()