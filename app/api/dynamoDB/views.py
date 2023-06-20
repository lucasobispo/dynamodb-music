import boto3

from fastapi import APIRouter

from app.api.dynamoDB.schema import Chave

router = APIRouter()

aws_access_key_id = ''
aws_secret_access_key = ''
aws_session_token = ''

@router.get("/", response_model=Chave)
async def buscar_dado(chave: Chave):
    # Configuração do cliente DynamoDB
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1',
                              aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key,
                              aws_session_token=aws_session_token)

    # Nome da tabela no DynamoDB
    nome_tabela = 'usuario'

    # Obtém a referência para a tabela
    tabela = dynamodb.Table(nome_tabela)

    # Realiza a consulta no banco de dados
    try:
        response = tabela.get_item(Key={'idUsuario': chave.idUsuario})
        item = response['Item']
        return Chave(
            idUsuario=item['idUsuario'],
            email=item['email'],
            senha=item['senha'],
            nome=item['nome'],
            urlfoto=item['urlfoto']

        )
    except Exception as e:
        return {"erro": str(e)}

