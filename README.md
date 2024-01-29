**Document Generation Script from Template and CSV Data**

This Python script utilizes the `docxtpl` module to generate customized Word documents (`.docx`) from a predefined template and data provided in a CSV file. In the provided example, the script is set up to generate letters to different hiring managers by combining user-specific information with fictitious data from a CSV file.

### Prerequisites

Before running the script, make sure to install the following packages:

```bash
pip install pandas docxtpl
```

### Usage

1. **Run the Script:**
   - Execute the `document_generator.py` script.

2. **Inputs and Options:**
   - The script currently uses a predefined template (`template-manager-info.docx`) and a CSV file (`fake_data.csv`). You can customize these files or provide new ones.
   - Modify the user-specific information (`my_name`, `my_phone`, `my_email`, `my_address`) in the script or provide these details via user inputs.
   - Consider adding more options or interactivity for flexibility.

3. **Generated Documents:**
   - The script generates individualized documents for each row of data in the CSV file.
   - Output files are named in the format `generated_doc_{index}.docx`.

4. **Extend Functionality:**
   - Feel free to adapt the script for different templates, data sources, or document structures.
   - Enhance the script by adding command-line arguments or a user interface for more dynamic interactions.

### Customization

- **Template Modification:**
  - Adjust the `template-manager-info.docx` file to change the layout, formatting, or content of the generated documents.

- **CSV Data:**
  - Provide a CSV file with relevant data columns matching the placeholders in the template.

- **User Inputs:**
  - Enhance the script to accept user inputs for personalized information.

### Example Execution

```bash
python document_generator.py
```

### Notes

- Ensure that your environment has the required permissions to read and write files in the specified locations.
- For security reasons, consider storing sensitive information such as email passwords in a secure manner, like environment variables.

Feel free to explore and adapt this script based on your specific document generation needs!