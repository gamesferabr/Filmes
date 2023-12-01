window.onload = function() {
    async function getMovies() {
        let response = await fetch(`/movie/`);
        let data = await response.json();
        let articlemovies = document.getElementsByTagName("article")
        

        for(let i = 0; i < articlemovies.length; i++){
            const nomefilme = document.querySelector(`.nomefilme${i}`);
            nomefilme.textContent = data.movies[i].title; 

            const ratingfilme = document.querySelector(`.score${i}`);
            ratingfilme.textContent = data.movies[i].vote_average.toFixed(1);
            
            const imagemfilme = document.querySelector(`.img${i}`);
            imagemfilme.src = "https://image.tmdb.org/t/p/w500/" + data.movies[i].poster_path;
            imagemfilme.alt = data.movies[i].title;
            
        }
    }

    getMovies();  // Chamada inicial da função

    const botao = document.getElementById("botaorecomendacao");
    botao.addEventListener('click', getMovies);  // Adicionar o evento
}
