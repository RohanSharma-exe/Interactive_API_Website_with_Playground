# 🚀 Interactive API Playground

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109.0-009688.svg)
![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-3.4.1-38B2AC.svg)

A powerful, modern, and beautiful web-based API testing tool built with **FastAPI** and **TailwindCSS**. Test your endpoints, manage authentication, and view responses in style—all without leaving your browser.

---

## ✨ Features

- **🎨 Modern UI**: Built with TailwindCSS for a clean, responsive, and premium feel.
- **🌙 Dark Mode**: Seamlessly switch between light and dark themes.
- **🛠️ Full Request Control**: Support for `GET`, `POST`, `PUT`, `DELETE`, and `PATCH`.
- **🔐 Authentication Support**: Dedicated tabs for **Bearer Token** and **Basic Auth**.
- **📜 Request History**: Automatically saves your recent requests to local storage for quick access.
- **⚡ Fast Proxy**: Built-in FastAPI proxy to handle CORS and facilitate secure requests.
- **🌈 Syntax Highlighting**: Beautiful JSON response formatting using `highlight.js`.

## 🛠️ Tech Stack

- **Backend**: Python, FastAPI, Uvicorn, HTTPX
- **Frontend**: Jinja2 Templates, HTML5, JavaScript
- **Styling**: TailwindCSS (via CDN), Custom Scrollbars
- **Testing**: Pytest

## 🚀 Getting Started

Follow these steps to get the project running on your local machine.

### Prerequisites

- Python 3.8 or higher
- working internet connection (for CDN assets)

### Installation

1.  **Clone the repository** (or download source):
    ```bash
    git clone https://github.com/yourusername/interactive-api-website.git
    cd Interactive_API_website
    ```

2.  **Create a virtual environment**:
    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

### Running the App

Start the development server with hot-reload enabled:

```bash
uvicorn app.main:app --reload
```

The application will be available at: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

## 🧪 Running Tests

Ensure your backend logic is working correctly by running the test suite:

```bash
python -m pytest
```

## 📂 Project Structure

```
Interactive_API_website/
├── app/
│   ├── main.py          # FastAPI application & Proxy logic
│   ├── templates/       # Jinja2 HTML templates
│   │   ├── base.html    # Base layout
│   │   └── index.html   # Main playground UI
│   └── static/          # Static assets (CSS)
├── tests/               # Pytest suites
├── requirements.txt     # Python dependencies
└── README.md            # You are here!
```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](#).

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).

---

<p align="center">
  Made with ❤️ using FastAPI
</p>
