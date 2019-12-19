from flask import Flask, request, jsonify, render_template, make_response
from sklearn.externals import joblib
import traceback
import pandas as pd
import json
from bs4 import BeautifulSoup 
import requests
from selenium import webdriver
import random
import time
import csv



# Your API definition


# Create the application instance
app = Flask(__name__, template_folder="templates")
app.config['JSON_AS_ASCII'] = False

@app.route('/yorumlar', methods=['GET'])
def yorumlar():
    pageCount =1
    yorumlar=[]
  #  imdbUrl =request.args.get('link', default = 1, type = str)
   # imdbUrl='https://www.hepsiburada.com/hometech-alfa-110a-intel-atom-z3735f-2gb-32gb-emmc-windows-10-home-11-6-fhd-tasinabilir-bilgisayar-p-HBV00000BEEWD'
    link = request.args.get('link', default = '*', type = str)
    link  = link + "-yorumlari?sayfa=" +str(pageCount)
    r = requests.get(link)
    soup = BeautifulSoup(r.content,"html.parser")
    gelen_veri2 = soup.find("div",{"class":"pagination"}).find("ul").find_all("li")
    sayi = len(gelen_veri2)

    while pageCount<sayi:
        gelen_veri = soup.find_all("p",{"class":"review-text"})
        
        for film in gelen_veri:
            yorumlar.append(film.text)

        pageCount+=1
       # json_string = jsonify(yorumlar)
       # json= json.dumps(json_string, ensure_ascii=False).encode('utf8')
        link =""
        link = request.args.get('link', default = '*', type = str)
        link  = link + "-yorumlari?sayfa="
        link = link + str(pageCount)

        r = requests.get(link)
        soup = BeautifulSoup(r.content,"html.parser")
    with open('urldatamts.csv','w',newline='',encoding='utf-16') as f:
        fieldname=['Yorum','Duygu']
        theWriter = csv.DictWriter(f,fieldnames=fieldname)
        
        
        theWriter.writeheader();
        for word in yorumlar:
            theWriter.writerow({'Yorum' : word , 'Duygu' : 0})
        yorumlar =[]
            
       
       
        
        
    return jsonify(yorumlar) 

@app.route('/olumluyorumlar', methods=['GET'])
def olumluYorumlar():
    pageCount =1
    yorumlar=[]
  #  imdbUrl =request.args.get('link', default = 1, type = str)
   # imdbUrl='https://www.hepsiburada.com/hometech-alfa-110a-intel-atom-z3735f-2gb-32gb-emmc-windows-10-home-11-6-fhd-tasinabilir-bilgisayar-p-HBV00000BEEWD'
    link = request.args.get('link', default = '*', type = str)
    link  = link + "-yorumlari?filtre=5&sayfa=" +str(pageCount)
    r = requests.get(link)
    soup = BeautifulSoup(r.content,"html.parser")
    gelen_veri2 = soup.find("div",{"class":"pagination"}).find("ul").find_all("li")[-1].find("span").text
    sayi = int(gelen_veri2)

    while pageCount<sayi:
        gelen_veri = soup.find_all("p",{"class":"review-text"})
        
        for film in gelen_veri:
            yorumlar.append(film.text)

        pageCount+=1
       # json_string = jsonify(yorumlar)
       # json= json.dumps(json_string, ensure_ascii=False).encode('utf8')
        link =""
        link = request.args.get('link', default = '*', type = str)
        link  = link + "-yorumlari?filtre=5&sayfa=" +str(pageCount)
        r = requests.get(link)
        soup = BeautifulSoup(r.content,"html.parser")
        
    with open('urlDataOlumlu.csv','w',newline='',encoding='utf-16') as f:
        fieldname=['Yorum','Duygu']
        theWriter = csv.DictWriter(f,fieldnames=fieldname)
        
        
        theWriter.writeheader();
        for word in yorumlar:
            theWriter.writerow({'Yorum' : word , 'Duygu' : 1})
            
       
       
        
        
    return jsonify(yorumlar) 


@app.route('/olumsuzyorumlar', methods=['GET'])
def olumsuzyorumlar():
    pageCount =1
    yorumlar=[]
    yorumlar2=[]

  #  imdbUrl =request.args.get('link', default = 1, type = str)
   # imdbUrl='https://www.hepsiburada.com/hometech-alfa-110a-intel-atom-z3735f-2gb-32gb-emmc-windows-10-home-11-6-fhd-tasinabilir-bilgisayar-p-HBV00000BEEWD'
    link = request.args.get('link', default = '*', type = str)
    link  = link + "-yorumlari?filtre=2%2C1&sayfa=" +str(pageCount)
    r = requests.get(link)
    soup = BeautifulSoup(r.content,"html.parser")
    gelen_veri2 = soup.find("div",{"class":"pagination"}).find("ul").find_all("li")
    sayi = len(gelen_veri2)

    while pageCount<sayi:
        gelen_veri = soup.find_all("p",{"class":"review-text"})
        
        for film in gelen_veri:
            yorumlar.append(film.text)


        pageCount+=1
       
        link =""
        link = request.args.get('link', default = '*', type = str)
        link  = link + "-yorumlari?filtre=2%2C1&sayfa=" +str(pageCount)
        r = requests.get(link)
        soup = BeautifulSoup(r.content,"html.parser")
        
    
    with open('urlDataOlumsuz.csv','w',newline='',encoding='utf-16') as f:
        fieldname=['Yorum','Duygu']
        theWriter = csv.DictWriter(f,fieldnames=fieldname)
        yorumlar2 = yorumlar
        
        
        theWriter.writeheader();
        for word in yorumlar:
            theWriter.writerow({'Yorum' : word , 'Duygu' : 0})
        yorumlar =[]

    return jsonify(yorumlar2) 

if __name__ == '__main__':


	

	'''
    try:  # for py3
    dump = np.load('filename.npz', encoding='bytes')
    dump = dict(dump[dump.files[0]].tolist())
    dump = {str(k.decode('utf-8')): dump[k] for k in dump}
	except:  # for py2
    dump = np.load(open('filename.npz', 'rb'))
    dump = dict(dump[dump.files[0]].tolist())
    # dump = {str(k): dump[k] for k in dump}
    '''

	print('Model columns loaded')
    
	
	app.run(debug=True)
