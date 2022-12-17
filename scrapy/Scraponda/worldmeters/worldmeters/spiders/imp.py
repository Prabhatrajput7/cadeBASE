#   conda install -c conda-forge scrapy==1.6 pylint autopep8 -y # y means yes to all
#   scrapy 
#   scrapy bench 
#   scrapy startproject worldmeters
#   scrapy genspider -l # to get all the template
#   scrapy genspider -t crawl bestmovies web.archive.org/web/20200715000935if_/https://www.imdb.com/search/title/?groups=top_250&sort=user_rating
#   scrapy genspider countries www.worldometers.info/world-population/population-by-country
#   conda install ipython
#   conda install protego
#   scrapy shell "URL"
#   fetch("https://www.worldometers.info/world-population/population-by-country/") or #8
#   r = scrapy.Request(url="https://www.worldometers.info/world-population/population-by-country/")
#   fetch(r)
#   response.body
#   view(response)
#   tx = response.xpath("//h1/text()")
#   tx
#   tx.get()
#   tc = response.css("h1::text")
#   country = response.xpath("//td/a/text()").getall() for multi elements
#   country_css = response.css("td a::text").getall()
#   scrapy crawl countries #to run a py file in terminal scrapy

#   DEBUGGING
#   scrapy parse --spider=countries -c parse_country https://www.worldometers.info/world-population/china-population/
#   scrapy parse --spider=countries -c parse_country --meta='{\"countryname\":\"China\"}' https://www.worldometers.info/world-population/china-population/

# Python3 implementation this is to use itertools.
# permutations as coded below:

#   css selector
#   .class.class || .class [name]
#   #class.#class || #class [id]
#   [abrname = 'value']
#   [abrname ^= 'start']
#   [abrname *= 'b/w']
#   [abrname $= 'end']
#   ele1 [spavce] ele2
#   ele > ele2 to select ele2 children of ele 
#   ele + ele2 next to tag immediately after
#   div ~ p div get p which is not directly below it
#   nth-child(position)
#   div class = div.class name || div id = div#idname
#   tag class = A B => .A.B
#   li date=7 item1 li close => li[date=7]
#   a href = http or a href = https u want to selecte hhtps a[href^='https'] ^beg to select end $=com
#   div[p[span id='']] to get p div.classname space p to get span div.classname space p,span#idname or div.classname space p,#idnmae
#   li:nth-child(1),li:nth-child(3) ||  li:nth-child(even)
#   div contains to p so div.class>p


#   Xpath
#   //div
#   //div[@class='name]
#   //div[@class='name]/p or //div[@class='name]/p[1]
#   li[position() =1 or position() =4] || li[position()>1] || li[postion() = 1 and contains(@text,'hello')] position = last() li[1 or 4]
#   starts-with(@href,'https'), contains and ends-with()[not avilable in version 1.0]  || beg, b/w and end
#   axisname::element name an-> parent, ancestor[grandparent], preceding[all ele] and preceding-sibling element name can de node()
#   axisname::element name an-> child, following[all ele], following-sibling[next ele] and descendant[child and grand child]
#   div is parent of p p[@='']/parent::node() || ancestor || to get p as well [ancestor-or-self] || preceding above element p/receding-sibling::node()
#   div got to child p div[]/child::p or child::node()
#   To get all element after div close div[]/following::node() ||following-siblient::node()[fetch all tags that share same parents]
#   decendant all tags under a tag /decendent::node()


#   alt+shilf+f to format json file in right format
#   scrapy crawl countries -o populationdb.json[.csv][.xml] #json file
#   ctrl+ship+p to disable js

#   URL https://web.archive.org/ || https://web.archive.org/web/20190225123327/https://www.tinydeal.com/specials.html

#   FEED_EXPORT_ENCODING = 'utf-8' place this in setting.py to get right encording

# HEADDERS

#   USER_AGENT = 'tinydeal (+http://www.yourdomain.com)' setting.py
#   USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36' setting.py
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# DEFAULT_REQUEST_HEADERS = {
#     'User_Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
# }

#   'name': glass.xpath("normalize-space(.//div[@class='p-title']/a/text())").get(), normalize-space space like click   me -> click me