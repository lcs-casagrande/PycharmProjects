import boto3
#Criando serviço com as suas credenciais da AWS
client = boto3.client(
    service_name='sns',
    region_name='sa-east-1',
    aws_access_key_id='casagrande-san@hotmail.com',
    aws_secret_access_key='Eng.1320'
)

#Envia o SMS paa o número desejado
client.publish(
    PhoneNumber='+5511974645103',
    Message='Olá Pycodebr:)'
)