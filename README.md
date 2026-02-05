# AWS Cloud Flask Application

## Overview
A production-ready Python Flask web application deployed on AWS EC2 using Nginx as a reverse proxy and Gunicorn as the application server. The project follows cloud and DevOps best practices, including process management with systemd and secure GitHub integration using SSH.

## Tech Stack
- AWS EC2
- Python
- Flask
- Nginx
- Gunicorn
- Linux (Ubuntu)
- systemd
- Git & GitHub

## Architecture
Client → Nginx (Reverse Proxy) → Gunicorn → Flask Application

## Features
- Cloud deployment on AWS EC2
- Nginx reverse proxy configuration
- Production-grade Gunicorn setup
- systemd service for auto-start and reliability
- Secure SSH-based GitHub authentication

## How to Run Locally
```bash
python3 -m venv venv
source venv/bin/activate
pip install flask gunicorn
python app.py
