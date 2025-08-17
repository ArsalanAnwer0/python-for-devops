# Python for DevOps

A comprehensive Python learning repository for DevOps engineers, covering fundamental concepts to advanced automation and monitoring tools. This repository provides practical examples and real-world scenarios for infrastructure automation and cloud operations.

## 📁 Repository Structure

```
python-for-devops/
├── beginner/           # Python fundamentals for DevOps
├── intermediate/       # Advanced DevOps automation
├── expert/            # Complex DevOps scenarios
└── README.md          # This file
```

## 🎯 Learning Path

### 📚 Beginner Level
**Location:** `/beginner/`

Master Python fundamentals essential for DevOps work:

- **`concepts.py`** - Variables, data types, operators, and comments
- **`conditionals.py`** - Control flow and decision making
- **`hello.py`** - Basic input/output and string manipulation
- **`input_output.py`** - User interaction and f-string formatting
- **`tasks.py`** - Cross-platform OS detection and system operations
- **`data_structures.py`** - Lists, dictionaries, tuples for configuration management

### 🚀 Intermediate Level
**Location:** `/intermediate/`

Practical DevOps automation and monitoring:

- **`api_test.py`** - REST API integration and weather data fetching
- **`devops_commands.py`** - Subprocess management for system commands
- **`docker_run.py`** - Container orchestration with Docker
- **`sys_utils.py`** - Cross-platform system monitoring utilities
- **`monitoring_app/`** - Complete Flask monitoring dashboard
  - **`app.py`** - Web server with CPU/memory monitoring endpoints
  - **`templates/index.html`** - Interactive dashboard with real-time gauges
- **`aws_s3.py`** - Cloud storage automation with boto3
- **`backup.py`** - Automated backup system with scheduling

### 🎓 Expert Level
**Location:** `/expert/` (Future advanced scenarios)

## 🛠️ Technologies & Libraries

- **Core Python**: subprocess, os, platform, datetime
- **Web Framework**: Flask for monitoring dashboards
- **Cloud Services**: AWS boto3 for S3 operations
- **System Monitoring**: psutil for system metrics
- **Task Scheduling**: schedule library for automation
- **Containerization**: Docker integration
- **API Integration**: requests library
- **Frontend**: HTML5, CSS3, JavaScript with Plotly.js

## ⚙️ Prerequisites

```bash
# Python 3.7+
python --version

# Required packages
pip install flask psutil boto3 schedule requests
```

## 🚀 Quick Start

1. **Clone the repository:**
```bash
git clone https://github.com/ArsalanAnwer0/python-for-devops.git
cd python-for-devops
```

2. **Start with beginner concepts:**
```bash
cd beginner
python concepts.py
```

3. **Try the monitoring dashboard:**
```bash
cd intermediate/monitoring_app
python app.py
# Visit: http://localhost:5000/dashboard
```

4. **Test AWS S3 operations:**
```bash
cd intermediate
# Configure AWS credentials first
python aws_s3.py
```

## 📊 Monitoring Dashboard Features

The intermediate monitoring app includes:

- **Real-time System Metrics**: CPU and memory utilization
- **Interactive Gauges**: Visual representation with color-coded alerts
- **RESTful API Endpoints**:
  - `/` - Health check
  - `/cpu` - System CPU usage
  - `/process-cpu` - Process-specific metrics
  - `/dashboard` - Web interface
- **Auto-refresh**: Updates every 10 seconds
- **Responsive Design**: Mobile-friendly interface

## 🔧 DevOps Use Cases

### Infrastructure Monitoring
```python
# System health checking
from intermediate.sys_utils import Utilities
monitor = Utilities()
monitor.show_disk_space()
monitor.show_ram()
```

### Automated Backups
```python
# Scheduled backup system
from intermediate.backup import create_backup
create_backup("/important/data", "/backup/location")
```

### Container Management
```python
# Docker operations
from intermediate.devops_commands import execute_command
result = execute_command("docker ps -a")
```

### Cloud Storage Operations
```python
# AWS S3 automation
from intermediate.aws_s3 import upload_to_bucket
upload_to_bucket(s3, "backup.tar.gz", "/local/file", "my-bucket")
```

## 🌟 Key Features

- **Cross-platform Compatibility**: Works on Windows, macOS, and Linux
- **Error Handling**: Robust exception management
- **Real-world Scenarios**: Practical DevOps automation examples
- **Progressive Learning**: Structured from basics to advanced
- **Production Ready**: Code suitable for production environments
- **Documentation**: Well-commented code with clear explanations

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎓 Learning Resources

- **Python Official Documentation**: https://docs.python.org/3/
- **Flask Documentation**: https://flask.palletsprojects.com/
- **AWS boto3 Documentation**: https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
- **Docker Documentation**: https://docs.docker.com/

## 📞 Support

If you have questions or need help:

1. Check the code comments in each file
2. Review the examples in the beginner section
3. Open an issue on GitHub
4. Refer to the learning resources above

---
