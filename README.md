# VenmoStats
VenmoStats is a simple data analytics tool to explore a users historical
Venmo data. It has data on all transactions with the note sent, amount paid, and date of the transaction.

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

# Example Usage:
![Screenshot 2025-01-26 at 6 04 57 PM](https://github.com/user-attachments/assets/da811861-ab11-442b-88b1-1e820f80e1bb)


<img src="https://github.com/user-attachments/assets/a3d591ff-1796-4cab-ad0c-019d1820efba" width="400" />

<img src="https://github.com/user-attachments/assets/aa9a7b66-bd28-434e-8e29-7abb116ffb11" width="350" />

<img src="https://github.com/user-attachments/assets/ff156465-ed69-43aa-8e54-27dd2d0dadcc" width="550" />

