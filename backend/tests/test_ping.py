from app.configs.config import Settings


def test_app():
    setting = Settings()
    assert setting.testing == 1
