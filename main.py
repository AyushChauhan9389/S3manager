import streamlit as st
import boto3
import sqlite3
import os
from database import init_db, get_items, add_item
from s3_operations import list_s3_objects, get_s3_object_url, upload_file_to_s3
from config import S3_BUCKET_NAME, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION
from utils import get_or_create_thumbnail
import io

# Initialize the database
init_db()

# Set up S3 client with explicit credentials
s3 = boto3.client('s3',
                  aws_access_key_id=AWS_ACCESS_KEY_ID,
                  aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                  region_name=AWS_REGION)

# Create thumbnails directory if it doesn't exist
THUMBNAILS_DIR = os.path.join(os.path.dirname(__file__), 'thumbnails')
os.makedirs(THUMBNAILS_DIR, exist_ok=True)

st.title('S3 Gallery App')

# Upload functionality
uploaded_file = st.file_uploader("Choose a file to upload", type=['png', 'jpg', 'jpeg', 'gif', 'pdf', 'txt'])
if uploaded_file is not None:
    if st.button('Upload to S3'):
        file_content = uploaded_file.read()
        upload_file_to_s3(s3, S3_BUCKET_NAME, uploaded_file.name, io.BytesIO(file_content))
        st.success(f"File {uploaded_file.name} uploaded successfully!")

# Refresh S3 items
if st.button('Refresh Items'):
    s3_items = list_s3_objects(s3, S3_BUCKET_NAME)
    for item in s3_items:
        add_item(item['Key'], item['LastModified'].strftime("%Y-%m-%d %H:%M:%S"), item['Size'])

# Fetch items from the local database
items = get_items()

# Display items in a list
for item in items:
    col1, col2, col3 = st.columns([1, 3, 1])
    with col1:
        thumbnail_path = get_or_create_thumbnail(item[1], THUMBNAILS_DIR)
        st.image(thumbnail_path, width=100)
    with col2:
        st.write(f"**{item[1]}**")
        st.write(f"Last Modified: {item[2]}")
        st.write(f"Size: {item[3]} bytes")
    with col3:
        if st.button('View', key=f"view_{item[0]}"):
            st.session_state.selected_item = item

# Display modal with item details
if 'selected_item' in st.session_state:
    item = st.session_state.selected_item
    with st.expander(f"Details for {item[1]}", expanded=True):
        thumbnail_path = get_or_create_thumbnail(item[1], THUMBNAILS_DIR)
        st.image(thumbnail_path, use_column_width=True)
        st.write(f"Filename: {item[1]}")
        st.write(f"Last Modified: {item[2]}")
        st.write(f"Size: {item[3]} bytes")
        download_url = get_s3_object_url(s3, S3_BUCKET_NAME, item[1])
        st.text_input("Download Link (Click to copy)", value=download_url)
        if st.button("Close"):
            del st.session_state.selected_item