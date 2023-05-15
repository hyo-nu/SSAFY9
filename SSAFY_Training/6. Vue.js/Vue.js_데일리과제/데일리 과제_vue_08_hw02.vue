methods: {
  login: function () {
      axios(...생략...)
      .then(res => {
	    const token = res.data.access
      localStorage.setItem('jwt',token)
      })
  }
}