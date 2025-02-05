from notifications_python_client.notifications import NotificationsAPIClient
from dotenv import load_dotenv
import os

load_dotenv('../.env')  # Load variables from .env file

def get_templates():
    # notifications_client = NotificationsAPIClient(os.getenv('NOTIFY_API_KEY'))
    #
    # response = notifications_client.get_all_templates(
    #     template_type="sms / letter / email"  # optional string
    # )

    response = {
        "templates": [
            {
                "id": "f33517ff-2a88-4f6e-b855-c550268ce08a",  # required string - template ID
                "name": "Pigeon registration - appointment email",  # required string - template name
                "type": "sms / email / letter",  # required string
                "created_at": "2024-05-10 10:30:31.142535",  # required string - date and time template created
                "updated_at": "2024-08-25 13:00:09.123234",  # required string - date and time template last updated
                "version": 2,  # required integer - template version
                "created_by": "charlie.smith@pigeons.gov.uk",  # required string
                "subject": "Your upcoming pigeon registration appointment",
                # required string for email and letter - subject of email / heading of letter
                "body": "Dear ((first_name))\r\n\r\nYour pigeon registration appointment is scheduled for ((appointment_date)).\r\n\r\nPlease bring:\r\n\n\n((required_documents))\r\n\r\nYours,\r\nPigeon Affairs Bureau",
                # required string - body of notification
                "letter_contact_block": "Pigeons Affairs Bureau\n10 Whitechapel High Street\nLondon\nE1 8EF"
                # optional string - present for letter templates where contact block is set, otherwise None
            },
        ]
    }

if __name__ == "__main__":
    get_templates()
