## Installation

Create a virtual environment and install the requirements

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running the server
Inside the virtual environment
```bash
fastapi dev main.py
```

## Running the tests
Inside the virtual environment
```bash
pytest
```

If there are permission issues, run the following command
```bash
chmod +x test 
```