import requests

class TestCalc:
    base_url = "http://127.0.0.1:5000"

    def test_add(self):
        response = requests.get(f"{self.base_url}/add/5&5")
        assert response.status_code == 200
        assert response.text == "Add 5 and 5. Got 10!"

    def test_subtract(self):
        response = requests.get(f"{self.base_url}/subtract/5&5")
        assert response.status_code == 200
        assert response.text == "Subtract 5 and 5. Got 0!"

    def test_multiply(self):
        response = requests.get(f"{self.base_url}/multiply/5&5")
        assert response.status_code == 200
        assert response.text == "Multiply 5 and 5. Got 25!"

    def test_divide(self):
        response = requests.get(f"{self.base_url}/divide/5&5")
        assert response.status_code == 200
        assert response.text == "Divide 5 and 5. Got 1!"
