function createMovieCard(movie){
  const card = document.createElement('div')
  card.setAttribute('class', 'movie-card')
  const title = document.createElement('h3')
  title.innerText = movie.title
  card.appendChild(title)
  return card
}

let pageNo = 1
const movieList = document.querySelector('#movie-list')


// IntersectionObserver!!!!!!!!!!!!

// const observer = new IntersectionObserver(callback,{rootMargin:'0% 0% -50% 0%'})

// function callback(entries,observer){
//   entries.forEach(entry => {
//     if(entry.isIntersecting){
//       console.log(entry.target.innerText)
//       entry.target.style.backgroundColor = 'crimson'
//     }
//     else{
//       entry.target.style.backgroundColor = 'olive'
//     }
//   })
// }

// fetchMovie!!!!!!!!!!!!

function fetchMovie(){
  axios({
    url : 'https://api.themoviedb.org/3/movie/popular',
    params:{
      api_key : '3e522bb11d9503474e85e9a710de1de4',
      language:'ko-KR',
      page:pageNo,
    },
  })
  .then(res =>{
    const movies = res.data.results
    movies.forEach(movie =>{
      movieList.appendChild(createMovieCard(movie))
    })
    pageNo += 1
  })
  .catch(err=>{
    console.log(err)
  })
}

const observer = new IntersectionObserver(callback)

const sentinel = document.querySelector('#sentinel')
observer.observe(sentinel)

function callback(entries,observer){
    entries.forEach(entry => {
      if(entry.isIntersecting){
        fetchMovie()
      }
    })
  }




// for(let i = 0; i < 20; i++){
//   const card = createMovieCard({title : `Title ${i}`})
//   movieList.appendChild(card)
//   observer.observe(card)       //관찰할 대상을 등록
// }

// document.addEventListener('scroll', function(event){
//   const {scrollHeight, scrollTop, clientHeight} = document.documentElement
//   // console.log(scrollHeight, scrollTop, clientHeight, scrollHeight- scrollTop)
//   if(Math.ceil(scrollHeight- scrollTop) === clientHeight){
//     // API : 3e522bb11d9503474e85e9a710de1de4
//     // url : https://api.themoviedb.org/3/movie/popular
//     axios({
//       url : 'https://api.themoviedb.org/3/movie/popular',
//       params:{
//         api_key : '3e522bb11d9503474e85e9a710de1de4',
//         language:'ko-KR',
//         page:pageNo,
//       },
//     })
//     .then(res =>{
//       const movies = res.data.results
//       movies.forEach(movie =>{
//         movieList.appendChild(createMovieCard(movie))
//       })
//       pageNo += 1
//     })
//     .catch(err=>{
//       console.log(err)
//     })
//   }
// })