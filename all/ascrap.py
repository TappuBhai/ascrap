# PRE-DEFINED LIBRERIES
import asyncio
import aiohttp
from bs4 import BeautifulSoup
import os
import json, time

# USER-DEFINED LIBRERIES
# from Exception import NetworkConnectionError



class ascrap:
    '''
    This is a class which requires to make a Response object while programming.
    '''
    DATA = ''
    def __init__(self, url):
        self._url = url

    def __save__():
        pass

        
    async def scrap(self) -> str: # Working as expected
        '''This method extract html content from the _url and make it a dictionary.\n* async function\n* Returns a scraped data as string'''
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self._url) as response:
                    ascrap.DATA =  await response.text()
        except:
            print("Please Enter the correct url..")

        
    def filter_html(self,tag:str=None, attr:list=[], attrV:list=[])-> list: # Having some issues
        '''This method takes two input first is attribute name and second is it's value and made a iterator which gives all the attr and its value containing lines.\n
        * Returns a filterd list\n
        * num. of elements in attr list must always equal to the num. of elements is attrV\n
        eg. response.filter(['class'], ['example'])
        '''
        soup = BeautifulSoup(ascrap.DATA,'html.parser')
        filteredData = []
        for i in range(len(attr)):
            filteredData = (str(soup.find_all(name=tag, attrs={attr[i] : attrV[i]})))

        return filteredData

    
    def save(self, filteredData:list, path:str)->int: # Also working well
        ''' This method save the file extracted info in to a json file.\n
        Returns 1 on success, 0 of failier\n
        Arguments:\n
        filteredData:iter -> returned value from filter method\n
        path:str -> full path with file name where the file is to save 

        '''
        Data = json.loads(json.dumps(filteredData,indent=3))
        if Data != []:
            with open(path,'w+') as file:
                file.write(Data)
                return 1
        print("There is no such item present plese provide a valid parameters.\nThank you, Ask me soon..")
        return 0
        



        
def scraper(url:str, path:str, tag:str=None, attr:list=[], attrV:list=[], onScreen=False) -> None:
        '''This method automatically extract all the required data from the site
            Parameters:\n
            * Positional arguments\n
            \t1. url-> url of the website \n
            \t2. path-> complete path of the destination where you want to store the web data\n
            \t3. attr -> List of name of the attrribute you want to extract\n
            \t4. attrV-> List of the attributes values\n
            * 

        '''
        response = ascrap(url)
        asyncio.run(response.scrap())
        data = response.filter_html(tag,attr,attrV)
        if onScreen == True:
            print(data)
            return
        if data != []:
            response.save(data,path)
        else:
            print("There is no such item present plese provide a valid parameters.\nThank you, Ask me soon..")



def isOpen(url:str)->bool:
    value = os.system(f"ping -c 1 {url} > /dev/null 2>&1; ")
    if value == 512:
        return False
    else:   
        return True


            
        

if __name__ == "__main__":
    st = time.time()
    url = 'https://www.scrapme.com.au/'
    path = '/home/tappubhai/Playground/Programing/Project/ascrap/Scraped/data2.html'
    attr = ["id","class"]
    attrV = ["ki1","img-fluid"]
    print("Strating")
    response = ascrap(url)
    scraper(url,path,tag='img',attr=attr, attrV=attrV,onScreen=True)
    print("ended")
    print(time.time() - st)
