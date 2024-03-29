# define base image 
FROM python:3.10.9

COPY ./ ./

RUN pip install scikit-learn

#CMD python src/titans_pattern_main.py --env=dev
CMD ["python","src/main.py"]