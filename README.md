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

##  API Endpoints

<!-- GET /classes/ -->
Returns all upcoming fitness classes.

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

// `POST /book/`

{
  "class_id": 1,
  "client_name": "Aparna",
  "client_email": "aparna@gmail.com"
}


// ✅ GET /bookings/?email=your_email@example.com

Returns all bookings made by the given email.