from app import create_app
from app.controllers.user_controller import login_usuario
import traceback

app = create_app()

with app.app_context():
    print("Testing login...")
    try:
        data = {"email": "test@example.com", "senha": "test123"}
        result = login_usuario(data)
        print("Result:", result)
    except Exception as e:
        print("Error:", type(e), str(e))
        traceback.print_exc()
