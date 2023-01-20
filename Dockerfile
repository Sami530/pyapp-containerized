#
FROM python:3.9


ADD WebScrapping.py .

RUN pip install requests BeautifulSoup4

CMD [ "python","./WebScrapping.py" ]