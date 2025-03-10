# RMHS Dashboard (Raw Material Handling System Dashboard)

A comprehensive dashboard application to record, track, and visualize daily operation, maintenance, delay, and rake handling activities for Raw Material Handling System (RMHS).

## Features

- Data entry through simple forms by shift engineers and maintenance engineers
- Data visualization through charts and clearly formatted text blocks
- Tracking of operations across different areas
- Delay reporting and analysis
- Rake completion tracking
- Maintenance activity logging

## Technology Stack

- **Backend**: Django
- **Frontend**: JavaScript, Bootstrap, HTML, CSS

## Project Structure

The project is organized into several Django apps:

- **operations**: Handles Area-1, Area-2, and Area-3 operational activities
- **delays**: Manages delay reports (Mechanical, Electrical, Operational)
- **rakes**: Tracks rake completion reports
- **maintenance**: Records general maintenance activities

## Setup Instructions

1. Clone this repository
2. Create a virtual environment:
   ```
   python -m venv venv
   ```
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Run migrations:
   ```
   python manage.py migrate
   ```
6. Create a superuser:
   ```
   python manage.py createsuperuser
   ```
7. Run the development server:
   ```
   python manage.py runserver
   ```

## User Roles

- **Operation Shift Engineers**: Record operation activities & rakes completed
- **Shift In-charges (Electrical/Mechanical/Operational)**: Submit delay reports
- **General Maintenance Engineers**: Enter maintenance data

## Shift Timings

- **Operation Shifts**:
  - Shift A: 6:00 AM - 2:00 PM
  - Shift B: 2:00 PM - 10:00 PM
  - Shift C: 10:00 PM - 6:00 AM
- **General Shift (Maintenance)**: 9:00 AM to 6:30 PM 