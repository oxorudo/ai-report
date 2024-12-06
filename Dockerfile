# Python 베이스 이미지 사용
FROM python:3.8

# 환경 변수 설정
ENV PYTHONUNBUFFERED 1

# 작업 디렉토리 설정
WORKDIR /app

# 프로젝트 파일 복사
COPY . /app

# 의존성 설치
RUN pip install --no-cache-dir -r requirements.txt

# Django 서버 실행
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]