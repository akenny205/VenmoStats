# VenmoStats
VenmoStats is a simple data analytics tool to explore a users historical
Venmo data. It has data on all transactions, with the note sent, amount paid, and date of the transaction.

### Features include:
- Viewing all transactions
- Viewing transaction history between specific users
- Viewing overall data
- Exploring a cool keyboard mashing algorithm

### Setup:
Because Venmo does not offer a public api, getting your Venmo data is going to 
be somewhat tedious. Venmo allows you to download monthly reports in the form of csv files.
In order to use this tool, you need to download each months csv file, and put them in a folder
of your choosing. I have mine in a folder called "transactions". No naming conventions are necessary for the 
csv files once they are in the folder of your choosing. Simply change the folder variable in the venmo.py
file. I chose to name my files under a specific naming convention, so if you do not wish to mirror this, simply change the
"csvs" variable to just look for all the files in the folder instead. Lastly make sure the change the "acc_holder" variable
so the code knows who is the user. 

### Starting the GUI
This tool was made using streamlit. Simply run "streamlit run Home.py" and the localhost streamlit 
window will open in your browser




