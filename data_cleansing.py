import pandas as pd
import re
 
# df = pd.read_csv('Asset/data.csv', encoding='latin1')
abusive = pd.read_csv('Asset/abusive.csv', encoding='utf-8')
new_kamusalay = pd.read_csv('Asset/new_kamusalay.csv', encoding='latin1')
new_kamus_alay = {}
for k,v in new_kamusalay.values:
    new_kamus_alay[k] = v

def processing_word(input_text):
    new_text = []
    new_new_text = []
    text = input_text.split(" ")
    for word in text: # memulai filter abusive word
        if word in abusive['ABUSIVE'].to_list():
            continue
        else:
            new_text.append(word)
    for word in new_text: #memulai filter alay word
        new_word = new_kamus_alay.get(word,word)
        new_new_text.append(new_word)
    
    text = " ".join(new_new_text)
    return text

def processing_text(input_text):
    text = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', 'EMAIL', input_text) #email
    text = input_text.lower()
    text = re.sub(r'[^\w\s]', '', text) # hapus semua punctuation (tanda baca)
    text = text.replace(" 62"," 0")
    text = re.sub(r"\b\d{4}\s?\d{4}\s?\d{4}\b", "NOMOR_TELEPON", text) #ganti nomor telepon ke kata 'NOMOR_TELEPON'
    text = re.sub('((www\.[^\s]+)|(https?://[^\s]+)|(http?://[^\s]+))','', text) #buang link
    text = text.replace("rt","")
    text = text.replace("user","")
    text = text.replace("\n","")
    text = text.replace("url","")
    text = text.strip()
    return text