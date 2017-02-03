# How did Vermont's senators vote on Trump's cabinet nominees?

The code here powers the table in [this](http://digital.vpr.net/post/vote-tracker-how-bernie-sanders-patrick-leahy-are-voting-trumps-cabinet-picks) VPR digital news post. It pulls data from a Google Spreadsheet and is embedded into our CMS through pym.js.


##Notes on the Project

The project was built off of VPR's [App Template](https://github.com/vprnet/app-template). The steps to get set up are here:

1. Make sure you have Python 2.7 installed.
1. Clone the repo locally. `git clone git@github.com:vprnet/cabinet-votes-2017.git`
1. [Install `pip`](https://pip.pypa.io/en/latest/installing.html)
1. Install virtualenv. `pip install virtualenv`
1. Change into the project directory. `cd cabinet-votes-2017`
1. Create a virtual environment for the app. `virtualenv venv`
1. Enter the virtual environment. `source venv/bin/activate`
1. Install the app requirements. `pip install -r requirements.txt`
1. To run locally, hit a quick	`python runserver.py` and head to `127.0.0.1:5000`, but know that it will be broken until you follow the Google Spreadsheet steps below.


##Notes on Interacting with Google Spreadsheets

The project is hooked up to a Google Spreadsheet that VPR reporters can populate. If you're interested in cloning this project, you'll need your own Google Spreadsheet to get started.

We use [gspread](https://github.com/burnash/gspread) with the Drive API to connect our spreadsheet to the app. Here are a few things to know about the implementation:

1. To start a new project, head to the [Google Developer's Console](https://console.developers.google.com/project).
1. Click `create a project`. Give it a name.
1. Click `Enable and manage APIs`.
1. Under `Google Apps APIs` click `Drive API` and `Enable`.
1. Click `Go to Credentials`.
1. `Create Credentials`.
1. `Create service account key`, and select `New service account`. Give it a name.
1. When you `create`, you'll see a JSON file incoming. Save that file to your project directory. Add it to your gitignore if your code is going anywhere public.
1. The json file is what gets loaded and opened in `sheet.py`. Make sure the names match.
1. Create a Google Spreadsheet through your Google Drive. Make sure your spreadsheet title is exactly what's trying to be opened in `sheet.py`'s `authorization.open("")` line. To match our project, you'll need a worksheet with columns: `Position`, `Nomination`, `Committee_Vote_Leahy`, `Committee_Vote_Sanders`, `Full_Vote_Senate_Approval`, `Senate_Vote_Leahy`, `Senate_Vote_Sanders`, `Senate_Vote_Date`, and `Nominee_Confirmed`.
1. You may need to *share your Google Spreadsheet* with the email provided in `client_email`.
1. If you have problems running the project locally, you'll likely need to need to `pip install gspread` and `pip install oauth2client` and maybe even `pip install pycrypto`.
