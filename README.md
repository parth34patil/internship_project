# High Court Case Search Web App

This project is a Django-based web application that allows users to search for court cases by their case number. Since no public court API was available, a custom API was created with sample data to demonstrate the search functionality. The app also includes a captcha system to prevent automated/bot submissions.

---

## 🚀 Features

- Search for court cases by case number
- Custom API with sample case data (no external API required)
- Captcha verification to prevent bots
- Error messages for invalid case numbers or incorrect captcha

---

## 🛠 Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS
- **Database:** SQLite (default Django)

---

## 📦 How It Works

1. User visits the home page and is shown a captcha.
2. User enters a case number, year, and the captcha code.
3. The app checks the captcha and searches the custom API (database) for the case.
4. If found, case details are displayed. If not, an error message is shown and a new captcha is generated.

---

## 🧰 Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/parth34patil/internship_project.git
   cd internship_project/higcourt\ project
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```bash
   python manage.py migrate
   ```
4. Start the development server:
   ```bash
   python manage.py runserver
   ```
5. Open your browser and go to `http://127.0.0.1:8000/`

---

## 📄 Example

1. Enter a case number and year (e.g., `12345`, `2023`).
2. Enter the captcha code shown.
3. Click search to view case details or error messages.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📜 License

This project is licensed under the MIT License.
