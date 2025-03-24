import requests 

needed_headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}
response = requests.get("https://www.themoviedb.org/tv", headers = needed_headers 

# response.status_code
# 200
# The request was successful. We can get the contents of the page using response.text.
# dwn_content = response.text
# len(dwn_content)
# 223531

# dwn_content[:500]
# '<!DOCTYPE html>
# \n  <html lang="en" class="no-js">
# \n  <head>
# \n  <title>Popular TV Shows — The Movie Database (TMDB)</title>
# \n  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
# \n  <meta http-equiv="cleartype" content="on">
# \n  <meta charset="utf-8">
# \n  
# \n  <meta name="keywords" content="Movies, TV Shows, Streaming, Reviews, API, Actors, Actresses, Photos, User Ratings, Synopsis, Trailers, Teasers, Credits, Cast">
# \n  <meta name="mobile-web-app-capable" content="yes">
# \n  <meta name="'

#=============================

# Executing the HTML Source Code Using BeautifulSoup




