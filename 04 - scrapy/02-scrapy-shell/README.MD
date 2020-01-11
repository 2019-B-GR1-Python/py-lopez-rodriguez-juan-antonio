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








