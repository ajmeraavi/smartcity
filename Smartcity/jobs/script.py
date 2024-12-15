from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, TimestampType
from datetime import datetime
import uuid

spark = SparkSession.builder.appName("GenerateEmergencyParquet").getOrCreate()

emergencySchema = StructType([
    StructField("id", StringType(), True),
    StructField("vehicle_id", StringType(), True),
    StructField("incidentId", StringType(), True),
    StructField("type", StringType(), True),
    StructField("timestamp", TimestampType(), True),
    StructField("location", StringType(), True),
    StructField("status", StringType(), True),
    StructField("description", StringType(), True),
])

emergency_data = [
    (str(uuid.uuid4()), "Vehicle-001", str(uuid.uuid4()), "Accident", datetime.now(), "(37.3382, -121.8863)", "Active", "Minor collision"),
    (str(uuid.uuid4()), "Vehicle-002", str(uuid.uuid4()), "Fire", datetime.now(), "(37.3541, -121.9552)", "Resolved", "Vehicle fire extinguished"),
]

emergencyDF = spark.createDataFrame(emergency_data, schema=emergencySchema)
emergencyDF.show()

emergencyDF.write.parquet("emergency_data.parquet", mode="overwrite")
print("emergency_data.parquet generated successfully.")
