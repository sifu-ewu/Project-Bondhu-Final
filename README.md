# Project Bondhu - Healthcare Management System

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Django](https://img.shields.io/badge/Django-3.2+-green.svg)](https://djangoproject.com)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-12+-blue.svg)](https://postgresql.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A comprehensive healthcare management system built with Django that provides disease prediction, patient-doctor consultation, appointment booking, and community forum features.

## 🌟 Features

### 🏥 Core Healthcare Features
- **Disease Prediction**: AI-powered symptom analysis and disease prediction
- **Patient Management**: Complete patient profile and medical history
- **Doctor Dashboard**: Doctor profiles with specializations and ratings
- **Consultation System**: Real-time chat between patients and doctors
- **Appointment Booking**: Schedule and manage medical appointments
- **Prescription Management**: Digital prescription creation and management

### 👥 User Management
- **Multi-role Authentication**: Separate interfaces for patients, doctors, and admins
- **Profile Management**: Comprehensive user profiles with medical information
- **Rating & Review System**: Patient feedback for doctors

### 💬 Community Features
- **Healthcare Forum**: Community discussions on health topics
- **Blog Posts**: Share healthcare knowledge and experiences
- **Comments System**: Interactive discussions on posts

### 🔧 Technical Features
- **Responsive Design**: Mobile-friendly interface
- **Rich Text Editor**: CKEditor integration for content creation
- **Secure Authentication**: Django's built-in security features
- **Database Integration**: PostgreSQL for robust data management
- **Static File Management**: Optimized asset delivery

## 🛠️ Technology Stack

- **Backend**: Python 3.8+, Django 3.2+
- **Database**: PostgreSQL
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap
- **Machine Learning**: scikit-learn, NumPy, Pandas
- **Rich Text**: CKEditor
- **Authentication**: Django Auth System
- **Deployment**: Gunicorn, Whitenoise

## 📋 Prerequisites

Before running this project, make sure you have the following installed:

- Python 3.8 or higher
- PostgreSQL 12 or higher
- pip (Python package manager)
- Git

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/sifu-ewu/Project-Bondhu-Final.git
cd Project-Bondhu-Final
```

### 2. Create Virtual Environment
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Setup

#### PostgreSQL Configuration
1. Install PostgreSQL and create a database
2. Create a new database named `predico2f`
```sql
CREATE DATABASE predico2f;
CREATE USER postgres WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE predico2f TO postgres;
```

### 5. Environment Configuration
1. Copy the environment template:
```bash
cp .env.example .env
```

2. Edit `.env` file with your configuration:
```env
SECRET_KEY=your-super-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

DB_NAME=predico2f
DB_USER=postgres
DB_PASSWORD=your-database-password
DB_HOST=localhost
DB_PORT=5432
```

### 6. Database Migration
```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create Superuser
```bash
python manage.py createsuperuser
```

### 8. Collect Static Files
```bash
python manage.py collectstatic
```

### 9. Run Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to access the application.

## 🏗️ Project Structure

```
Project-Bondhu-Final/
├── accounts/              # User authentication and registration
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
├── main_app/              # Core application logic
│   ├── models.py         # Patient, Doctor, Disease models
│   ├── views.py          # Main views and disease prediction
│   ├── urls.py
│   └── ...
├── chats/                 # Real-time messaging system
│   ├── models.py         # Chat and Feedback models
│   ├── views.py
│   └── ...
├── projects/              # Forum and blog functionality
│   ├── models.py         # Post, Comment, Appointment models
│   ├── views.py
│   ├── forms.py
│   └── templates/
├── disease_prediction/    # Main project settings
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── templates/             # HTML templates
├── static/                # CSS, JS, Images
├── media/                 # User uploaded files
├── pics/                  # Profile pictures
├── trained_model          # ML model for disease prediction
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
└── README.md
```

## 👥 User Roles & Permissions

### 🏥 Admin
- Full system access
- User management
- System monitoring
- Access: `/admin/`

### 👨‍⚕️ Doctor
- View patient consultations
- Create prescriptions
- Manage appointments
- Access: `/doctor_ui/`

### 🧑‍🤝‍🧑 Patient
- Disease prediction
- Book appointments
- Chat with doctors
- Community participation
- Access: `/patient_ui/`

## 🔐 API Endpoints

### Authentication
- `POST /accounts/signup_patient/` - Patient registration
- `POST /accounts/signup_doctor/` - Doctor registration
- `POST /accounts/sign_in_patient/` - Patient login
- `POST /accounts/sign_in_doctor/` - Doctor login
- `POST /accounts/logout/` - Logout

### Main Features
- `GET /` - Homepage
- `GET /disease_predict/` - Disease prediction interface
- `GET /consultation_history/` - View consultations
- `POST /rate_doctor/<id>/` - Rate a doctor

### Forum & Community
- `GET /project/homeview/` - Forum homepage
- `POST /project/add_post/` - Create new post
- `GET /project/article/<id>/` - View post details
- `POST /project/appointment/` - Book appointment

## 🤖 Machine Learning Features

The system includes a trained machine learning model for disease prediction:

### Disease Prediction Workflow
1. **Symptom Input**: Users select symptoms from a predefined list
2. **ML Processing**: Symptoms are processed through the trained model
3. **Prediction**: System returns predicted disease with confidence score
4. **Doctor Recommendation**: Suggests relevant specialists
5. **Medical Record**: Saves prediction to patient's medical history

### Model Details
- **Type**: Classification model for disease prediction
- **Input**: Symptom vectors
- **Output**: Disease name and confidence percentage
- **Storage**: Serialized model in `trained_model` file

## 🔧 Configuration

### Environment Variables
| Variable | Description | Default |
|----------|-------------|---------|
| `SECRET_KEY` | Django secret key | Required |
| `DEBUG` | Debug mode | `True` |
| `ALLOWED_HOSTS` | Allowed hostnames | `localhost,127.0.0.1` |
| `DB_NAME` | Database name | `predico2f` |
| `DB_USER` | Database user | `postgres` |
| `DB_PASSWORD` | Database password | Required |
| `DB_HOST` | Database host | `localhost` |
| `DB_PORT` | Database port | `5432` |

### CKEditor Configuration
The system uses CKEditor for rich text editing in blog posts and descriptions.

## 🚀 Deployment

### Production Setup
1. Set `DEBUG=False` in environment variables
2. Configure proper `ALLOWED_HOSTS`
3. Set up SSL certificates
4. Use production database credentials
5. Configure email settings for notifications

### Using Gunicorn
```bash
gunicorn disease_prediction.wsgi:application --bind 0.0.0.0:8000
```

### Static Files in Production
```bash
python manage.py collectstatic --noinput
```

## 🧪 Testing

Run the test suite:
```bash
python manage.py test
```

Run specific app tests:
```bash
python manage.py test accounts
python manage.py test main_app
python manage.py test chats
python manage.py test projects
```

## 🐛 Troubleshooting

### Common Issues

#### Database Connection Error
```bash
# Check PostgreSQL service status
sudo systemctl status postgresql

# Restart PostgreSQL
sudo systemctl restart postgresql
```

#### Migration Issues
```bash
# Reset migrations (use with caution)
python manage.py migrate --fake-initial

# Or delete migration files and recreate
rm */migrations/0*.py
python manage.py makemigrations
python manage.py migrate
```

#### Static Files Not Loading
```bash
# Collect static files
python manage.py collectstatic --clear

# Check STATIC_URL and STATIC_ROOT settings
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guidelines
- Write comprehensive tests
- Update documentation for new features
- Use meaningful commit messages

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Authors

- **Main Developer** - *Initial work* - [sifu-ewu](https://github.com/sifu-ewu)

## 🙏 Acknowledgments

- Django community for the excellent framework
- Bootstrap for responsive design components
- CKEditor for rich text editing capabilities
- PostgreSQL for robust database management
- All contributors and testers

## 📞 Support

For support and questions:
- Create an issue on GitHub
- Contact the development team
- Check the documentation

## 🔮 Future Enhancements

- [ ] Mobile application development
- [ ] Telemedicine video consultations
- [ ] AI-powered health recommendations
- [ ] Integration with wearable devices
- [ ] Multi-language support
- [ ] Advanced analytics dashboard
- [ ] Pharmacy integration
- [ ] Insurance claim processing

---

**Note**: This is a healthcare management system. Please ensure compliance with local healthcare regulations and data protection laws when deploying in production environments.