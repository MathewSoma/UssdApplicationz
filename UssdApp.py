from flask import Flask, request
import africastalking
import os

app = Flask(__name__)
username = "sandbox"
api_key = "57c6199d2c3b001ff8b1cf97d4a6f7aa80c5b0a93c28cf27a6ca6c84e0742017"
africastalking.initialize(username, api_key)
sms = africastalking.SMS

@app.route('/', methods=['POST', 'GET'])
def ussd_callback():
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")
    sms_phone_number = [phone_number]

    # USSD logic
    if text == '':
        # Main Menu
        response = "CON Welcome! Select an option\n\n"
        response += "1. Login\n"
        response += "2. Register as new VHT\n"

    elif text == '1':
        # Sub-Menu: Logging In
        response = "CON Enter your VHT ID"

    elif text.startswith('1*'):
        # Get the VhtID from the input
        VhtID = text.split("*")[1]

        # Validate the user name and email
        if len(VhtID) < 3:
            # Display an error message and ask the user to try again
            response = "CON Invalid VhtID\n"
            response += "Try Again\n"
        else:
            # Save the user data to the database
            # TODO: Add your database logic here

            # Display a success message and the menu options
            response = "CON Login successful\n"
            response += "1. Patient Management\n"
            response += "2. Case Reporting\n"
            response += "3. Submit Reports\n"
            response += "4. Seek Guidance"

    elif text == '1*1':  # Added this block for submenu 1*1
        # Sub-Menu: Patient Management
        response = "CON Manage patient records:\n\n"
        response += "1. Search by name\n"
        response += "2. Add new patient record\n"
        response += "3. Update patient record\n"
        response += "4. Delete patient record\n"
        response += "5. Back to main menu"

    elif text == '2':
        # Sub-Menu: Registration
        response = "CON Please enter details:\n\n"
        response += "1. Name\n"
        response += "2. Phone Number\n"
        response += "3. Location\n"
        response += "4. Complete registration"

    elif text == '4':
        # Sub-Menu: Case Reporting
        response = "CON Report case details:\n\n"
        response += "1. Malaria\n"
        response += "2. Diarrhea\n"
        response += "3. Pregnancy complications\n"
        response += "4. Other illnesses\n"
        response += "5. Back to main menu"

    elif text == '5':
        # Sub-Menu: Weekly Reports
        response = "CON Submit weekly reports:\n\n"
        response += "1. Malaria cases reported\n"
        response += "2. Diarrhea cases reported\n"
        response += "3. Pregnancy complications reported\n"
        response += "4. Total vaccinations administered\n"
        response += "5. Back to main menu"

    elif text == '6':
        # Terminal Response: Exiting App
        response = "END Thank you for using our services!"

    elif text == '0':
        # Go back to the previous menu
        response = "CON Returning to the previous menu..."

    else:
        # Unknown input
        response = "END Invalid choice."

    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ.get("PORT"))
