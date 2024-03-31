from django.db import models
from cryptography.fernet import Fernet
from django.conf import settings


class Product(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    marja = models.DecimalField(max_digits=10, decimal_places=2)
    package_code = models.CharField(max_length=50)

    def encrypt_field(self, field_value):
        key = settings.AES_ENCRYPTION_KEY
        cipher_suite = Fernet(key)
        encrypted_value = cipher_suite.encrypt(field_value.encode('utf-8'))
        return encrypted_value.decode('utf-8')

    def get_encrypted_fields(self):
        encrypted_price = self.encrypt_field(str(self.price))
        encrypted_marja = self.encrypt_field(str(self.marja))
        encrypted_package_code = self.encrypt_field(self.package_code)
        return {
            'price': encrypted_price,
            'marja': encrypted_marja,
            'package_code': encrypted_package_code
        }
