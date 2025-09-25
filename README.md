# Currency Rate Scraper

A Django application for scraping and managing currency rates with REST API endpoints.

## Local Development

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your local settings
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Run the development server:
```bash
python manage.py runserver
```

## Railway Deployment

This project is configured for deployment on Railway with the following setup:

### Required Environment Variables

Set these in your Railway project settings:

- `SECRET_KEY`: A secure secret key for Django
- `DEBUG`: Set to `False` for production
- `ALLOWED_HOSTS`: Your Railway app domain (e.g., `your-app.railway.app`)
- `DB_ENGINE`: Database engine (default: `django.db.backends.mysql`)
- `DB_NAME`: Database name
- `DB_USER`: Database user
- `DB_PASSWORD`: Database password
- `DB_HOST`: Database host
- `DB_PORT`: Database port (default: 3306)

### Deployment Steps

1. Connect your GitHub repository to Railway
2. Railway will automatically detect the Python project
3. Set the required environment variables in Railway dashboard
4. Deploy - Railway will install dependencies and start the application

### Production Features

- Gunicorn WSGI server for production
- WhiteNoise for static file serving
- MySQL database support
- Environment-based configuration
- Security headers and settings
