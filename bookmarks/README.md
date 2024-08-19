# Generate bookmarks

From the Confluence page at  https://collaborate.akamai.com/confluence/display/GPO/EPRE+SRE+Tools
We want to generate an importable bookmarks file for Chrome.

To update
From the Confluence page, click on the three dots on the upper right and select "view source"
From the source page, right click and save as an HTML page

run bookmarikit.py <foo> where foo is the name of the file you just saved.
The output will go to terminal so directed it to a file, sretools.html

From Chrome, open Bookmark Manager.
Click on the three vertical dots, and select "Import Bookmarks", and select your sretools.html
Bookmarks will be available under "Imported Bookmarks"
