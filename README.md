# S3Manager - Gallery Management with AWS S3

S3Manager is a powerful Python application designed to manage your image gallery using Amazon S3 for storage. It features database integration and thumbnail generation for efficient image organization and access.

## Features

- Image upload and management with AWS S3
- Local database for quick access and metadata storage
- Automatic thumbnail generation for optimized gallery browsing
- Flexible configuration options
- Utility functions for enhanced functionality

## Installation

Follow these steps to set up S3Manager on your local machine:

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/S3Manager.git
   cd S3Manager
   ```

2. Set up a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Configure the application:
   ```
   cp config.py.example config.py
   ```
   Edit `config.py` with your AWS credentials and other settings.

5. Initialize the database:
   ```
   python database.py
   ```

6. Run the application:
   ```
   python main.py
   ```

## Usage

After installation, use the `main.py` script to interact with S3Manager. This interface allows you to upload images, generate thumbnails, and manage your gallery.

For detailed usage instructions, refer to the documentation or comments within each module.

## Contributing

Contributions to S3Manager are welcome! Feel free to submit issues, fork the repository, and send pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

If you have any questions, please open an issue in the GitHub repository.

Happy gallery managing!