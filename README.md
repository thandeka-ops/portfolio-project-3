cat > README.md <<'EOF'
# 🚀 Portfolio Project 3 — Production CI/CD & AWS Monitoring

A production-style Python Flask application demonstrating a complete DevOps workflow from source code to automated deployment, infrastructure monitoring, and alerting on AWS.

The project combines Docker, GitHub Actions, AWS EC2, GitHub OIDC, AWS Systems Manager, Nginx, Amazon CloudWatch, CloudWatch Agent, CloudWatch Alarms, and Amazon SNS.

---

## 🎯 Project Overview

This project demonstrates an automated DevOps pipeline where changes pushed to the `main` branch are:

1. Checked out by GitHub Actions
2. Tested with automated Pytest tests
3. Built into a Docker image
4. Published to Docker Hub
5. Deployed to an AWS EC2 server
6. Deployed securely using GitHub OIDC and AWS Systems Manager
7. Served through Nginx
8. Monitored using Amazon CloudWatch
9. Protected by CPU, memory, and disk alarms
10. Connected to Amazon SNS for email notifications
11. Verified automatically through live health and version checks

---

## 🏗️ Architecture

```text
                    ┌─────────────────────┐
                    │      Developer      │
                    │       Git Push      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │       GitHub        │
                    │      Repository     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   GitHub Actions    │
                    │                     │
                    │ • Pytest            │
                    │ • Docker Build      │
                    │ • Docker Push       │
                    │ • Deployment        │
                    └──────────┬──────────┘
                               │
                     GitHub OIDC Identity
                               │
                               ▼
                    ┌─────────────────────┐
                    │       AWS IAM       │
                    │   Deployment Role   │
                    └──────────┬──────────┘
                               │
                         AWS Systems
                         Manager (SSM)
                               │
                               ▼
              ┌────────────────────────────────┐
              │          AWS EC2               │
              │                                │
              │  ┌──────────────┐              │
Internet ────►│  │    Nginx     │              │
              │  │ Reverse Proxy│              │
              │  └──────┬───────┘              │
              │         │                      │
              │  ┌──────▼───────┐              │
              │  │ Docker Flask │              │
              │  │ Application  │              │
              │  └──────────────┘              │
              │                                │
              │     CloudWatch Agent            │
              └──────────────┬─────────────────┘
                             │
                             ▼
                    ┌─────────────────────┐
                    │   Amazon CloudWatch │
                    │                     │
                    │ • CPU               │
                    │ • Memory            │
                    │ • Disk              │
                    │ • Network           │
                    │ • EBS               │
                    └──────────┬──────────┘
                               │
                         CloudWatch
                           Alarms
                               │
                               ▼
                    ┌─────────────────────┐
                    │     Amazon SNS      │
                    │                     │
                    │   Email Alerts      │
                    └──────────┬──────────┘
                               │
                               ▼
                         📧 Outlook
