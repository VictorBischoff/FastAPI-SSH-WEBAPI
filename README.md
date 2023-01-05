# FastAPI-SSH-WEBAPI
<center><img src="logo-api.png"></center>


# Introduction
This API utilizes the paramiko library to establish an SSH connection with the remote server and facilitate secure communication. The Ed25519Key module of paramiko is used to handle the generation and management of the SSH key pairs. FastAPI is utilized to build the API and provide an interface for interacting with the remote server through the swagger documentation. The API allows the user to copy their SSH key to the remote server, enabling them to authenticate and execute commands with the privileges of their account. Additionally, the API allows for the execution of commands with sudo privileges by passing in the password for the remote user.
