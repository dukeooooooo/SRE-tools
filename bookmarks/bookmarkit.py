import sys
from bs4 import BeautifulSoup
import time

# Check if the HTML file path is provided as an argument
if len(sys.argv) < 2:
    print("Please provide the path to the HTML file as an argument.")
    sys.exit(1)

html_file = sys.argv[1]

print('''<!DOCTYPE NETSCAPE-Bookmark-file-1>
<!-- This is an automatically generated file.
     It will be read and overwritten.
     DO NOT EDIT! -->
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<TITLE>SRE Tools</TITLE>
<H1>SRE Tools</H1>
<dl><p>
      ''')

# Read the HTML file
with open(html_file, 'r') as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all <h2> headers
h2_headers = soup.find_all('h2')

# Get the current time in Unix time
current_time = int(time.time())

# print a dummy header for the bookmars
print(f'<DT><H3 PERSONAL_TOOLBAR_FOLDER="TRUE" ADD_DATE="{current_time}" >SRE Tools</H3><dl><p>')

print('<dt><a href="https://collaborate.akamai.com/confluence/display/GPO/EPRE+SRE+Tools" ADD_DATE="{}" LAST_MODIFIED="{}">EPRE SRE Tools</a>'.format(current_time, current_time))
# Iterate over the <h2> headers
for h2 in h2_headers:
    header_text = h2.get_text(strip=True)
#    if h2 == h2_headers[0]:
#        print(f'<DT><H3 PERSONAL_TOOLBAR_FOLDER="TRUE" ADD_DATE="{current_time}" >{header_text}</H3><dl><p>')
#    else:
#        print(f'<DT><H3 ADD_DATE="{current_time}" LAST_MODIFIED="{current_time}">{header_text}</H3><dl><p>')

     # Iterate through siblings until the next <h2> is found
    for sibling in h2.find_next_siblings():
        if sibling.name == 'h2':
            break
        # Find all <a> tags within the current sibling
        a_tags = sibling.find_all('a')
        for a in a_tags:
            href = a.get('href')
            link_text = a.get_text(strip=True)

            print('<dt><a href="{}" ADD_DATE="{}" LAST_MODIFIED="{}">{}</a>'.format(href, current_time, current_time, link_text))

    #print ('</dl><p>')
 
print ('</dl><p>')