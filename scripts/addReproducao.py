import boto3

# Configurações do DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
tabela_reproducao = dynamodb.Table('reproducao')

# Popula os dados na tabela Reproducao
tabela_reproducao.put_item(
    Item={
        'idMusica': 1,
        'idUsuario': 4,
        'dataReproducao': '2023-01-29 12:00:00'
    }
)

tabela_reproducao.put_item(
    Item={
        'idMusica': 2,
        'idUsuario': 3,
        'dataReproducao': '2023-02-01 15:30:00'
    }
)

tabela_reproducao.put_item(
    Item={
        'idMusica': 6,
        'idUsuario': 3,
        'dataReproducao': '2023-03-16 08:45:00'
    }
)

tabela_reproducao.put_item(
    Item={
        'idMusica': 4,
        'idUsuario': 8,
        'dataReproducao': '2023-03-03 20:15:00'
    }
)

tabela_reproducao.put_item(
    Item={
        'idMusica': 1,
        'idUsuario': 5,
        'dataReproducao': '2023-05-01 10:00:00'
    }
)

tabela_reproducao.put_item(
    Item={
        'idMusica': 1,
        'idUsuario': 5,
        'dataReproducao': '2023-05-23 18:30:00'
    }
)

tabela_reproducao.put_item(
    Item={
        'idMusica': 4,
        'idUsuario': 8,
        'dataReproducao': '2023-06-05 14:20:00'
    }
)

tabela_reproducao.put_item(
    Item={
        'idMusica': 10,
        'idUsuario': 8,
        'dataReproducao': '2023-02-20 09:10:00'
    }
)

tabela_reproducao.put_item(
    Item={
        'idMusica': 2,
        'idUsuario': 9,
        'dataReproducao': '2023-04-06 16:40:00'
    }
)

tabela_reproducao.put_item(
    Item={
        'idMusica': 1,
        'idUsuario': 10,
        'dataReproducao': '2023-04-27 13:05:00'
    }
)

print("Dados populados com sucesso!")