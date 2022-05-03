import requests
import bs4
import csv

class Page:
          
          def __init__(self):

                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36", 
                    "Accept-Encoding":"gzip, deflate", 
                    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
                    "DNT":"1",
                    "Connection":"close",
                    "Upgrade-Insecure-Requests":"1"
                    }

                    #get the html for the page
                    page_html=requests.get(self.url,headers=headers).content
                    self.page=bs4.BeautifulSoup(page_html,"lxml")
                    

class Data:
          
          def __init__(self):

                    #product name
                    product_name_components=self.page.find(id="productTitle").get_text().strip()
                    self.product=" ".join(product_name_components)
                    
                    #product price
                    price_html_components=self.page.find_all("span",class_=["a-offscreen"])
                    self.price=price_html_components[0].get_text()


class Excel:
          
          def __init__(self):
                    header=["name","price"]
                    data=[self.product,self.price]
                    with open("amazon_webscrape_data.csv","w",newline="",encoding="UTF8") as excel_file:
                              writer=csv.writer(excel_file)
                              writer.writerow(header)
                              writer.writerow(data)


class URL(Page,Data,Excel):
          
          def __init__(self,name,url):
                    self.name=name
                    self.url=url
                    Page.__init__(self)
                    Data.__init__(self)
                    Excel.__init__(self)


if __name__=="__main__":
          
          amozon=URL("Amozon","https://www.amazon.com/Nintendo-Switch-Neon-Blue-Joy%E2%80%91/dp/B07VJRZ62R/?_encoding=UTF8&pd_rd_w=4GEPX&pf_rd_p=716a1ed9-074f-4780-9325-0019fece3c64&pf_rd_r=K54EWM7WHFZWNZ3Z78NV&pd_rd_r=8e3f53ba-5709-4390-a4df-f56c5e5f2134&pd_rd_wg=1bM2C&ref_=pd_gw_ci_mcx_mr_hp_atf_m&th=1")
          
          print(amozon.price)
          with open("test.txt","w",encoding="utf-8") as test_file:
                    test_file.write(amozon.product+"\n"+amozon.price)
