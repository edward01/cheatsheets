import axios from 'axios'

this.loading = true
this.errored = false
const promise = axios.get('/url')
return promise
  .then(resp => {
    this.info = response.data.records
  })
  .catch(error => {
    console.log('axios-error:', error)
    this.errored = true
  })
  .finally(() => this.loading = false)
