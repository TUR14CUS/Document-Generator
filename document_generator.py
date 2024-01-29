import pandas as pd
from datetime import datetime
from docxtpl import DocxTemplate

def get_user_input(prompt, data_type=str):
    while True:
        try:
            user_input = data_type(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid value.")

# Request personal information
my_name = get_user_input("Enter your name: ")
my_phone = get_user_input("Enter your phone number: ")
my_email = get_user_input("Enter your email: ")
my_address = get_user_input("Enter your address: ")

today_date = datetime.today().strftime("%d %b, %Y")

my_context = {'my_name': my_name, 'my_phone': my_phone, 'my_email': my_email, 'my_address': my_address,
              'today_date': today_date}

# Request CSV file path
csv_path = get_user_input("Enter the path to the CSV file: ")

# Request document template path
docx_template_path = get_user_input("Enter the path to the Docx template: ")

# Read data from CSV file
try:
    df = pd.read_csv(csv_path)
except FileNotFoundError:
    print(f"Error: File not found at {csv_path}")
    exit()

# Loop over DataFrame rows
for index, row in df.iterrows():
    context = {'hiring_manager_name': row['name'],
               'address': row['address'],
               'phone_number': row['phone_number'],
               'email': row['email'],
               'job_position': row['job'],
               'company_name': row['company']}

    context.update(my_context)

    # Render and save generated documents
    try:
        doc = DocxTemplate(docx_template_path)
        doc.render(context)
        doc.save(f"generated_doc_{index}.docx")
        print(f"Document {index} generated successfully.")
    except Exception as e:
        print(f"Error generating document for index {index}: {str(e)}")

print("Process completed.")
