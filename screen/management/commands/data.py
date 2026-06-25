from typing import Any
from screen.models import Movie
from django.core.management.base import BaseCommand
from django.utils.text import slugify

class Command(BaseCommand):
    help='This cmd inserts review'

    def handle(self, *args:Any, **options:Any):
        Movie.objects.all().delete()
        title=[
            'Obsession',
            'Superman',
            'Avengerrs Doomsday',
            'F1',
            'Spiderman Brand new day'
        ]
        year=[
            '2026',
            '2025',
            '2026',
            '2025',
            '2026',
        ]
        img_src=[

            'https://posters.movieposterdb.com/26_03/0/37287335/l_-movie-poster_3db06a10.jpg',
            'https://posters.movieposterdb.com/25_06/2025/5950044/l_superman-movie-poster_acf06a86.jpg' ,
            'https://posters.movieposterdb.com/25_12/2026/21357150/l_avengers-doomsday-movie-poster_7046491b.jpg',
            'https://posters.movieposterdb.com/25_06/2025/16311594/s_f1-the-movie-movie-poster_c4cb907a.jpg',
            'https://posters.movieposterdb.com/26_05/2026/22084616/s_spider-man-brand-new-day-movie-poster_ffdef880.jpeg'
        ]
        for title,year,img_src in zip(title,year,img_src):
            Movie.objects.create(title=title,year=year,img_src=img_src)
        
        self.stdout.write(self.style.SUCCESS("Insterted data"))