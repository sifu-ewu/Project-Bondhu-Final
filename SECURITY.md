# Security Guidelines for Project Bondhu

## 🚨 Immediate Actions Required

### 1. **REVOKE EXPOSED CREDENTIALS**
The following credentials were exposed in the Git repository and must be changed immediately:

- **Database Password**: `ashraful123` ❌ **CHANGE NOW**
- **Secret Key**: `v3v5vfsn0xxjtmb=eoawoiw$5br4g0r&jy_l39995h_93l+-z5` ❌ **CHANGE NOW**

### 2. **Generate New Credentials**

#### New Secret Key:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

#### New Database Password:
```bash
# Use a password generator or create a strong password manually
# Example: Use at least 16 characters with mixed case, numbers, and symbols
```

### 3. **Update Database Credentials**
```sql
-- Connect to PostgreSQL as admin
ALTER USER postgres PASSWORD 'your_new_very_strong_password_here';

-- Or create a new dedicated user
CREATE USER bondhu_app WITH PASSWORD 'your_new_very_strong_password_here';
GRANT ALL PRIVILEGES ON DATABASE predico2f TO bondhu_app;
```

## 🛡️ Security Checklist

### Environment Security
- [ ] `.env` file created with secure credentials
- [ ] `.env` added to `.gitignore`
- [ ] Old credentials revoked/changed
- [ ] `DEBUG=False` set for production
- [ ] `ALLOWED_HOSTS` configured for your domain
- [ ] Strong database password set
- [ ] Email app passwords configured

### Application Security
- [ ] Secret key regenerated
- [ ] Database user has minimal required permissions
- [ ] SSL/HTTPS enabled in production
- [ ] Security headers configured
- [ ] File upload restrictions in place
- [ ] User input validation enabled

### Deployment Security
- [ ] Server firewall configured
- [ ] Database not exposed to internet
- [ ] Regular security updates scheduled
- [ ] Monitoring and logging enabled
- [ ] Backup strategy implemented

## 🔒 Best Practices

### 1. **Credential Management**
```bash
# ✅ Good: Environment variables
export SECRET_KEY="your-secret-key"

# ❌ Bad: Hardcoded in source
SECRET_KEY = "hardcoded-secret"
```

### 2. **Database Security**
```python
# ✅ Good: Environment-based configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}

# ❌ Bad: Hardcoded credentials
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'predico2f',
        'USER': 'postgres',
        'PASSWORD': 'ashraful123',  # NEVER DO THIS
        'HOST': 'localhost'
    }
}
```

### 3. **Secret Key Generation**
```python
# ✅ Good: Generate unique keys
from django.core.management.utils import get_random_secret_key
SECRET_KEY = get_random_secret_key()

# ❌ Bad: Default or shared keys
SECRET_KEY = 'v3v5vfsn0xxjtmb=eoawoiw$5br4g0r&jy_l39995h_93l+-z5'
```

## 🚀 Secure Deployment Process

### 1. **Pre-deployment Security Check**
```bash
# Run security validation
python security_config.py

# Check for any remaining secrets in code
grep -r "password\|secret\|key" --exclude-dir=venv .
```

### 2. **Environment Setup**
```bash
# Create secure .env file
cp .env.example .env

# Edit with secure values
nano .env  # or your preferred editor

# Verify no secrets in git
git status
git log --oneline | head -5
```

### 3. **Database Setup**
```bash
# Create dedicated database user
createuser -P bondhu_app

# Create database with new user
createdb -O bondhu_app bondhu_production
```

### 4. **Web Server Configuration**
```nginx
# Nginx configuration with security headers
server {
    listen 443 ssl http2;
    server_name yourdomain.com;
    
    # Security headers
    add_header X-Frame-Options DENY;
    add_header X-Content-Type-Options nosniff;
    add_header X-XSS-Protection "1; mode=block";
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload";
    
    # SSL configuration
    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/private.key;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-RSA-AES256-GCM-SHA512:DHE-RSA-AES256-GCM-SHA512;
    
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

## 🔍 Security Monitoring

### Log Analysis
```bash
# Monitor failed login attempts
grep "Invalid password" logs/django.log

# Check for suspicious requests
grep "POST" logs/django.log | grep -E "(admin|login)"

# Monitor for injection attempts
grep -E "(SELECT|UNION|DROP|DELETE)" logs/django.log
```

### Regular Security Tasks
- [ ] Weekly password rotation for service accounts
- [ ] Monthly security updates
- [ ] Quarterly security assessments
- [ ] Annual penetration testing

## 📞 Incident Response

### If Credentials Are Compromised:
1. **Immediately** change all affected passwords
2. **Revoke** all API keys and tokens
3. **Regenerate** Django secret keys
4. **Review** access logs for unauthorized activity
5. **Update** all affected systems
6. **Document** the incident and lessons learned

### Contact Information:
- Security Team: security@bondhu.com
- Emergency: +1-XXX-XXX-XXXX
- Documentation: https://docs.bondhu.com/security

## 📚 Additional Resources

- [Django Security Documentation](https://docs.djangoproject.com/en/stable/topics/security/)
- [OWASP Web Application Security](https://owasp.org/www-project-top-ten/)
- [PostgreSQL Security](https://www.postgresql.org/docs/current/security.html)
- [Let's Encrypt SSL Certificates](https://letsencrypt.org/)

---

**Remember: Security is an ongoing process, not a one-time setup!**
