import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

class TestJSONPlaceholderAPI:
    
    def test_get_user(self):
        """Test GET request to retrieve user"""
        response = requests.get(f"{BASE_URL}/users/1")
        
        # Check status code
        assert response.status_code == 200
        
        # Check JSON structure
        user_data = response.json()
        expected_fields = ['id', 'name', 'username', 'email', 'address', 'phone', 'website', 'company']
        for field in expected_fields:
            assert field in user_data
        
        # Check field values
        assert user_data['id'] == 1
        assert user_data['name'] == "Leanne Graham"
        assert user_data['username'] == "Bret"
        assert user_data['email'] == "Sincere@april.biz"
        assert user_data['phone'] == "1-770-736-8031 x56442"
        assert user_data['website'] == "hildegard.org"
        
        # Check nested address structure
        assert 'street' in user_data['address']
        assert 'city' in user_data['address']
        assert 'zipcode' in user_data['address']
        assert 'geo' in user_data['address']
    
    def test_create_user(self):
        """Test POST request to create user"""
        new_user = {
            "name": "Test User",
            "username": "testuser",
            "email": "test@example.com",
            "phone": "1-234-567-8900",
            "website": "test.org"
        }
        
        response = requests.post(f"{BASE_URL}/users", json=new_user)
        
        # Check status code
        assert response.status_code == 201
        
        # Check JSON structure
        created_user = response.json()
        expected_fields = ['id', 'name', 'username', 'email', 'phone', 'website']
        for field in expected_fields:
            assert field in created_user
        
        # Check field values match request
        assert created_user['name'] == new_user['name']
        assert created_user['username'] == new_user['username']
        assert created_user['email'] == new_user['email']
        assert created_user['phone'] == new_user['phone']
        assert created_user['website'] == new_user['website']
        
        # Check ID was generated
        assert isinstance(created_user['id'], int)
        assert created_user['id'] >= 1
    
    def test_update_user(self):
        """Test PUT request to update user"""
        updated_user = {
            "id": 1,
            "name": "Updated User",
            "username": "updateduser",
            "email": "updated@example.com",
            "phone": "1-999-999-9999",
            "website": "updated.org"
        }
        
        response = requests.put(f"{BASE_URL}/users/1", json=updated_user)
        
        # Check status code
        assert response.status_code == 200
        
        # Check JSON structure
        user_data = response.json()
        expected_fields = ['id', 'name', 'username', 'email', 'phone', 'website']
        for field in expected_fields:
            assert field in user_data
        
        # Check data was updated
        assert user_data['id'] == updated_user['id']
        assert user_data['name'] == updated_user['name']
        assert user_data['username'] == updated_user['username']
        assert user_data['email'] == updated_user['email']
        assert user_data['phone'] == updated_user['phone']
        assert user_data['website'] == updated_user['website']

if __name__ == "__main__":
    # Run tests
    pytest.main([__file__, "-v"])