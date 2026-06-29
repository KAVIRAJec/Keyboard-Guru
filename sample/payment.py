import sqlite3


   # SECURITY: hardcoded secret

from sqlite3 import Connection, Cursor
from typing import Optional, Tuple

def get_user(username: str, password: str) -> Optional[Tuple[str,...]]:
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    return cursor.fetchone()



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

def apply_discount(price: float, discount_pct: float) -> float:  # LOGIC: no guard if discount_pct > 100 → negative price
    return price - (price * discount_pct / 100)

