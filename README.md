**RAG for SLR Review**

**Description:**
RAG_for_SLR-Review. is a Python script tailored for researchers and developers working in a Google Colaboratory environment who need to manage large sets of PDF documents and process them for further analysis. The script automates the setup of Google Drive within Colab, organizes directories for storing files, and handles the installation of essential Python packages for document processing, natural language processing, and vector storage using ChromaDB.

**Key Features**
•	Google Drive Integration: Simplifies access to Google Drive from within Google Colab, ensuring that all files are directly accessible for processing.
•	Directory Management: Automatically creates and manages directories for storing PDFs and vector data, facilitating organized data storage.
•	Automated Package Installation: Installs a set of predefined Python packages crucial for handling PDF documents, performing natural language processing, and managing vector data in a Chroma database.

**Installation:**
Prerequisites:
•	Access to Google Colaboratory.
•	A Google Drive account with sufficient storage space.

Setup Instructions:
1.	Clone the repository:
git clone https://github.com/yourusername/ RAG_for_SLR-Review.ipynb.git
2.	Open the script in Google Colab:
o	Upload RAG_for_SLR-Review.ipynb to your Google Colab session.
o	Run the script in a new notebook.

**Google Drive Authorization**
When running the script for the first time, Google Colab will request authorization to access your Google Drive. Follow the on-screen instructions to allow access, which is necessary for the script to function properly.

**Usage**
After setting up, you can execute the script by running:

!python RAG_for_SLR-Review.ipynb

This will mount your Google Drive, create necessary directories, and install all required packages automatically.

**Custom Configuration**
Modify the directory paths in the script to align with your specific Google Drive structure:
python
Copy code
pdf_folder_path = '/content/drive/MyDrive/output/pdf/'
vector_folder_path = '/content/drive/MyDrive/output/newvectorstores/'
Adjust these paths according to where you want your files stored within your Google Drive.

**Dependencies**
This script requires the installation of several Python packages which are listed in the script and include:
•	langchain
•	openai
•	PyMuPDF (for PDF processing)
•	chromadb (for managing vector data)
•	Additional dependencies for enhanced performance and compatibility.

**Authors**
•	Your Name – Sourabh Chaturvedi











