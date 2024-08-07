# Job Application Form Web App

This is a web application built using Python, HTML, and Flask. The app allows users to fill out a job application form and receive a confirmation email upon submission. The user's data is also stored in an SQL database.

## Features

- User-friendly job application form
- Fields: First Name, Last Name, Email, Start Date, Current Occupation
- Sends a congratulatory email to the user upon form submission
- Stores user data in an SQL database
- Displays a success message on the webpage after submission
- Uses Bootstrap for front-end styling

## Technologies Used

- **Python**
- **Flask**: Web framework
- **Flask-Mail**: Library for sending emails
- **SQLAlchemy**: ORM for database interactions
- **HTML/CSS**: Markup and styling
- **Bootstrap**: Front-end framework

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Mahdi-Meyghani/Job-Application-Form.git
    cd job-application-form
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. Set up your email configuration in the `app.py` file:
    ```python
   app.config["MAIL_SERVER"] = 'smtp.yourmailserver.com'
   app.config["MAIL_PORT"] = 465
   app.config["MAIL_USE_SSL"] = True
   app.config["MAIL_USERNAME"] = 'your-email@example.com'
   app.config["MAIL_PASSWORD"] = 'your-email-password'
    ```

2. Configure your database URI in the `app.py` file:
    ```python
    app.config["SECRET_KEY"] = "your-secret-key"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    ```

## Usage

1. Run the application:
    ```bash
    app.py -> run
    ```

2. Open your web browser and go to `http://127.0.0.1:5001/` to access the job application form.

## How It Works

1. The user fills out the job application form with their details.
2. Upon clicking the submit button, a POST request is sent.
3. The app sends a congratulatory email to the user using Flask-Mail.
4. The user's data is stored in an SQL database using SQLAlchemy.
5. A success message is displayed on the webpage.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Acknowledgements

- Flask
- Flask-Mail
- SQLAlchemy
- Bootstrap

