import sys
import os 
import datetime 
import pandas as pd 

def main():
    sales_csv = get_sales_csv()
    orders_dir = create_orders_dir(sales_csv)
    process_sales_data(sales_csv, orders_dir)

# Get path of sales data CSV file from the command line
def get_sales_csv():
    # Check whether command line parameter provided
    number_parameters = len(sys.argv) -1 
    if number_parameters >=1:
        csv_path = sys.argv[1]
    # Check whether provide parameter is valid path of file
    if os.path.isfile(csv_path):
        return os.path.abspath (csv_path)
    else:
        print('Error: Missing CSV file path.')
        sys.exit(1)
    

# Create the directory to hold the individual order Excel sheets

def create_orders_dir(sales_csv):

    # Get directory in which sales data CSV file resides
    sale_directory = os.path.dirname(sales_csv)
    # Determine the name and path of the directory to hold the order data files
    todays_date =datetime.date.today().isoformat()
    orders_directory_name = f'Orders_{todays_date}'
    orders_directory_path = os.path.join(sale_directory,orders_directory_name )
    # Create the order directory if it does not already exist
    if not os.path.isdir(orders_directory_path):
        os.makedirs(orders_directory_path)
    
    return orders_directory_path 

# Split the sales data into individual orders and save to Excel sheets
def process_sales_data(sales_csv, orders_dir):
    # Import the sales data from the CSV file into a DataFrame
   sales_df =  pd.read_csv('data.csv')

    # Insert a new "TOTAL PRICE" column into the DataFrame
    # Remove columns from the DataFrame that are not needed
    # Group the rows in the DataFrame by order ID
    # For each order ID:
        # Remove the "ORDER ID" column
        # Sort the items by item number
        # Append a "GRAND TOTAL" row
        # Determine the file name and full path of the Excel sheet
        # Export the data to an Excel sheet
        # TODO: Format the Excel sheet
   pass

if __name__ == '__main__':
    main()