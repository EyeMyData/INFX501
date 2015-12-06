## import webbrowser
## webbrowser.open('http://inventwithpython.com/')

##sudo pip install requests
import requests, bs4
import html5lib
import csv
import unicodedata

from unicodedata import normalize

##import codecs
##import sys 
##UTF8Writer = codecs.getwriter('utf8')
##sys.stdout = UTF8Writer(sys.stdout)

import sys
reload(sys)
sys.setdefaultencoding('utf8')

## import sys
## sys.stdout.buffer.write(chr(9986).encode('utf8'))

## res = requests.get('http://nostarch.com')
res = requests.get('https://azure.microsoft.com/en-us/updates/')
res.raise_for_status()
## AzureSoup = bs4.BeautifulSoup(res.text,"html.parser")
AzureSoup = bs4.BeautifulSoup(res.text,'html5lib')

## text1 = AzureSoup.select('span class')
## text2 = AzureSoup.find_all('a')

## Original code to grab all div elements
##text2 = AzureSoup.find_all('div','wa-serviceUpdate')
##print(text2[4])

## text1 = AzureSoup('div', {'class' : 'data-services'})

text1 = AzureSoup.find_all('div', {'class' : 'wa-serviceUpdate'})
##
##unicode(string[, encoding, errors])
##unicode(text1, errors='ignore')

## text1.encode('ascii', 'ignore')
## text1.encode('utf-8')

csvFile = open('/Users/ryanbrush/Documents/INFX501/output.txt', 'w')
##csvWriter = csv.writer(csvFile, delimiter=':', lineterminator='\n')
##csvWriter.writerow(['Data_Services', 'Data_Platforms', 'Update_Date', 'Update_Types', 'Update_Title', 'Update_Description'])
## csvRows = [ ]

csvFile.write('Data_Services$Data_Platforms$Update_Date$Update_Type$Update_Title$Update_Description' + '\n')
##
with open('/Users/ryanbrush/Documents/INFX501/output.txt', 'w'):
    for div in text1:
    ## print(div['data-services'], ":" ,div['data-platforms'], ":" , div['data-updatetypes'], ":" , div('span',{'class':'wa-date'}), ":" , div('a'), ":" , div('p') )
    ## print(div['data-services'], ":" ,div['data-platforms'], ":" , div['data-updatetypes'], ":" , div.span({'class':'wa-date'}))
    ## print(div['data-services'], ":" ,div['data-platforms'], ":" , div['data-updatetypes'], ":" , div('span','wa-date') )
    ## str(u":".join(div['data-services'], ":" ,div['data-platforms'], ":" , div['data-updatetypes'], ":" , div.span.text.split('>') , ":" , div.a.text.split('>'), ":" , div.p.text.split('>')) )
    ##print(div['data-services'] + ":" + div['data-platforms'] + ":" + div['data-updatetypes'] + ":" + div.span.text.split('>') + ":" + div.a.text.split('>') + ":" + div.p.text.split('>') )
 ##       div.text.encode('ascii','ignore')
        csvFile.write(div['data-services'] + "$" + div['data-platforms'] + "$" + ', '.join(div.span.text.split('>')) + "$" + div['data-updatetypes'] + "$" + ', '.join(div.a.text.split('>')) + "$" + ', '.join(div.p.text.split('>')) + '\n' )
 ##   csvRows.append(1:2:3:4:5:6)
## return csvRows
## csvRows.append

## csvWriter.writerow(csvRows)
csvFile.close()



 ##   unicodestring = str(div.span.text.split('>') )

 ##   asciistring = unicodedata.normalize('NFKD', unicodestring).encode('ASCII', 'ignore')

    ## unicodestring.encode('ascii')
    ## asciistring = unicodestring.encode('ascii')
 ##   asciistring = unicodestring.normalize()
    ##.encode('ascii', 'replace')
 ##   print(asciistring)
##    text10 = u div['data-services']
##    text11 = div['data-services']
##    print(text10.decode('utf8'), text11.decode('utf8'))
## print(text1)
## csvRows.append
 ##       .decode('utf8')
##csvWriter.writerow(csvRows)
##csvFile.close()

##         str(u":".join(csvRows))
## text2 = AzureSoup.find_all('div','wa-serviceUpdate')
## text2 = AzureSoup.find_all('div span', 'wa-date')

##for post in text2:
##    print (post.['data-platforms'] , ":" , post.['data-updatetypes'])

## text2 = AzureSoup.select('div span')
    
    
## attrs={'id':'articlebody'})
##str(text2[1])
##print(text2[1].attrs)

##samples = text2[1]
##print(samples)


## source.find('div', attrs={'id':'articlebody'})
##elems = AzureSoup.select('#class')
##print(elems[0].attr)

##mydivs = AzureSoup.findAll("div", { "class" : "wa-serviceUpdate" })
##sample2 = samples.getText()
##print(noStarchSoup)

## print(mydivs)
## print(sample2)


## <span class="wa-date">November 12, 2015</span>


##div class="wa-serviceUpdate"
##from BeautifulSoup import BeautifulSoup
##import requests
##
##url = 'http://stefan.sofa-rockers.org/search/?q=%(q)s'
##payload = {
##    'q': 'Python',
##}
##r = requests.get(url % payload)
##
##soup = BeautifulSoup(r.text)
##titles = [h2.text for h2 in soup.findAll('h2', attrs={'class': 'post_title'})]
##
##for t in titles:
##    print(t)


##pycharm


## python /Users/ryanbrush/Documents/INFX501/Web_Scrape.py

## res = requests.get('https://azure.microsoft.com/en-us/updates/')


