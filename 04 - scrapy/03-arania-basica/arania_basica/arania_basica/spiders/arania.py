import scrapy

class IntroSpider(scrapy.Spider):
    name = 'introduccion_spider'

    urls = ['http://books.toscrape.com/catalogue/category/books/travel_2/index.html','http://books.toscrape.com/catalogue/category/books/mystery_3/index.html']

        
    def start_requests(self):
        for url in self.urls:
            # yield permite esperar hasta que se complete esa linea y no sea asincrono
            yield scrapy.Request(url=url)

    
    def parse(self, response):
        # utilizar css para obtener lo siguiente
        etiqueta_contenedora = response.css('article.product_pod')
        # podemos concatenar el selector de arriba con lo que queremos sacar
        titulos = etiqueta_contenedora.css('h3 > a::text').extract()
        #print(titulos)
        precios = etiqueta_contenedora.css('div.product_price > p.price_color::text').extract()
        #print(precios)
        
        imagenes = etiqueta_contenedora.css('div.image_container > a > img::attr(src) ').extract()
        
        link_libros =  response.css('li > ul > li > a::attr(href)').extract()
        
        path_imagenes = 'http://books.toscrape.com/'
        path_imagenes_reemplazar = '../../../../'
        
        path_link_libros = 'http://books.toscrape.com/catalogue/category/books'
        path_link_libros_reemplazar = '..'


        def completar_path(lista ,original, reemplazar):
            for cambio in range(len(lista)):
                lista[cambio] = lista[cambio].replace(reemplazar, original)


        completar_path(imagenes, path_imagenes, path_imagenes_reemplazar)
        completar_path(link_libros, path_link_libros, path_link_libros_reemplazar)
        


        for elemento in range(len(titulos)): 
            
            # falta aniadir http://books.toscrape.com/ antes de el link de la imagen
            #http://books.toscrape.com/catalogue/category/books/travel_2/index.html
            #falta guardar los link de la izquierda
            print(titulos[elemento] + ' Precio: ' + precios[elemento] + '  Imagen:' + imagenes[elemento])
            #print(precios[contador])
        
        for elemento in range(len(link_libros)):
            print(link_libros[elemento]) 
        

        