#  Project 3 — Production CI/CD & AWS Monitoring

A production-style Python Flask application demonstrating a complete DevOps workflow from source code to automated testing, Docker image publishing, AWS deployment, HTTPS verification, monitoring, and alerting.

The project demonstrates how a code change can move through an automated CI/CD pipeline and reach a live AWS environment with deployment verification.

---

##  Project Overview

This project demonstrates a production-oriented DevOps workflow where changes pushed to the `main` branch are:

1. Checked out by GitHub Actions
2. Tested with automated Pytest tests
3. Built into a Docker image
4. Published to Docker Hub
5. Authenticated to AWS using GitHub OIDC
6. Deployed to AWS EC2
7. Deployed through AWS Systems Manager
8. Served through Nginx
9. Protected with HTTPS and Cloudflare
10. Monitored using Amazon CloudWatch
11. Protected with CloudWatch alarms
12. Connected to Amazon SNS for notifications
13. Verified through live HTTPS health and version checks

---

## 🏗️ Architecture

```text
Developer
    |
    | git push
    v
GitHub Repository
    |
    v
GitHub Actions
    |
    +----------------------+
    |                      |
    v                      v
Pytest Tests          Docker Build
                           |
                           v
                      Docker Hub
                           |
                           v
                    GitHub OIDC
                           |
                           v
                       AWS IAM
                           |
                           v
                  AWS Systems Manager
                           |
                           v
                       AWS EC2
                           |
                           v
                        Nginx
                           |
                           v
                   Docker Flask App
                           |
             +-------------+-------------+
             |                           |
             v                           v
        HTTPS / Cloudflare        CloudWatch Agent
                                         |
                                         v
                                  Amazon CloudWatch
                                         |
                              +----------+----------+
                              |                     |
                              v                     v
                       CloudWatch Alarms      Monitoring
                              |
                              v
                          Amazon SNS
                              |
                              v
                       Email Notifications
```

---

## 🧰 Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.12 | Application runtime |
| Flask | Web application |
| Pytest | Automated testing |
| Docker | Application containerization |
| Docker Hub | Container image registry |
| Git | Version control |
| GitHub | Source code repository |
| GitHub Actions | CI/CD automation |
| GitHub OIDC | Keyless AWS authentication |
| AWS IAM | Deployment authorization |
| AWS EC2 | Application hosting |
| AWS Systems Manager | Remote deployment |
| Nginx | Reverse proxy |
| Cloudflare | DNS and HTTPS |
| Amazon CloudWatch | Monitoring |
| CloudWatch Agent | System metrics |
| CloudWatch Alarms | Alerting |
| Amazon SNS | Email notifications |
| YAML | CI/CD configuration |

---

## 📁 Project Structure

```text
portfolio-project-3/
|
+-- .github/
|   +-- workflows/
|       +-- ci.yml
|
+-- app/
|   +-- __init__.py
|   +-- app.py
|   +-- requirements.txt
|   +-- test_app.py
|
+-- .dockerignore
+-- .gitignore
+-- Dockerfile
+-- README.md
```

---

## 🐍 Flask Application

The application is built with Flask.

The current application version is:

```text
3.0.5
```

### Home Endpoint

```text
GET /
```

Returns application information including the application name, status, and version.

Example:

```json
{
  "application": "CI/CD Demo Application",
  "status": "running",
  "version": "3.0.5"
}
```

### Health Endpoint

```text
GET /health
```

Returns:

```json
{
  "status": "healthy"
}
```

### Version Endpoint

```text
GET /version
```

Returns:

```json
{
  "version": "3.0.5"
}
```

---

## 🧪 Automated Testing

The application includes automated tests using Pytest.

The tests verify:

- Home endpoint availability
- Application name
- Application version
- Health endpoint
- Health status
- Version endpoint
- Version value

Run the tests locally with:

```bash
pytest
```

The GitHub Actions pipeline also runs the tests before the Docker image is built and published. :contentReference[oaicite:2]{index=2}

---

## 🔄 CI/CD Pipeline

The GitHub Actions workflow is located at:

```text
.github/workflows/ci.yml
```

The workflow runs when changes are pushed to `main` or when a pull request targets `main`. :contentReference[oaicite:3]{index=3}

### Pipeline Flow

```text
Git Push
   |
   v
Checkout
   |
   v
Set up Python
   |
   v
Install Dependencies
   |
   v
Run Pytest
   |
   v
Determine Application Version
   |
   v
Docker Login
   |
   v
Build Docker Image
   |
   v
Push Versioned Image
   |
   v
Push Latest Image
   |
   v
Authenticate to AWS
   |
   v
Deploy to EC2
   |
   v
Health Check
   |
   v
Verify HTTPS Deployment
   |
   v
Verify Live Version
```

---

## 🐳 Docker

The project packages the Flask application into a Docker image.

The CI/CD pipeline creates two Docker tags:

```text
tholiwe/portfolio-project-3:<version>
tholiwe/portfolio-project-3:latest
```

The version is extracted automatically from `app/app.py` during the pipeline. :contentReference[oaicite:4]{index=4}

The pipeline then publishes both the versioned image and the `latest` image to Docker Hub. :contentReference[oaicite:5]{index=5}

---

## ☁️ AWS Deployment

The application is deployed to an AWS EC2 instance.

The deployment pipeline uses:

- AWS IAM
- GitHub OIDC
- AWS Systems Manager
- EC2
- Docker

The workflow configures AWS credentials using an IAM role assumed through GitHub OIDC. :contentReference[oaicite:6]{index=6}

This avoids storing long-lived AWS access keys directly in the GitHub Actions workflow.

---

## 🔐 GitHub OIDC

GitHub Actions uses OpenID Connect to authenticate with AWS.

The workflow requests an OIDC identity token and configures AWS credentials using:

```yaml
role-to-assume: ${{ secrets.AWS_ROLE_ARN }}
```

The workflow also includes diagnostic output for the OIDC claims used by AWS trust configuration. :contentReference[oaicite:7]{index=7}

This demonstrates keyless cloud authentication between GitHub Actions and AWS.

---

## 🛠️ AWS Systems Manager Deployment

The deployment is sent to EC2 through AWS Systems Manager.

The workflow:

1. Creates the deployment script
2. Encodes the script
3. Sends it through SSM
4. Waits for the SSM command to complete
5. Checks the deployment result
6. Displays deployment output

The deployment command uses the AWS `AWS-RunShellScript` document. :contentReference[oaicite:8]{index=8}

---

## 🔁 Deployment and Rollback

The deployment script records the previous Docker image before replacing the running container.

The new container is started and tested using:

```text
/health
```

If the health check succeeds:

```text
DEPLOYMENT SUCCESSFUL
```

If the health check fails, the deployment stops the new container and attempts to restore the previous image. :contentReference[oaicite:9]{index=9}

This provides a basic automated rollback mechanism.

---

## 🌐 HTTPS Deployment Verification

After deployment, the CI/CD pipeline verifies the live application through HTTPS.

The pipeline checks:

```text
https://tholiwe.co.za/health
```

and:

```text
https://tholiwe.co.za/version
```

The health endpoint must return a healthy status.

The live version must also match the version produced by the CI/CD pipeline. :contentReference[oaicite:10]{index=10}

This provides automated end-to-end deployment verification.

---

## 🌍 Nginx and Cloudflare

The deployed application is served through Nginx and exposed through HTTPS.

Cloudflare is used as part of the public HTTPS deployment.

The architecture therefore separates:

```text
Internet
    |
    v
Cloudflare
    |
    v
Nginx
    |
    v
Docker Flask Application
```

---

## 📊 AWS Monitoring

The project includes AWS monitoring using Amazon CloudWatch.

The monitoring architecture includes:

- CloudWatch Agent
- CPU metrics
- Memory metrics
- Disk metrics
- Network metrics
- CloudWatch Alarms
- Amazon SNS

The goal is to monitor both the application environment and the underlying EC2 infrastructure.

---

## 🚨 Alerting

CloudWatch alarms are used to detect infrastructure conditions such as resource usage thresholds.

Amazon SNS is connected to the alerting workflow to provide email notifications.

The overall flow is:

```text
EC2 Metrics
    |
    v
CloudWatch
    |
    v
CloudWatch Alarm
    |
    v
Amazon SNS
    |
    v
Email Notification
```

---

## 🔒 Security

Security practices demonstrated in this project include:

- GitHub OIDC authentication for AWS
- IAM role-based AWS access
- GitHub encrypted secrets
- No long-lived AWS access keys in the workflow
- Environment-based configuration
- HTTPS
- Cloudflare
- Nginx reverse proxy
- Automated deployment verification
- Health checks before deployment completion

Secrets such as:

```text
DOCKERHUB_USERNAME
DOCKERHUB_TOKEN
AWS_ROLE_ARN
```

are supplied through GitHub Actions secrets rather than being hard-coded into the workflow. :contentReference[oaicite:11]{index=11} :contentReference[oaicite:12]{index=12}

---

## ✅ Verification

The project verifies the deployment at multiple stages.

### Application Tests

Pytest verifies the Flask endpoints and expected application values.

### Docker Build

The CI/CD pipeline builds the Docker image automatically.

### Docker Publishing

The pipeline publishes versioned and latest images.

### AWS Authentication

GitHub Actions verifies the AWS identity using:

```bash
aws sts get-caller-identity
```

### Deployment

AWS Systems Manager reports the deployment status.

### Health Check

The deployment script checks:

```text
http://localhost:5000/health
```

### Live HTTPS Check

The pipeline verifies:

```text
https://tholiwe.co.za/health
```

### Version Verification

The pipeline compares the expected application version with the live version.

A mismatch causes the pipeline to fail. :contentReference[oaicite:13]{index=13}

---

## 💡 DevOps Skills Demonstrated

This project demonstrates practical experience with:

- Python
- Flask
- Pytest
- Docker
- Docker Hub
- Git
- GitHub
- GitHub Actions
- CI/CD
- AWS EC2
- AWS IAM
- GitHub OIDC
- AWS Systems Manager
- Nginx
- Cloudflare
- HTTPS
- Amazon CloudWatch
- CloudWatch Agent
- CloudWatch Alarms
- Amazon SNS
- Automated health checks
- Automated deployment verification
- Docker image versioning
- Deployment rollback
- Cloud security practices
- Infrastructure monitoring
- Production-style deployment workflows

---

## 📚 What I Learned

Through this project I practiced:

- Building a CI/CD pipeline from source code to deployment
- Running automated tests in GitHub Actions
- Building and publishing Docker images
- Using application versions as Docker image tags
- Connecting GitHub Actions securely to AWS
- Using GitHub OIDC with AWS IAM
- Deploying to EC2 through AWS Systems Manager
- Performing automated health checks
- Implementing deployment rollback
- Serving applications through Nginx
- Working with HTTPS and Cloudflare
- Monitoring AWS infrastructure
- Configuring CloudWatch alarms
- Connecting alerts to SNS notifications
- Verifying a live production deployment from CI/CD

---

## 🚀 Future Improvements

Potential future improvements include:

- Kubernetes deployment
- Terraform infrastructure as code
- Blue/green deployment
- Rolling deployments
- Container security scanning
- Dependency vulnerability scanning
- Centralized logging
- More advanced observability
- Secrets management using AWS Secrets Manager
- Automated infrastructure provisioning
- Expanded integration testing

---

## 👩‍💻 Author

**Tholiwe Mchunu**

Junior DevOps & Cloud Engineer

KwaZulu-Natal, South Africa

GitHub:

https://github.com/thandeka-ops

---

## 📌 Project Status

**Status: Production-style CI/CD and AWS monitoring project completed**

The project demonstrates an end-to-end DevOps workflow covering automated testing, Docker image publishing, AWS authentication, EC2 deployment, deployment verification, HTTPS, monitoring, alerting, and rollback.

The latest CI/CD workflow verifies the deployed application through HTTPS and confirms that the live application version matches the version produced by the pipeline. :contentReference[oaicite:14]{index=14}