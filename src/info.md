# Documentation


**Magellan** is a simple command line interface tool (CLI) which allows you to analyse the accessibility of your data from all parts of the world. We have partnered up with BrightData to enable this service, therefore in order for the application to function you ***will need to have/create a [BrightData](brightdata.com) account***

## Requirements

> Apart from a BrightData account here are 3 pieces of data that you will need:
- [ ✅ ] BrightData customerID
- [ ✅ ] BrightData proxy password
- [ ✅ ] URL that you want to analyse


> Here is where you can find the above:
 1. Go to [BrightData](brightdata.com)
 2. Log in and open your user dashboard
 3. Open left side menu
 4. *API & Integrations > Proxy & Web Unlocker API > Other Software*
 5. **User** is your customerID and **Password** is your password

## Application

> Once you open the app, you will see the folloing menu options:
- INFO: Documentation for the application
- LOGIN: Initiates authentication
- EXIT: Exits the application

> Once logged in your menu options your should also find:
- RUN: Prompts you for URL runs the programme on that URL
- LOGOUT: Logs you out

> Each RUN request will generate an *analysis* folder containing results of all queries separately in JSON formats and a *summary.txt* file containing the summary of all requests in table format
 
> The JSON files representing a request from a country will contain:
- url -> URL that the query has been run on
- status_code -> Status code of the HTTPResponse
- headers -> Headers of the HTTPResponse
- text -> HTML retreived from the url in string format

&nbsp;


