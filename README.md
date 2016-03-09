Used Python's BeautifulSoup module to scrape the following forum (pages 1-9) after some thorough investigation of the page source:
http://www.oldclassiccar.co.uk/forum/phpbb/phpBB2/viewtopic.php?t=12591

The script outputs the scraped data to a file called "forum.csv" in the following format: [postID,posterName,postTime,postBodyText].