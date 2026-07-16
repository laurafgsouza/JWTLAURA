from app import create_app
from app.extensions import db
from app.models.user import User
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    # Check if user already exists
    existing = User.query.filter_by(email="test@example.com").first()
    if not existing:
        test_user = User(
            nome="Test User",
            email="test@example.com",
            senha=generate_password_hash("test123"),
            admin=True
        )
        db.session.add(test_user)
        db.session.commit()
        print("Test user created successfully!")
        print("Email: test@example.com")
        print("Password: test123")
    else:
        print("Test user already exists!")
        print("Email: test@example.com")
        print("Password: test123")
