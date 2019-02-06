# NU-Daily-Diary-Automation
Now fill your IP daily diary just with a click of a button (Only for NIIT University, Neemrana).

# Prerequisites

1. Python 3.x
2. Virtualenv <b>(Optional)</b>
3. pip, Selenium and DateTime
4. WebDriver - I've used Chrome
5. A 'descriptions.txt' file 

# Installation 

## For linux based systems
1. Clone/Download this repository
2. Install [Python 3.x](https://askubuntu.com/questions/865554/how-do-i-install-python-3-6-using-apt-get) and Pip
```
$ sudo apt update
$ sudo apt install python3-pip
```
2. Install and create a virtual environment <b>(Optional)</b>
```
$ pip install virtualenv
$ cd /path/to/repository/
$ virtualenv env
$ source /env/bin/activate
```
3. Install selenium and datetime
```
$ pip install selenium
$ pip install DateTime
```
4. Download webdriver for your favourite browser. Following is the link for chrome : [Click here](https://chromedriver.storage.googleapis.com/index.html?path=2.46/)
5. Create a 'descriptions.txt' file with some random sentences to be added as a description in your daily diary. One line of the file will be randomly selected for the day. Make sure you also don't have other characters in your description that are not allowed as per nucleus. 
6. Open the file <i>NUcleusSelenium.py</i> and add your NUcleus UserName, NUcleus Password to variables NUUserName and NUPass on line 25 and 26 respectively.
7. Add path to WebDriver which you've downloaded to line 19 : self.driver
8. Keep your descriptions.txt file in the same folder as NUcleusSelenium.py and you're ready to go
9. Open terminal in the folder and run
```
python NUcleusSelenium.py
```
10. Click on OK when you'll get a prmpt saying "Successfully submitted your daily diary". Even if you don't click, it'll automatically close the window after 10 seconds.

## For Windows based systems

Follow same steps as above <br/>
Some useful links :<br/>
1. Installing [Python 3.x](https://realpython.com/installing-python/#windows)
2. Install and setup [pip and virtualennv](https://pymote.readthedocs.io/en/latest/install/windows_virtualenv.html)

# Coming Up Next / Thoughts in mind:
1. An executable file for Windows users
2. bak file which runs on startup for windows users - So you don't even need to runthe script. Script will automatically run when you'll start your computer on the day.
3. Daily diary automation for Mobile

# Disclaimer
I've just made this script for fun. If you're using it, it'll be your responsibilty. Making this repository public since few friends asked for it. Any problem with NU, CIC or your IP Organisation, if arises, will not be my responsibility. You'll be using it at your own risk.
