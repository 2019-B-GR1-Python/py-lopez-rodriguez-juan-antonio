# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=238&s=150Ypp=25

import scrapy
from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import TakeFirst

def transformar_url_imagen(texto):
    url_fybeca = 'https://www.fybeca.com'
    cadena_texto = '../..'
    return texto.replace(cadena_texto, url_fybeca)


class ProductoFybeca(scrapy.Item):
    titulo = scrapy.Field()
    imagen = scrapy.Field(
        input_processor = MapCompose(
            transformar_url_imagen
        ),
        output_processor = TakeFirst()
    )

class  AraniaFybecaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
