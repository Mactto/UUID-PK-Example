import uuid
from app.database import Base, engine, SessionLocal
from app.models import TextPkTable, UUIDPkTable


def generate_text_pk_data(num_records):
    return [
        TextPkTable(pk=str(uuid.uuid4()))
        for _ in range(num_records)
    ]

def generate_uuid_pk_data(num_records):
    return [
        UUIDPkTable(pk=uuid.uuid4())
        for _ in range(num_records)
    ]

def bulk_insert(session, model, data, batch_size=10000):
    for i in range(0, len(data), batch_size):
        session.bulk_save_objects(data[i:i + batch_size])
        session.commit()
        print(f"Inserted records {i} to {i + batch_size}")

# Create the tables
Base.metadata.create_all(bind=engine)

# Insert TextPkTable data
with SessionLocal() as session:
    text_data = generate_text_pk_data(10_000_000)
    bulk_insert(session, TextPkTable, text_data)

# Insert UUIDPkTable data
with SessionLocal() as session:
    uuid_data = generate_uuid_pk_data(10_000_000)
    bulk_insert(session, UUIDPkTable, uuid_data)
