from bs4 import BeautifulSoup
import openpyxl


# READ data
with open('consumer.txt', 'r') as file:
    data = file.read()

# SCRABE DATA
soup = BeautifulSoup(data, 'lxml')
products = soup.find_all('a', class_ = 'products-a-z__results__item')
product_catagory={}
for product in products:
    product_name = product.string.replace('\n','')
    if product_name[0] in product_catagory.keys():
        product_catagory[product_name[0]].append(product_name)
    else:
        product_catagory[product_name[0]] = [product_name,]

product_links = [[link.string.replace('\n',''), link['href']] for link in products]


#STORE DATA

wb = openpyxl.Workbook()
link_sheet = wb.create_sheet('product links')
catagory_sheet = wb.active
catagory_sheet.title = 'product catagory'
for key,value in product_catagory.items():
    for index,product in enumerate(value,1):
        catagory_sheet[key + str(index)] = product

for product in product_links:
    link_sheet.append(product)

wb.save('consumer_report.xlsx')
