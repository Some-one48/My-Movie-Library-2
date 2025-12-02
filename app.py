from flask import Flask, render_template
import csv

# Cria a aplicação Flask
app = Flask(__name__)

# Define a rota principal, que irá renderizar o index.html
@app.get("/")
def index():
    movies = []
    with open('movies.csv', mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            movies.append(row)

    return render_template("index.html", movies=movies)

@app.get("/movie/<int:movie_id>")
def movie_details(movie_id):
    found_movie = None

    with open('movies.csv', mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for movie in csv_reader:
            # Compara o ID da linha com o ID do filme
            if int(movie['id']) == movie_id:
                found_movie = movie
                break # Encontramos o filme, podemos parar o loop
        
    # Se o filme for encontrado, renderiza a página de detalhes
    if found_movie:
        return render_template("details.html", movie=found_movie)
    # Se não, retorna erro 404
    else:
        return "Movie not found!", 404

if __name__ == "__main__":
    app.run(debug=True)
