# 🕌 Ghumariya School (المدرسة الغمارية لإحياء العلوم)

A Django-based educational platform dedicated to reviving Islamic sciences, featuring a modern, premium "Black & Gold" design and full internationalization support.

## 🌟 Features

*   **Global Expansion (i18n):** Full support for **Arabic (AR)**, **English (EN)**, and **French (FR)**.
*   **Dynamic Content:**
    *   **Branches:** Manage international branches (Palestine, Tunisia, France) with geolocation details.
    *   **Book Library:** Upload and manage books with cover images and authors.
    *   **Lessons:** Video lesson management linked to scholars and branches.
    *   **Scholars:** Profiles for scholars and teachers.
*   **Premium UI/UX:**
    *   Custom "Black & Gold" aesthetic using **Tailwind CSS**.
    *   Responsive design with animations and glassmorphism effects.
    *   Dynamic "About School" page editable from the admin panel.
*   **Admin Panel:** customized Django admin for easy content management.

## 🛠 Tech Stack

*   **Backend:** Python, Django 5.x
*   **Frontend:** HTML5, Tailwind CSS
*   **Database:** SQLite (Development) / PostgreSQL (Production ready)
*   **Internationalization:** Django i18n

## 🚀 Getting Started

### Prerequisites

*   Python 3.10+
*   Git

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Khalil96N/GhumariyaSchool.git
    cd GhumariyaSchool
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

7.  Visit `http://127.0.0.1:8000` in your browser.

## 📸 Screenshots

*(Add your screenshots here)*

## 📄 License

This project is licensed under the MIT License.
