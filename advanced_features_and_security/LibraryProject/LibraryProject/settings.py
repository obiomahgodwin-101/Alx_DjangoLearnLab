# SECURITY SETTINGS FOR HTTPS AND SECURE COOKIES

# Redirect all HTTP requests to HTTPS
SECURE_SSL_REDIRECT = True  # Ensures all requests are served via HTTPS

# HTTP Strict Transport Security (HSTS)
SECURE_HSTS_SECONDS = 31536000  # 1 year in seconds
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Apply HSTS to all subdomains
SECURE_HSTS_PRELOAD = True  # Allow domain to be preloaded in browsers

# Secure cookies
SESSION_COOKIE_SECURE = True  # Only send session cookies over HTTPS
CSRF_COOKIE_SECURE = True     # Only send CSRF cookies over HTTPS

# Additional security headers
X_FRAME_OPTIONS = "DENY"             # Prevent clickjacking
SECURE_CONTENT_TYPE_NOSNIFF = True   # Prevent MIME-type sniffing
SECURE_BROWSER_XSS_FILTER = True     # Enable browser XSS filtering

# DEBUG should be False in production
DEBUG = False

# Existing settings (don't remove)
STATIC_URL = '/static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'bookshelf.CustomUser'

