
import requests
from bs4 import BeautifulSoup
import Funciones_scraping
#se hace una peticion mediante http de la pagina web"
page = requests.get('https://www.pccomponentes.com/xiaomi-mi-smart-band-5')
#Sirve para ver en detalle el contenido de la web
soup = BeautifulSoup(page.content,'html.parser')
#procesando el texto codigo de la pagina web y buscando el elemento que deseamos 'div' => 'id=precio-main'
#result = soup.find('div',{'id':'precio-main'})
#procesando el texto codigo de la pagina web y buscando el elemento que deseamos 'div' => 'class=precioMain h1'
result = soup.find('div',{'class':'precioMain h1'})
#imprimimos el contenido con .text
precioActual_texto = result.text
precioActual = precioActual_texto.replace("€","")
precioActual = int(float(precioActual.replace(",",".")))
#Establecemos un precio deseado para comparar",
precioDeseado = 30
print ("\nEl precio máximo deseado para este producto es de "+ str(precioDeseado)+"€\n")

global hayOferta
#Calcula el precio
hayOferta = Funciones_scraping.Oferta_Precio_Deseado(precioActual,precioDeseado)

if(hayOferta):
    print("Tenemos OFERTA! - Avisamos al usuario!")
    #avisar por telegram
    import aviso_telegram
    aviso_telegram
else:
    print("No hay oferta.")