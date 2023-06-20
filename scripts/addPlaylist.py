import boto3

# Configurações do DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
tabela_playlist = dynamodb.Table('playlist')

# Popula os dados na tabela Playlist
tabela_playlist.put_item(
    Item={
        'idPlaylist': 1,
        'nomePlaylist': 'Vibes Inesquecíveis',
        'idMusica': 3,
        'idUsuario': 1
    }
)

tabela_playlist.put_item(
    Item={
        'idPlaylist': 2,
        'nomePlaylist': 'Energy Boost',
        'idMusica': 5,
        'idUsuario': 4
    }
)

tabela_playlist.put_item(
    Item={
        'idPlaylist': 3,
        'nomePlaylist': 'Chill Mode',
        'idMusica': 3,
        'idUsuario': 1
    }
)

tabela_playlist.put_item(
    Item={
        'idPlaylist': 4,
        'nomePlaylist': 'Indie Discoveries',
        'idMusica': 4,
        'idUsuario': 2
    }
)

tabela_playlist.put_item(
    Item={
        'idPlaylist': 5,
        'nomePlaylist': 'Feel Good Jams',
        'idMusica': 3,
        'idUsuario': 10
    }
)

tabela_playlist.put_item(
    Item={
        'idPlaylist': 6,
        'nomePlaylist': 'Late Night Grooves',
        'idMusica': 10,
        'idUsuario': 7
    }
)

tabela_playlist.put_item(
    Item={
        'idPlaylist': 7,
        'nomePlaylist': 'Rhythm Revolution',
        'idMusica': 2,
        'idUsuario': 7
    }
)

tabela_playlist.put_item(
    Item={
        'idPlaylist': 8,
        'nomePlaylist': 'Soulful Serenade',
        'idMusica': 8,
        'idUsuario': 9
    }
)

tabela_playlist.put_item(
    Item={
        'idPlaylist': 9,
        'nomePlaylist': 'Epic Soundscapes',
        'idMusica': 9,
        'idUsuario': 10
    }
)

tabela_playlist.put_item(
    Item={
        'idPlaylist': 10,
        'nomePlaylist': 'Dance Party Anthems',
        'idMusica': 10,
        'idUsuario': 1
    }
)

print("Dados populados com sucesso!")