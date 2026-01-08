from faker import Faker
import random
from db import get_connection

fake = Faker("fr_FR")
conn = get_connection()
cur = conn.cursor()

cur.execute("SELECT id FROM formations")
formations = [x[0] for x in cur.fetchall()]

for _ in range(13250):
    cur.execute("""
    INSERT INTO etudiants (nom, prenom, formation_id, promo)
    VALUES (%s,%s,%s,%s)
    """, (
        fake.last_name(),
        fake.first_name(),
        random.choice(formations),
        random.randint(2022,2025)
    ))

conn.commit()
cur.close()
conn.close()
