import boto3

# Configurações do DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
tabela_usuario = dynamodb.Table('usuario')

# Popula os dados na tabela Usuario
with tabela_usuario.batch_writer() as batch:
    batch.put_item(
        Item={
            'idUsuario': '1',
            'email': 'pedro@gmail.com',
            'senha': 'senha123',
            'nome': 'pedro',
            'urlfoto': 's3://uspfy/photo/foto1.jpg'
        }
    )
    batch.put_item(
        Item={
            'idUsuario': '2',
            'email': 'maria@gmail.com',
            'senha': 'senha456',
            'nome': 'maria',
            'urlfoto': 's3://uspfy/photo/foto2.jpg'
        }
    )
    batch.put_item(
        Item={
            'idUsuario': '3',
            'email': 'pedro@gmail.com',
            'senha': 'senha789',
            'nome': 'pedro',
            'urlfoto': 's3://uspfy/photo/foto3.jpg'
        }
    )
    batch.put_item(
        Item={
            'idUsuario': '4',
            'email': 'ana@gmail.com',
            'senha': 'senha321',
            'nome': 'ana',
            'urlfoto': 's3://uspfy/photo/foto4.jpg'
        }
    )
    batch.put_item(
        Item={
            'idUsuario': '5',
            'email': 'carlos@gmail.com',
            'senha': 'senha654',
            'nome': 'carlos',
            'urlfoto':'s3://uspfy/photo/foto5.jpg'
        }
    )
    batch.put_item(
        Item={
            'idUsuario': '6',
            'email': 'laura@gmail.com',
            'senha': 'senha987',
            'nome': 'laura',
            'urlfoto':'s3://uspfy/photo/foto6.jpg'
        }
    )
    batch.put_item(
        Item={
            'idUsuario': '7',
            'email': 'rodrigo@gmail.com',
            'senha': 'senhaabc',
            'nome': 'rodrigo',
            'urlfoto': 's3://uspfy/photo/foto7.jpg'
        }
    )
    batch.put_item(
        Item={
            'idUsuario': '8',
            'email': 'clara@gmail.com',
            'senha': 'senhaxyz',
            'URLfoto': 's3://uspfy/photo/foto8.jpg'
        }
    )
    batch.put_item(
        Item={
            'idUsuario': '9',
            'email': 'paulo@gmail.com',
            'senha': 'senhajkl',
            'nome': 'paulo',
            'urlfoto': 's3://uspfy/photo/foto9.jpg'
        }
    )
    batch.put_item(
        Item={
            'idUsuario': '10',
            'email': 'amanda@gmail.com',
            'senha': 'senhamno',
            'nome': 'amanda',
            'urlfoto': 's3://uspfy/photo/foto10.jpg'
        }
    )

print("Dados populados com sucesso!")