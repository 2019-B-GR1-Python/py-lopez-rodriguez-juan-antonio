import scrapy

class IntroSpider(scrapy.Spider):
    name = 'introduccion_spider'

    urls = ['http://books.toscrape.com/catalogue/category/books/travel_2/index.html', 'http://books.toscrape.com/catalogue/category/books/mystery_3/page-2.html','http://books.toscrape.com/catalogue/category/books/mystery_3/index.html',
'http://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html','http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html',
'http://books.toscrape.com/catalogue/category/books/classics_6/index.html','http://books.toscrape.com/catalogue/category/books/philosophy_7/index.html','http://books.toscrape.com/catalogue/category/books/romance_8/index.html',
'http://books.toscrape.com/catalogue/category/books/womens-fiction_9/index.html','http://books.toscrape.com/catalogue/category/books/fiction_10/index.html',
'http://books.toscrape.com/catalogue/category/books/childrens_11/index.html','http://books.toscrape.com/catalogue/category/books/religion_12/index.html','http://books.toscrape.com/catalogue/category/books/nonfiction_13/index.html','http://books.toscrape.com/catalogue/category/books/music_14/index.html','http://books.toscrape.com/catalogue/category/books/default_15/index.html',
'http://books.toscrape.com/catalogue/category/books/science-fiction_16/index.html','http://books.toscrape.com/catalogue/category/books/sports-and-games_17/index.html','http://books.toscrape.com/catalogue/category/books/add-a-comment_18/index.html',
'http://books.toscrape.com/catalogue/category/books/fantasy_19/index.html','http://books.toscrape.com/catalogue/category/books/new-adult_20/index.html',
'http://books.toscrape.com/catalogue/category/books/young-adult_21/index.html','http://books.toscrape.com/catalogue/category/books/science_22/index.html',
'http://books.toscrape.com/catalogue/category/books/poetry_23/index.html','http://books.toscrape.com/catalogue/category/books/paranormal_24/index.html',
'http://books.toscrape.com/catalogue/category/books/art_25/index.html','http://books.toscrape.com/catalogue/category/books/psychology_26/index.html','http://books.toscrape.com/catalogue/category/books/autobiography_27/index.html',
'http://books.toscrape.com/catalogue/category/books/parenting_28/index.html','http://books.toscrape.com/catalogue/category/books/adult-fiction_29/index.html',
'http://books.toscrape.com/catalogue/category/books/humor_30/index.html','http://books.toscrape.com/catalogue/category/books/horror_31/index.html',
'http://books.toscrape.com/catalogue/category/books/history_32/index.html','http://books.toscrape.com/catalogue/category/books/food-and-drink_33/index.html',
'http://books.toscrape.com/catalogue/category/books/christian-fiction_34/index.html','http://books.toscrape.com/catalogue/category/books/business_35/index.html',
'http://books.toscrape.com/catalogue/category/books/biography_36/index.html','http://books.toscrape.com/catalogue/category/books/thriller_37/index.html',
'http://books.toscrape.com/catalogue/category/books/contemporary_38/index.html','http://books.toscrape.com/catalogue/category/books/spirituality_39/index.html',
'http://books.toscrape.com/catalogue/category/books/academic_40/index.html','http://books.toscrape.com/catalogue/category/books/self-help_41/index.html','http://books.toscrape.com/catalogue/category/books/historical_42/index.html',
'http://books.toscrape.com/catalogue/category/books/christian_43/index.html','http://books.toscrape.com/catalogue/category/books/suspense_44/index.html',
'http://books.toscrape.com/catalogue/category/books/short-stories_45/index.html','http://books.toscrape.com/catalogue/category/books/novels_46/index.html','http://books.toscrape.com/catalogue/category/books/health_47/index.html',
'http://books.toscrape.com/catalogue/category/books/politics_48/index.html','http://books.toscrape.com/catalogue/category/books/cultural_49/index.html','http://books.toscrape.com/catalogue/category/books/erotica_50/index.html','http://books.toscrape.com/catalogue/category/books/crime_51/index.html', 'http://books.toscrape.com/catalogue/category/books/historical-fiction_4/page-2.html','http://books.toscrape.com/catalogue/category/books/sequential-art_5/page-2.html','http://books.toscrape.com/catalogue/category/books/sequential-art_5/page-3.html','http://books.toscrape.com/catalogue/category/books/sequential-art_5/page-4.html','http://books.toscrape.com/catalogue/category/books/romance_8/page-2.html','http://books.toscrape.com/catalogue/category/books/fiction_10/page-2.html','http://books.toscrape.com/catalogue/category/books/fiction_10/page-3.html','http://books.toscrape.com/catalogue/category/books/fiction_10/page-4.html']
        
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
            try:
                path = './LibrosURLs.txt'
                archivo_escritura_abierto = open(path,mode="a")
                archivo_escritura_abierto.writelines(titulos[elemento] + ' Precio: ' + precios[elemento] + '  Imagen:' + imagenes[elemento] + '\n')
                archivo_escritura_abierto.close()
            except Exception as error:
                print(f'Error:  {error}')
        
        for elemento in range(len(link_libros)):
            print(link_libros[elemento]) 
            
    






        