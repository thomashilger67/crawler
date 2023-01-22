import pytest 
from main import *


def test_mycrawler():
    output=mycrawler("https://ensai.fr")
    resu=[]
    with open('crawled_webpages.txt') as f:
        for line in f:
            resu.append(line.strip())

    assert resu == output
       
