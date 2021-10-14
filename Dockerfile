FROM continuumio/anaconda3
COPY ./app.py /deploy/
COPY ./environment.yml /deploy/
COPY ./model.pkl /deploy/
RUN conda update -y conda
WORKDIR /deploy
RUN conda env create -f environment.yml
SHELL ["conda", "run", "-n", "summerschool", "/bin/bash", "-c"]
EXPOSE 5050
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "summerschool", "python", "app.py"]