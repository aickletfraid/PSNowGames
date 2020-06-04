# PSNowGames
Game List for PS Now Games

https://github.com/aickletfraid/PSNowGames/blob/master/psnowgamelist3-2.csv

This is a short script for fetching available games on the Playstation Now platform by Sony.
It supports the region: USA and Europe


Necessary modules for the script: requests, html2json, bs4, bs2json, ast

Install them via pip to your Python environment.

You can run the "Gamelist PS Now new.ipynb" first and then "US and Europe in one list.ipynb" to get the complete list with Jupyter Notebook.

Otherwise run "usa_and_europe.py" with Python. It has a better database than the first script.
```sh
$ python usa_and_europe.py
```

In both cases a new "psnowgamelist.csv" file will be created with all the games.

------------------------

License
----

MIT

This project has no affiliation with "Sony" or "Playstation" and its similar products at all in any way.

Sony, Sony Entertainment Network, Playstation,  are trademarks or registered trademarks of Sony Corporation.

DUALSHOCK, PlayStation, PS2, PS3, PS4, “PSN”  are trademarks or registered trademarks of Sony Interactive Entertainment Inc.
