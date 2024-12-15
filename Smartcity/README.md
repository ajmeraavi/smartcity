
# Smart City IoT Data Streaming Project

This project is designed to simulate and analyze data streaming in a smart city scenario. It processes and integrates multiple data streams such as GPS, traffic, weather, and emergency data to provide actionable insights.

---

## Features

### Required Features
1. **Data Processing**:
   - Reads and processes Parquet data files (e.g., GPS, traffic, weather, emergency).
   - Implements data transformations using PySpark.

2. **Configuration**:
   - Configurable parameters for data processing in `config.py`.

3. **Execution Pipeline**:
   - A main execution script (`main.py`) that orchestrates data ingestion and processing.

4. **Environment Setup**:
   - Docker Compose configuration (`docker-compose.yml`) for containerized deployment.

### Additional Features
1. **Scalability**:
   - Uses Apache Spark for large-scale data processing.
   
2. **Extensibility**:
   - Modular scripts for adding new data sources and processing logic.
   
3. **Data Storage**:
   - Supports Parquet format for efficient storage and querying.

---

## Setup Instructions

### Prerequisites
1. **Install Docker**:
   - [Docker Installation Guide](https://docs.docker.com/get-docker/)

2. **Install Python and Virtual Environment**:
   - Python 3.8+ is recommended.
   - Install `virtualenv`: `pip install virtualenv`.

3. **Install Spark**:
   - [Spark Installation Guide](https://spark.apache.org/docs/latest/)

### Step-by-Step Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repository-url.git
   cd Smartcity
   ```

2. **Set Up Virtual Environment**:
   ```bash
   virtualenv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate     # For Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Docker Compose**:
   ```bash
   docker-compose up
   ```

5. **Execute the Main Script**:
   ```bash
   python jobs/main.py
   ```

---

## Best Practices
1. **Code Structure**:
   - Follow modular design principles. Place reusable utilities in the `config.py` file.
   
2. **Data Handling**:
   - Validate all input data to ensure consistency.
   - Log data processing steps for better debugging.

3. **Containerization**:
   - Use Docker for consistent runtime environments.
   - Define all environment variables in `.env` files.

4. **Performance**:
   - Optimize PySpark queries for faster processing.
   - Utilize Spark's caching mechanism for frequently accessed data.

5. **Version Control**:
   - Use Git to track changes.
   - Push feature branches for collaborative development.

---

## Directory Structure
```
Smartcity/
│
├── jobs/                      # Contains processing scripts
│   ├── main.py                # Main execution script
│   ├── config.py              # Configuration settings
│   ├── script.py              # Additional utility script
│   └── spark-city.py          # Spark job script
│
├── weather_data.parquet/      # Weather data in Parquet format
├── traffic_data.parquet/      # Traffic data in Parquet format
├── gps_data.parquet/          # GPS data in Parquet format
├── emergency_data.parquet/    # Emergency data in Parquet format
│
├── requirements.txt           # Python dependencies
├── docker-compose.yml         # Docker Compose file
└── README.md                  # Project documentation
```

---
