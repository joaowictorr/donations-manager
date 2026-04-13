import pytest
from src.donation import Donation
from datetime import date, timedelta

def test_valid_donation_creation():
    future_date = str(date.today() + timedelta(days=15))
    d = Donation("Rice", 10, future_date)
    assert d.item_name == "Rice"
    assert d.quantity == 10

def test_invalid_quantity():
    with pytest.raises(ValueError):
        Donation("Beans", 0, "2026-05-20")

def test_expiration_logic():
    near_date = str(date.today() + timedelta(days=3))
    d = Donation("Milk", 5, near_date)
    assert d.is_near_expiration()