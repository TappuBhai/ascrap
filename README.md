# ascrap
This python library is totally written in python and also fetches html content from the browser.


How To Use:
 1. make a response object to capture all the html
    * response = ascrap(url) -> url is the web address of the target.
 2. Now you are good to go.


Functions:
 * There are at most 3 to 4 resonse function
    1. response.scrap() -> This is a async function, so you must use it with asyncio.run()
       Parameters : None
    2. response.filter() -> This funtion shape your html content in small html as you wish.
       Parameters :
       1. tag:str=None -> kwarg, tag you want to fetch
       2. attr:list=[] -> kwarg, attribute contain in the tag
       3. attrV:list=[] -> kwarg, value of the attribute respectly to the above attribute list index
       ** Remember if you don't provide attrV or attr and provide some param values that the html content missing then you got a empty list
  
   3. response.save() -> Save the file to the given path
      Parameters:
      1. filterdData -> Data you finaly select
      2. Path -> Address of the file where you want to store the html


* more funtion on the file
  1. scraper() -> It is not a response method. This function combines all the above processes and do them automatically rather than manually
     Parameters:
     1. url -> url is the web address of the target.
     2. Path -> Address of the file where you want to store the html.
     3. tag:str=None -> kwarg, tag you want to fetch
     4. attr:list=[] -> kwarg, attribute contain in the tag
     5. attrV:list=[] -> kwarg, value of the attribute respectly to the above attribute list index
     ** Remember if you don't provide attrV or attr and provide some param values that the html content missing then you got a empty list
     6. onScreen: False -> This parameter decides whether the file get stored or displayed on the screen.






