# Remote_job_searcher
Web page where you can search for a remote job using web scraping.<br>
https://repl.it/@SurimYuk/SuperScrapper

--------
## Functions
- [x] Web scraping
- [x] Export searched results into CSV file
- [x] Load data faster using fake DB
- [x] Apply button

--------
## Development environment
- IDE
> repl.it
- Language
> Python
- Library
> - Requests
> - BeautifulSoup
- Framework
> Flask

--------
## Details
- Web scraping
> Scrape information from these 3 pages:<br>
>> https://stackoverflow.com/jobs<br>
>> https://weworkremotely.com/<br>
>> https://remoteok.io/
- UI
> Setting UI with Flask.<br>
> Make HTML/CSS files and rendering on python file.
- Fake DB
> By using fake DB, load data faster which is already been searched fatser.
- Apply button
> You can go straight to the homepage where you can apply by pressing APPLY button
- Export
> Downloading a CSV file by using send_file in Flask

### @app.route()
- /home
> First page.<br>
> Get word from a user through input form.
- /report
> View the search results.<br>
- /export
> Download the search results in the form of a CSV file.

--------
## Preview
![image](https://user-images.githubusercontent.com/33217962/92355401-1a8dc400-f11f-11ea-916d-55466eecbd29.png)
![image](https://user-images.githubusercontent.com/33217962/92355375-0b0e7b00-f11f-11ea-9ad4-5ad67a810b47.png)
