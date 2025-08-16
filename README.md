### Installation

Step-by-step guide on how to Activity-1-Midterms  

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/polynexe/Quiz03.git
    cd Quiz03
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Database setup (for Django):**
    ```bash
    python manage.py migrate
    ```

[//]: # (5.  **Create a superuser &#40;optional, for admin access&#41;:**)

[//]: # (    ```bash)

[//]: # (    python manage.py createsuperuser)

[//]: # (    ```)

### Running the Project

How to start your Django development server.

```bash
python manage.py runserver