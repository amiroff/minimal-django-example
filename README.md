# Minimal Django Example
This is a minimal `Hello World` example using [Django](https://www.djangoproject.com/), in my opinion, the most productive, intuitive and developer-friendly web framework. It cannot be used for serious purposes, example just shows how simple and minimal Django can be to start learning it.

## Setting up:

1. Download this repository, or if you have git installed, clone it
2. Install Python
3. Change into project directory: `cd minimal-django-example`
4. Create a virtual environment, and install django:
    ```shell
    python3 -m venv venv
    source venv/bin/activate
    pip install django
    ```
5. Run the development server: `python minimal.py runserver`
6. Navigate your browser to `http://127.0.0.1:8000/` to see basic example using `HttpResponse`
7. Navigate your browser to `http://127.0.0.1:8000/hello/World` to see basic basic example using template rendering.
