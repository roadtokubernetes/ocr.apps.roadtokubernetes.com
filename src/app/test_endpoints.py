from fastapi.testclient import TestClient
from PIL import Image

from app.main import BASE_DIR, app
from app.settings import get_settings

TEST_IMAGE_DIR = BASE_DIR / "images"
client = TestClient(app)


def test_get_home():
    response = client.get("/")  # requests.get("") # python requests
    assert response.text != "<h1>Hello world</h1>"
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]


def test_invalid_file_upload_error():
    response = client.post("/")  # requests.post("") # python requests
    assert response.status_code == 422
    assert "application/json" in response.headers["content-type"]


def test_prediction_upload_missing_headers():
    for path in TEST_IMAGE_DIR.glob("*"):
        response = client.post("/", files={"file": open(path, "rb")})
        assert response.status_code == 401


def test_prediction_upload():
    settings = get_settings()
    valid_images = []
    invalid_images = []
    for path in TEST_IMAGE_DIR.glob("*"):
        try:
            img = Image.open(path)
        except:
            img = None
        if img is not None:
            valid_images.append(path)
        else:
            invalid_images.append(path)
    for path in valid_images:
        response = client.post(
            "/",
            files={"file": open(path, "rb")},
            headers={"Authorization": f"JWT {settings.secret_token}"},
        )
        assert response.status_code == 200
        data = response.json()
        assert len(data.keys()) == 2
    for path in invalid_images:
        response2 = client.post(
            "/",
            files={"file": open(path, "rb")},
            headers={"Authorization": f"JWT {settings.secret_token}"},
        )
        assert response2.status_code == 400
