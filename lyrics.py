#!/usr/bin/env python
#coding:utf-8

import time
import requests
import json
import re
from bs4 import BeautifulSoup

def download_by_music_id(music_id):
    #根据歌词id下载
    url = 'http://music.163.com/api/song/lyric?'+ 'id=' + str(music_id)+ '&lv=1&kv=1&tv=-1'
    r = requests.get(url)
    json_obj = r.text

    j = json.loads(json_obj)
    lrc = j['lrc']['lyric']
    pat1 = re.compile(r'\[.*\]')  #这里几行代码是把歌词中的空格和符号之类的去掉
    lrc = re.sub(pat1,'',lrc)
    pat2 = re.compile(r'.*\:.*')
    lrc = re.sub(pat2,'',lrc)
    pat3 = re.compile(r'.*\/.*')
    lrc = re.sub(pat3,'',lrc)  
    lrc = lrc.strip()
    return lrc

def get_music_ids_by_musican_id(singer_id): #通过一个歌手id下载这个歌手的所有歌词
    singer_url = 'http://music.163.com/artist?'+ 'id='+str(singer_id)
    r = requests.get(singer_url).text
    soupObj = BeautifulSoup(r,'lxml')
    song_ids = soupObj.find('textarea').text
    jobj = json.loads(song_ids)

    ids ={}
    for item in jobj:
        ids[item['name']] = item['id']
    return ids

def download_lyric(uid):
    music_ids = get_music_ids_by_musican_id(uid)
    for key in music_ids:
        try:
            text = download_by_music_id(music_ids[key])
            with open('%s.txt'%singer_id,'a',encoding='utf-8') as f:
	            f.write('\n')
	            for t in text:
		            f.write(t)
        except:
            print('')

print("请输入歌手的id：")
singer_id = input()
download_lyric(singer_id)