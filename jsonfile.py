import json

def add_data():
    file_name='data.json'
    try:
        with open(file_name,'r') as json_file:
            existing_file=json.load(json_file)
    except FileNotFoundError:
        existing_file={}
    data_input=input("Enter the data you want to add in your file: ")
        
    existing_file.update({'new_data': data_input})
    with open(file_name, 'w') as json_file:
        json.dump(existing_file, json_file, indent=4)
add_data()
    

def retrieve_data():
    file_name='data.json'
    
    try:
        with open(file_name,'r') as json_file:
            data=json.load(json_file)
            check=input("Do you want to see your input?(y/n) : ")
            if check == 'y':
                print("Data in the JSON file:")
                print(json.dumps(data, indent=4))
            if check == 'n':
                print("Ok! ")
    except FileNotFoundError:
        print("File not found. No data to display.")
        
retrieve_data()

def update_data():
    file_name='data.json'
    
    try:
        with open(file_name,'r') as json_file:
            existing_data=json.load(json_file)
        using_key=input("Enter the key you want to update: ").lower()
        
        if using_key in existing_data:
            new_value=input(f"Write new value for {using_key}:")
            existing_data[using_key]=new_value
            with open(file_name,'w') as json_file:
                json.dump(existing_data, json_file, indent=4)
            
            print(f"Value for {using_key} successfully updated:")
        else:
            print(f"Key {using_key} is not found:" )
    except FileNotFoundError:
        print("File not found and not updated.")
        
update_data()

def delete_data():
    file_name='data.json'
    try:
        with open (file_name,'r') as json_file:
            existing_data=json.load(json_file)
        delete_key=input("Write the key you want to delete: ")
        if delete_key in existing_data:
            del existing_data[delete_key] 
            
            with open(file_name,'w') as json_file:
                json.dump(existing_data, json_file, indent=4)
            print(f"Key {delete_key} is successfully deleted.")
    except FileNotFoundError:
        print("File not found.")
delete_data()
                
        
            
