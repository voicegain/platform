import csv

# Define the input CSV file path
csv_file_path = "./call_id-dataObj_id.csv"

# Open the CSV file and read its contents
with open(csv_file_path, mode='r') as infile:
    reader = csv.DictReader(infile)
    
    # Iterate over each row in the CSV file
    for row in reader:
        call_id = row['call_id']
        data_object_id = row['data_object_id']
        
        # Generate the SQL update query
        sql_query = f"UPDATE sa_call SET recording = '{data_object_id}' WHERE call_id = {call_id};"
        
        # Print the SQL update query
        print(sql_query)