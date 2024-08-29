# file: your_app/your_module/doctype/employee/employee.py
import frappe
from urllib.parse import urlencode

@frappe.whitelist()
def generate_pdf_url(doc_name):
    # Get the employee document
    si = frappe.get_doc("Sales Invoice", doc_name)
    
    # Define the base URL for the PDF download
    base_url = "/api/method/frappe.utils.print_format.download_pdf"
    
    # Create the query parameters
    query_params = {
        "doctype": "Sales Invoice",
        "name": si.name,
        "format": "Sales Invoice Print Format",  # Replace with your actual print format name
        "no_letterhead": 1,
        "letterhead": "No Letterhead",
        "settings": "{}",
        "_lang": "en"
    }
    
    # Encode the query parameters
    query_string = urlencode(query_params)
    
    # Construct the full URL
    full_url = f"{frappe.utils.get_url()}{base_url}?{query_string}"
    
    return full_url

    # Redirect the user to the full URL

    # frappe.local.response["type"] = "redirect"
    # frappe.local.response["location"] = full_url
