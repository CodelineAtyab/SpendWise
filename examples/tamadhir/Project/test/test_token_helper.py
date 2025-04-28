import unittest
import sys
import os
import jwt

from unittest.mock import patch
from datetime import datetime, timedelta

from app_utils.token_helper import generate_token, validate_token


class TestTokenHelper(unittest.TestCase):
    def setUp(self):
        self.test_username = "testuser"
        self.secret_key = "your_secret_key"
        self.algorithm = "HS256"

    def test_generate_token_success(self):
        """Test successful token generation"""
        token = generate_token(self.test_username)
        # Verify token is a non-empty string
        self.assertIsInstance(token, str)
        self.assertTrue(len(token) > 0)
        
        # Decode and verify token contents
        decoded = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
        self.assertEqual(decoded['sub'], self.test_username)
        self.assertTrue('exp' in decoded)

    def test_validate_token_success(self):
        """Test successful token validation"""
        token = generate_token(self.test_username)
        self.assertTrue(validate_token(token))

    def test_validate_token_expired(self):
        """Test validation of expired token"""
        # Create an expired token
        expired_payload = {
            "sub": self.test_username,
            "exp": datetime.utcnow() - timedelta(hours=1)
        }
        expired_token = jwt.encode(expired_payload, self.secret_key, algorithm=self.algorithm)
        self.assertFalse(validate_token(expired_token))

    def test_validate_token_invalid(self):
        """Test validation of invalid token"""
        invalid_token = "invalid.token.string"
        self.assertFalse(validate_token(invalid_token))

    def test_validate_token_modified(self):
        """Test validation of tampered token"""
        token = generate_token(self.test_username)
        modified_token = token + "tampered"
        self.assertFalse(validate_token(modified_token))

if __name__ == '__main__':
    unittest.main()