FROM python:3.10-slim

WORKDIR /app

COPY student_grade.py .

ENTRYPOINT ["python", "student_grade.py"]
