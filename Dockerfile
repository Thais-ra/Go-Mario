# especificando a imagem
FROM python:3 
# copiar tudo q ta no diretorio atual e passa para o /app
COPY . /app 
# muda para o diretorio /app
WORKDIR /app 
# instala bibliotecas que faltam
RUN pip install -r requirements.txt --use-feature=2020-resolver
# comando para executar o codigo
CMD python go_mario.py