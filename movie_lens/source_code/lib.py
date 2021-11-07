from IPython.display import display, HTML
import pandas as pd
import numpy as np
import math


def displayMovies(movies, movieIds, ratings=[]):
    html = ""
    for i, movieId in enumerate(movieIds):
        movie = movies[movies["movieId"] == movieId].iloc[0]
        html += f"""
            <div style="display:inline-block;min-width:150px;max-width:150px; vertical-align:top">
                <img src='{movie.imgurl}' width=120> <br/>
                <span>{movie.title}</span> <br/>
                {f"<span>{ratings[i]}</span> <br/>" if len(ratings) > 0 else ""}
                <span>{"".join([f"<li>{genre}</li>" for genre in movie.genres.split('|')])}</span>
            </div>
        """
        print(movie)
        print(movieId)
    display(HTML(html))


def getMAE(real, pred):
    errors = (real - pred).abs().mean()
    return errors


def getRMSE(real, pred):
    errors = math.sqrt((real - pred).pow(2).mean())
    return errors
