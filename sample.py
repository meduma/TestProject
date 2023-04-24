# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

# Importing the necessary libraries
from bs4 import BeautifulSoup
import requests

# Sending a GET request to a sample URL and extracting the HTML content
res = requests.get('https://www.example.com')
soup = BeautifulSoup(res.content, 'html.parser')


if __name__ == "__main__":        
   
    print("SSample run done.")