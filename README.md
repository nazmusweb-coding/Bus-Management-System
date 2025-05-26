﻿# Bus Management System

A **Bus Management System** built using **Python** and the **Django** web framework. This backend-focused project implements full CRUD functionality with a structured database. The system allows users to book bus tickets, view invoices, check bus availability, and manage bookings, while admins have full control over bus data through the Django admin panel.

## Features

### User Features:

* **Signup / Login**: New users can register and log in to their accounts.
* **Book Tickets**: Book bus tickets by selecting destination, time, and available seats.
* **Invoice Generation**: View booking details and download invoices.
* **Availability Check**: Check bus availability for specific routes and times.
* **Cancel Booking**: Cancel existing bookings and see status in user dashboard.
* **Dashboard**: View current and past bookings, along with status.

### Admin Features:

* **Admin Panel**: Access Django's built-in admin interface.
* **Manage Buses**: Add, update, and delete bus details.
* **Monitor Bookings**: View all user bookings and statuses.

## Technologies Used

* **Backend**: Python, Django
* **Frontend**: HTML, CSS
* **Database**: SQLite (default), easily extendable to PostgreSQL or MySQL

## Installation

1. **Clone the repository**

```bash
https://github.com/nazmusweb.coding/bus-management-system.git
```

2. **Navigate to the project directory**

```bash
cd bus-management-system
```

3. **Create a virtual environment**

```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

4. **Install dependencies**

```bash
pip install -r requirements.txt
```

5. **Apply migrations**

```bash
python manage.py migrate
```

6. **Create a superuser**

```bash
python manage.py createsuperuser
```

7. **Run the development server**

```bash
python manage.py runserver
```

8. **Access the application**

* User Interface: `http://127.0.0.1:8000/`
* Admin Panel: `http://127.0.0.1:8000/admin/`

## Screenshots

*TBA*

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.
