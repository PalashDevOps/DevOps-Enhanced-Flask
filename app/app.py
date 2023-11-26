from flask import Flask, render_template
import boto3
import pymysql

app = Flask(__name__)

# AWS S3 Configuration
s3 = boto3.client('s3')
s3_bucket_name = 'your-s3-bucket-name'

# AWS RDS Configuration
rds_host = 'your-rds-host'
db_name = 'your-db-name'
db_user = 'your-db-user'
db_password = 'your-db-password'
db_port = 3306

# Establish database connection
def create_db_connection():
    return pymysql.connect(rds_host, user=db_user, password=db_password, db=db_name, connect_timeout=5)

@app.route('/')
def hello():
    # Retrieve data from S3
    s3_response = s3.list_objects(Bucket=s3_bucket_name)
    s3_files = [obj['Key'] for obj in s3_response.get('Contents', [])]

    # Retrieve data from RDS
    try:
        connection = create_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM your_table;")
            rds_data = cursor.fetchall()
    finally:
        connection.close()

    return render_template('index.html', s3_files=s3_files, rds_data=rds_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
