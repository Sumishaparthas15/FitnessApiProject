#  Fitness Class Booking API

This is a Django REST Framework backend project for booking fitness classes like Yoga, Zumba, and HIIT.  
It allows users to view available classes, book a class, and view their bookings using their email.

---

##  Technologies Used

- Python 3.x
- Django
- Django REST Framework
- SQLite (default DB)
- Postman for API testing

---

 <!-- Setup Instructions -->

```bash
# Clone the repository
git clone https://github.com/Sumishaparthas15/FitnessApiProject.git
cd fitness_api_project

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate 


python manage.py migrate
python manage.py runserver


##  API Endpoints

### 1. GET All Fitness Classes

`GET /classes/ `
Returns all upcoming fitness classes.

Sample cURL
curl -X GET http://127.0.0.1:8000/classes/

**Example response:**
```json
[
  {
    "id": 1,
    "name": "Yoga",
    "instructor": "Amit",
    "datetime": "2025-07-10T10:00:00Z",
    "available_slots": 8
  }
]
### 2. Book a Class
Body: JSON

---> Sample cURL
curl -X POST http://127.0.0.1:8000/book/ \
  -H "Content-Type: application/json" \
  -d '{"class_id": 1, "client_name": "Aparna", "client_email": "aparna@gmail.com"}'

---> Sample Postman
Method: POST

URL: http://127.0.0.1:8000/book/

Headers:
Content-Type: application/json

Body (raw JSON):
json

{
  "class_id": 1,
  "client_name": "Aparna",
  "client_email": "aparna@gmail.com"
}

---> Example Success Response
json

{
  "id": 5,
  "fitness_class": "Yoga",
  "client_name": "Aparna",
  "client_email": "aparna@gmail.com",
  "booked_at": "2025-07-09T12:30:00Z"
}
---> Example Error Response
json

{
  "error": "No available slots"
}


3.  Get Bookings by Email
URL: /bookings/?email=aparna@gmail.com
Method: GET

---> Sample cURL

curl -X GET "http://127.0.0.1:8000/bookings/?email=aparna@gmail.com"
//  GET /bookings/?email=your_email@example.com


---> Sample Postman
Method: GET

URL: http://127.0.0.1:8000/bookings/?email=aparna@gmail.com

📤 Example Response
json

[
  {
    "id": 5,
    "fitness_class": "Yoga",
    "client_name": "Aparna",
    "client_email": "aparna@gmail.com",
    "booked_at": "2025-07-09T12:30:00Z"
  }
]

Project Structure

fitness_api_project/
├── booking/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
├── fitness_api_project/
│   ├── settings.py
├── db.sqlite3
├── manage.py
└── README.md