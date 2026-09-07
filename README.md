# 🚀 Portfolio Project 3 — Production CI/CD & AWS Monitoring

A production-style Python Flask application demonstrating a complete DevOps workflow from source code to automated deployment, infrastructure monitoring, HTTPS, and alerting on AWS.

The project combines Docker, GitHub Actions, AWS EC2, GitHub OIDC, AWS Systems Manager, Nginx, Cloudflare, Amazon CloudWatch, CloudWatch Agent, CloudWatch Alarms, and Amazon SNS.

---

## 🎯 Project Overview

This project demonstrates an automated DevOps pipeline where changes pushed to the `main` branch are:

1. Checked out by GitHub Actions
2. Tested with automated Pytest tests
3. Built into a Docker image
4. Published to Docker Hub
5. Deployed securely to AWS EC2
6. Deployed using GitHub OIDC and AWS Systems Manager
7. Served through Nginx
8. Protected with HTTPS and Cloudflare
9. Monitored using Amazon CloudWatch
10. Protected by CPU, memory, and disk alarms
11. Connected to Amazon SNS for email notifications
12. Verified automatically through live health and version checks

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
                    │ • Live Verification │
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
              │            AWS EC2             │
              │                                │
              │  ┌──────────────┐              │
Internet ────►│  │    Nginx     │              │
              │  │ Reverse Proxy│              │
              │  │    HTTPS     │              │
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
