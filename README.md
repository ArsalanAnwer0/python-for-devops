# Python for DevOps

A comprehensive Python learning repository for DevOps engineers, covering fundamental concepts to advanced automation and monitoring tools. This repository provides practical examples and real-world scenarios for infrastructure automation and cloud operations.

## 📁 Repository Structure

```
python-for-devops/
├── beginner/                    # Python fundamentals for DevOps
│   ├── OOP/                    # Object-Oriented Programming concepts
│   ├── activities/             # Hands-on practice exercises
│   ├── Fake_News_Headline_Generator/  # Project-based learning
│   └── core concepts files     # Basic Python syntax and concepts
├── intermediate/               # Advanced DevOps automation
├── expert/                    # Complex DevOps scenarios
└── README.md                  # This file
```

## 🎯 Learning Path

### 📚 Beginner Level
**Location:** `/beginner/`

Master Python fundamentals essential for DevOps work:

#### Core Python Concepts
- **`comments.py`** - Documentation and code commenting best practices
- **`data_types.py`** - Variables, strings, numbers, booleans
- **`operators.py`** - Arithmetic, comparison, logical, and assignment operators
- **`control_statements.py`** - If/else, loops, and flow control
- **`sample.py`** - Basic Python syntax examples
- **`concepts.py`** - Variables, data types, operators, and comments
- **`conditionals.py`** - Control flow and decision making
- **`hello.py`** - Basic input/output and string manipulation
- **`input_output.py`** - User interaction and f-string formatting
- **`tasks.py`** - Cross-platform OS detection and system operations
- **`data_structures.py`** - Lists, dictionaries, tuples for configuration management

#### Object-Oriented Programming (`/OOP/`)
- **`methods.py`** - Instance, class, and static methods
- **`inheritance.py`** - Class inheritance and method overriding
- **`polymorphism.py`** - Method overloading and polymorphic behavior
- **`abstraction.py`** - Abstract classes and methods
- **`composition.py`** - Object composition patterns
- **`aggregation.py`** - Object aggregation relationships
- **`duck_typing.py`** - Dynamic typing and duck typing concepts
- **`magic_method.py`** - Special methods and operator overloading
- **`nested_class.py`** - Inner classes and nested structures
- **`property_decorator.py`** - Property decorators and getters/setters
- **`static.py`** - Static methods and class variables
- **`super.py`** - Super keyword and method resolution order

#### Practical Activities (`/activities/`)
**16 hands-on exercises** covering:
- **`act_one.py` to `act_sixteen.py`** - Progressive coding exercises
- **`for_act_sixteen.py`** - Advanced looping exercises
- **`youtube.db`** - Database interaction examples

#### Project-Based Learning
- **`Fake_News_Headline_Generator/`** - Complete project demonstrating:
  - File handling and data processing
  - String manipulation and text generation
  - Project structure and organization

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

- **Core Python**: subprocess, os, platform, datetime, sqlite3
- **Object-Oriented Programming**: Classes, inheritance, polymorphism, abstraction
- **Web Framework**: Flask for monitoring dashboards
- **Cloud Services**: AWS boto3 for S3 operations
- **System Monitoring**: psutil for system metrics
- **Task Scheduling**: schedule library for automation
- **Containerization**: Docker integration
- **API Integration**: requests library
- **Database**: SQLite for data storage
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

2. **Start with core Python concepts:**
```bash
cd beginner
python data_types.py
python operators.py
python control_statements.py
```

3. **Learn Object-Oriented Programming:**
```bash
cd beginner/OOP
python methods.py
python inheritance.py
python polymorphism.py
```

4. **Practice with activities:**
```bash
cd beginner/activities
python act_one.py
# Continue through act_sixteen.py
```

5. **Try the monitoring dashboard:**
```bash
cd intermediate/monitoring_app
python app.py
# Visit: http://localhost:5000/dashboard
```

6. **Test AWS S3 operations:**
```bash
cd intermediate
# Configure AWS credentials first
python aws_s3.py
```

## 📚 Learning Progression

### Phase 1: Python Fundamentals (Beginner)
1. **Basic Syntax** → `data_types.py`, `operators.py`, `comments.py`
2. **Control Flow** → `control_statements.py`, `conditionals.py`
3. **Data Structures** → `data_structures.py`
4. **Functions & Input/Output** → `hello.py`, `input_output.py`

### Phase 2: Object-Oriented Programming
1. **Basic OOP** → `methods.py`, `inheritance.py`
2. **Advanced OOP** → `polymorphism.py`, `abstraction.py`
3. **Design Patterns** → `composition.py`, `aggregation.py`
4. **Python-Specific** → `duck_typing.py`, `magic_method.py`

### Phase 3: Hands-on Practice
1. **Activities** → Complete all 16 activities in sequence
2. **Project Work** → Fake News Headline Generator
3. **System Integration** → `tasks.py` for OS operations

### Phase 4: DevOps Applications (Intermediate)
1. **System Monitoring** → `sys_utils.py`, monitoring app
2. **Cloud Operations** → `aws_s3.py`
3. **Automation** → `backup.py`, `devops_commands.py`
4. **Containerization** → `docker_run.py`

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

## 🎯 Practice Exercises

The `/beginner/activities/` folder contains 16 progressive exercises:
- **Activities 1-4**: Basic syntax and variables
- **Activities 5-8**: Control structures and loops
- **Activities 9-12**: Functions and data structures
- **Activities 13-16**: File handling and database operations

Each activity builds upon previous concepts, providing hands-on experience with Python fundamentals.

## 🌟 Key Features

- **Comprehensive Coverage**: From basic syntax to advanced OOP concepts
- **Cross-platform Compatibility**: Works on Windows, macOS, and Linux
- **Progressive Learning**: Structured from basics to advanced
- **Hands-on Practice**: 16+ practical exercises and activities
- **Real-world Projects**: Complete applications and tools
- **Error Handling**: Robust exception management
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
- **SQLite Documentation**: https://docs.python.org/3/library/sqlite3.html

## 📞 Support

If you have questions or need help:

1. Check the code comments in each file
2. Review the examples in the beginner section
3. Try the hands-on activities for practice
4. Open an issue on GitHub
5. Refer to the learning resources above

---
