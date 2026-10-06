import psycopg2
# 1. add unicodedata, re, psycopg
# 2. create main function
# 3. create clean tag function
# 4. create ingestion function
# 5. select data from bronze, then insert to silver

def main():
    ingestion()

def ingestion(data):
    dsn = "dbname=bronze user=l1 password=l1admin host=localhost port=5001"
    conn = psycopg2.connect(dsn)

    cursor = conn.cursor()
    query = """insert into articles (urlhash, urls, title, content,tag, published_date) 
    values (%s, %s, %s, %s, %s, %s)"""

    cursor.execute(query, (
        data['urlhash'], data['url'], data['title'],
        data['content'], ", ".join(data['tag']), data['published_date']
    ))

    conn.commit()

def preprocessing(content):
    cleaned_text = []
    exclusion=[
        'Baca Juga:',
        'Lanjutkan Membaca:',
        'Langganan Sekarang',
        'Berlangganan untuk',
    ]

    for kalimat in content.split('.'):
        if not kalimat:
            continue

        if not any(
            word.lower() in kalimat.lower()
                for word in exclusion
        ):
            cleaned_text.append(kalimat.strip())
    return ".".join(cleaned_text)

if __name__ == '__main__':
    main()