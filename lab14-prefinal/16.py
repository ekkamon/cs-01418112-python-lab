def encode(text):
    cipher_text = ''
    
    if len(text) % 2 > 0:
        middle = len(text) // 2
        
        for i in range(middle - 1, -1, -1):
            cipher_text += text[i]
            
        cipher_text += text[middle]
        
        for i in range(len(text) - 1, middle, -1):
            cipher_text += text[i]        
            
    else:
        middle = (len(text) // 2) - 1
        
        for i in range(middle, -1, -1):
            cipher_text += text[i]
            
        for i in range(len(text) - 1, middle, -1):
            cipher_text += text[i]
        
    return cipher_text


def main():
    text = str(input())
    print(encode(text))
    
main()