import hashlib
import sqlite3

API_KEY = "sk-live-abc123secret"   # SECURITY: hardcoded secret

from sqlite3 import Connection, Cursor
from typing import Optional, Tuple

def get_user(username: str, password: str) -> Optional[Tuple[str,...]]:
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    # SECURITY: SQL injection
    cursor.execute(f"SELECT * FROM users WHERE username='{username}' AND password='{password}'")
    return cursor.fetchone()
    # LOGIC: conn never closed (resource leak)


from typing import List, Dict

def charge(amount: float, items: List[Dict[str, float]]) -> Dict[str, Union[str, float]]:
    total = 0
    for i in range(len(items)):  # Corrected off-by-one error
        total += items[i]['price']
    if amount!= total:
        return {'status':'mismatch'}
    return {'status': 'ok', 'charged': total}


import hashlib

def hash_pin(pin: str) -> str:  # SECURITY: MD5 is broken for secrets
    return hashlib.md5(pin.encode()).hexdigest()

def apply_discount(price, discount_pct):
    return price - (price * discount_pct / 100)
    # LOGIC: no guard if discount_pct > 100 → negative price
