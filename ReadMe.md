# Face Authentication
I have developed a face recognising system in python using DeepFace, FastAPI. 

You can use it for authenticating applications, web pages and other fields where face recognition is needed.

## Installation

You can easly getstarted by cloning project and running server

```bash
git clone https://github.com/ijas0805/face-authentication.git
```
```bash
cd face-authentication
```
Activate your venv and run 
```bash
pip install -r requirements.txt
```
Start server by 
```bash
python3 server.py
```

## Usage 

## To register a user
- Select Add User POST
- Select on Try it out
- Enter password (DM me for password)
- Enter a new username(Remember your username)
- Upload image
- Click on Execute (I am using free server from AWS. So it will take some time to add new user)
- Check on Response body below for replay from server
## To verify a user
- Select on Verify User POST
- Select Try it out
- Enter password
- Enter User name (Please verify that user name match the username you created. It is case sensitive)
- Upload User image
- Click Execute
- You will get a 'User verified' message on Response body if the user name and image match