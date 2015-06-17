'''
Python Code to Extract Web Articles as Paragraphs
By Karl Brown ( thekarlbrown ) 17th June 2015

Utilizing the BeautifulSoup and Requests Libraries I developed an algorithm to clean and format HTML into paragraphs. 
This is part of my bigger project, Divination, which performs Market Analysis using News Articles, Stock Data, Neural Networks, and Genetic Algorithms.
Most news sites can be scraped using this approach I designed myself.
You first identify the section with the primary text, then mention any areas inside it to the algorithm
Headings, tweets, and paragraph spacing is also removed.
'''

import requests
from bs4 import BeautifulSoup

"""
Prints out contents of News Article as paragraph

articleURL - HTTP (no HTTPS) link to the article
coreIdentifier - id or class of HTML tag containing article text
coreIdentifierIsID - boolean specifying if identifier is id or not
idsToDecompose - List (default []) of known id's inside identified HTML tag to remove for specific site
classesToDecompose - List (default []) of known class's inside identified HTML tag to remove for specific site
"""
def parsedArticle (articleURL, coreIdentifier, coreIdentifierIsID,idsToDecompose,classesToDecompose):
	# Obtain the HTML tree
	articlePage = requests.get(articleURL)
	 
	# Create BeautifulSoup from HTML tree
	soup = BeautifulSoup(articlePage.content, "lxml")

	# Filter out data we are interested in
	soup = soup.find(id=coreIdentifier) if coreIdentifierIsID else soup.find(class_=coreIdentifier)

	# Remove junk tags included in target as identified by id or class
 	for idToRemove in idsToDecompose:
 		soup.find(id=idToRemove).decompose()
 	for classToRemove in classesToDecompose:
 		soup.find(class_=classToRemove).decompose()

 	#Removes any headings if present
 	for tags in soup.find_all('h1'):
 		soup.find('h1').decompose()
 	for tags in soup.find_all('h2'):
 		soup.find('h2').decompose()
 	for tags in soup.find_all('h3'):
 		soup.find('h3').decompose()

 	#Remove any twitter tweets attached in articles
 	for tweets in soup.find_all( class_='twitter-tweet'):
 		soup.find(class_='twitter-tweet').decompose()

 	#Output formatted text	
	print " ".join(soup.text.split())
	print "\t"

# Example targets
parsedArticle('http://arstechnica.com/apple/2015/06/apple-to-ios-devs-ipv6-only-cell-service-is-coming-soon-get-your-apps-ready/','article-content clearfix',False,[],['intro-image image center full-width'])
parsedArticle('http://recode.net/2015/06/16/apple-replaces-lead-contractor-on-new-spaceship-campus/','large-12 columns postarea',False,['jp-post-flair','recode-outbrain'],['post-send-off','row'])
parsedArticle('http://www.macrumors.com/2015/06/16/apple-watch-hacked-truly-native-apps/','content',False,[],['linkback'])
parsedArticle('http://qz.com/428935/apple-inc-is-hiring-journalists-who-want-to-work-a-40-hour-a-week-gig/','item-body',False,[],['article-aside','item-share-tools article-footer'])
parsedArticle('http://www.businessinsider.com/apple-text-message-ios-patent-2015-6','KonaBody post-content',False,[],['KonaFilter image-container float_right click-to-enlarge','see-also','margin-top popular-video'])
parsedArticle('http://www.cnbc.com/id/102763942','article_body',True,[],['player embed-container cnbcvideo autoplay'])
parsedArticle('http://appleinsider.com/articles/15/06/15/ios-9-code-points-to-apple-tv-apps-ipad-pro-keyboard-new-photos-feature','article',False,[],['gray small byline','font-sz right'])
