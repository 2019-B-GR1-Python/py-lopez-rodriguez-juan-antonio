# Scrapy
## Scrapy intlacion

## Ejecutar dentro del `Anaconda prompt`
```
$ pip install scrapy
```

## Comandos generales
Da `las caracteristicas` para poder hacer web Scraping o web Crawling de ese computador.
```
$ scrapy bench
```

## Comandos generales
Visualizar `las configuraciones` extras
```
$ scrapy settings
```

Visualizar la `version` de scrapy
## Comandos generales
```
$ scrapy version
```

### scrapy view `url`

`Visualizar el contenido como lo ve scrapy`
Si se ve el contenido
```
$ scrapy view https://www.pluralsight.com/authors
```

No se ve el contenido
```
$ scrapy view https://srienlinea.sri.gob.ec/sri-en-linea/inicio/NAT
```

### scrapy shell `url`
Permite interactiar con la respuesta del scrapy
```
$ scrapy shell http://quotes.toscrape.com/
```

`No buscamos por identificador porque solo debe y suele haber uno en cada pagina, por lo que no ayuda mucho esa informacion`
```
$ response.css('title')

$ response.css('title').extract()

$ response.css('title::text').extract()

$ response.css('.author').extract()

$ response.css('.author::text').extract()

$ type(response.css('.author::text'))

$ response.css('.author::text')[0]

$ response.css('.author::text')[0].extract()

$response.css('.author::text').extract_first() 

$len(response.css('a.tag::text').extract())

$ len(response.css('div.tags > a.tag::text').extract())

$ len(response.css('.quote >div.tags > a.tag::text').extract())

$  response.css('.quote >div.tags > a.tag::text').extract()

 $ response.css('div.tags > a.tag::attr(href)').extract_first()


```


Extraer solo los links de los autores (about)
```
$ len(response.css('div.quote > span > a::attr(href)').extract())
```

`SEGUNDA CLASE`
XPATH permite realizar lo que ya conocemos de forma diferente y mas simple
```
$ response.xpath('//title').extract()

$ response.css('.row > div > div:nth-child(2) > .text::text').extract()

$ response.xpath("/html/body/div/div[2]/div[2]/h2").extract()

$ response.xpath("/html/body/div/div[2]/div[2]/h2/text()").extract()

$ response.xpath("//div[@class='quote']").extract_first()

$ response.xpath("//div[@class='quote']/span[@class='text']/text()").extract_first()

```

Obtner el link de author
```
$ response.xpath("//div[@class='quote']/span/a/@href").extract_first()

```

`NOTA DEL INGE`
```
$ response.xpath('/html/head/title').extract()
$ response.xpath('//title').extract()
$ response.xpath('/html/body/div/div[2]/div[2]/h2').extract()
$ response.xpath('/html/body/div/div[2]/div[2]/h2').extract()
$ response.xpath("//div[@class='quote']/span[@class='text']").extract_first()
$ response.xpath("//div[@class='quote']/span[@class='text']/text()").extract_first()
$ //div[@class='quote']/span/a/@href").extract_first()

```

## scrapy startproject `Nombre_proyecto`
 
```
$ scrapy shell http://books.toscrape.com/
$ scrapy startproject arania_basica

$ scrapy crawl introduccion_spider
```

Para crawling se practica con:
`http://books.toscrape.com/`











