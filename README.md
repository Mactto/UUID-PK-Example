# UUID를 Primary Key로 사용했을 때 발생할 수 있는 성능 이슈 소개


### Blog Post


### Environment
```
python 3.10.11
postgresql 15
```

### Setting Gudie

1. Create Vritual Environment
```
pyenv virtualenv 3.10.11 uuid-example
```

2. Install Requirements
```
pip install -r requirements.txt
```

3. Set Database
```
# after create your database

# database.py
fix url -> DATABASE_URL

# alembic.ini
fix url -> sqlalchemy.url
```

4. Insert Data
```
python -m script.insert_data
```
