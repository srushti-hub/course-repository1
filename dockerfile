FROM python:3.10-slim

WORKDIR /app

COPY student_grade.py .

CMD ["python", "student_grade.py"]
