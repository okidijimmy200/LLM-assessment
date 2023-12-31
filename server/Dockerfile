FROM pytorch/pytorch:latest 

WORKDIR /

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["/bin/sh", "-c", ". ./info.sh && python main.py"]