# hedgehogs

## How to run
* Clone the repository
* Navigate to hedgehogs/data_collection
The current pipeline currently looks something like this:
  xlsxDownloader --> xlsx2json.py --> json2mongodb.py
In order to run the program do the following:
* run `python xlsxDownload.py TICKER` to download the .xlsx files
* run `python xlsx2json.py FILE_NAME` to convert a .xlsx to .json
* run `python json2mongodb.py FILE_NAME` to send the .json file to a running MongoDB server


## Installation (deprecated)
* Install either Miniconda or Anaconda
  * Miniconda https://conda.io/miniconda.html
  * Anaconda https://www.anaconda.com/download/
* Configure the PATH system variable as such
  * `export PATH=~/miniconda2/bin:$PATH`
  * `export PATH=~/anaconda2/bin:$PATH`
* Verify Installation of Anaconda/Miniconda
  * `conda --version`
* Install Zipline
  * `conda install -c Quantopian zipline`
  * Yes, we are using Quantopian's API..
  
