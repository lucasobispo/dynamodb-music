import json
import boto3

# Configurações do DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
tabela_musica = dynamodb.Table('musica')

# Popula os dados na tabela Musica
tabela_musica.put_item(
    Item={
        'idMusica': 1,
        'nomeMusica': 'Blinding Lights',
        'genero': 'R&B, Pop',
        'urlmusica': 's3://uspfy/musica/Blinding_Lights.mp3',
        'Artista': json.dumps({
            'idArtista': 1,
            'nomeArtista': 'The Weeknd'
        }),
        'Album': json.dumps({
            'idAlbum': 1,
            'nomeAlbum': 'After Hours',
            'ano': 2020,
            'urlImagem': 's3://uspfy/imagem/imagem1.jpg'
        })
    }
)

tabela_musica.put_item(
    Item={
        'idMusica': 2,
        'nomeMusica': 'drivers license',
        'genero': 'Pop',
        'urlmusica': 's3://uspfy/musica/drivers_license.mp3',
        'Artista': json.dumps({
            'idArtista': 2,
            'nomeArtista': 'Olivia Rodrigo'
        }),
        'Album': json.dumps({
            'idAlbum': 2,
            'nomeAlbum': 'SOUR',
            'ano': 2021,
            'urlImagem': 's3://uspfy/imagem/imagem2.jpg'
        })
    }
)

tabela_musica.put_item(
    Item={
        'idMusica': 3,
        'nomeMusica': 'Bad Guy',
        'genero': 'Pop',
        'urlmusica': 's3://uspfy/musica/Bad_Guy.mp3',
        'Artista': json.dumps({
            'idArtista': 3,
            'nomeArtista': 'Billie Eilish'
        }),
        'Album': json.dumps({
            'idAlbum': 3,
            'nomeAlbum': 'WHEN WE ALL FALL ASLEEP, WHERE DO WE GO?',
            'ano': 2019,
            'urlImagem': 's3://uspfy/imagem/imagem3.jpg'
        })
    }
)

tabela_musica.put_item(
    Item={
        'idMusica': 4,
        'nomeMusica': 'Dance Monkey',
        'genero': 'Pop, Eletrônica',
        'urlmusica': 's3://uspfy/musica/Dance_Monkey.mp3',
        'Artista': json.dumps({
            'idArtista': 4,
            'nomeArtista': 'Tones and I'
        }),
        'Album': json.dumps({
            'idAlbum': 4,
            'nomeAlbum': 'The Kids Are Coming',
            'ano': 2019,
            'urlImagem': 's3://uspfy/imagem/imagem4.jpg'
        })
    }
)

tabela_musica.put_item(
    Item={
        'idMusica': 5,
        'nomeMusica': 'Shape of You',
        'genero': 'Pop',
        'urlmusica': 's3://uspfy/musica/Shape_of_You.mp3',
        'Artista': json.dumps({
            'idArtista': 5,
            'nomeArtista': 'Ed Sheeran'
        }),
        'Album': json.dumps({
            'idAlbum': 5,
            'nomeAlbum': 'Divide',
            'ano': 2017,
            'urlImagem': 's3://uspfy/imagem/imagem5.jpg'
        })
    }
)

tabela_musica.put_item(
    Item={
        'idMusica': 6,
        'nomeMusica': 'Someone You Loved',
        'genero': 'Pop, R&B',
        'urlmusica': 's3://uspfy/musica/Someone_You_Loved.mp3',
        'Artista': json.dumps({
            'idArtista': 6,
            'nomeArtista': 'Lewis Capaldi'
        }),
        'Album': json.dumps({
            'idAlbum': 6,
            'nomeAlbum': 'Divinely Uninspired to a Hellish Extent',
            'ano': 2019,
            'urlImagem': 's3://uspfy/imagem/imagem6.jpg'
        })
    }
)

tabela_musica.put_item(
    Item={
        'idMusica': 7,
        'nomeMusica': 'Watermelon Sugar',
        'genero': 'Pop, Rock',
        'urlmusica': 's3://uspfy/musica/Watermelon_Sugar.mp3',
        'Artista': json.dumps({
            'idArtista': 7,
            'nomeArtista': 'Harry Styles'
        }),
        'Album': json.dumps({
            'idAlbum': 7,
            'nomeAlbum': 'Fine Line',
            'ano': 2019,
            'urlImagem': 's3://uspfy/imagem/imagem7.jpg'
        })
    }
)

tabela_musica.put_item(
    Item={
        'idMusica': 8,
        'nomeMusica': 'Peaches',
        'genero': 'Pop, R&B',
        'urlmusica': 's3://uspfy/musica/Peaches.mp3',
        'Artista': json.dumps({
            'idArtista': 8,
            'nomeArtista': 'Justin Bieber ft. Daniel Caesar, Giveon'
        }),
        'Album': json.dumps({
            'idAlbum': 8,
            'nomeAlbum': 'Justice',
            'ano': 2021,
            'urlImagem': 's3://uspfy/imagem/imagem8.jpg'
        })
    }
)

tabela_musica.put_item(
    Item={
        'idMusica': 9,
        'nomeMusica': 'Save Your Tears',
        'genero': 'R&B, Pop',
        'urlmusica': 's3://uspfy/musica/Save_Your_Tears.mp3',
        'Artista': json.dumps({
            'idArtista': 1,
            'nomeArtista': 'The Weeknd ft. Ariana Grande'
        }),
        'Album': json.dumps({
            'idAlbum': 1,
            'nomeAlbum': 'After Hours',
            'ano': 2020,
            'urlImagem': 's3://uspfy/imagem/imagem9.jpg'
        })
    }
)

tabela_musica.put_item(
    Item={
        'idMusica': 10,
        'nomeMusica': 'Levitating',
        'genero': 'Pop, Dance',
        'urlmusica': 's3://uspfy/musica/Levitating.mp3',
        'Artista': json.dumps({
            'idArtista': 10,
            'nomeArtista': 'Dua Lipa ft. DaBaby'
        }),
        'Album': json.dumps({
            'idAlbum': 10,
            'nomeAlbum': 'Future Nostalgia',
            'ano': 2020,
            'urlImagem': 's3://uspfy/imagem/imagem10.jpg'
        })
    }
)

print("Dados populados com sucesso!")