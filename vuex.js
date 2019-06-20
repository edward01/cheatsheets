// -----------------
// vuejs-vuex.js
// -----------------
import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)

const store = new Vuex.Store({
    state: {
        movies: [],
    },
    getters: {
        movies: state => state.movies,
    },
    mutations: {
        setMovies (state, movies) {
            state.movies = movies
        },
    },
    actions: {
        getMovies (context) {
            axios.get('/api/movies')
                .then((movies) => {
                    context.commit('setMovies', movies)
                })
        },
    },
})

new Vue({
    el: '#app',
    store,
    render: h => h(App)
})
// ------------------------------------------------------------

// -----------------
// MovieActions.vue
// -----------------
<template lang="html">
    <div>
        <div v-for="m in movies">
            <p>{{ m.name }}</p>
            <p>{{ m.description }}</p>
        </div>

        <div v-for="a in actors">
            <p>{{ a.firstName }} {{ a.lastName }}</p>
        </div>
    </div>
</template>

<script>
export default {
    mounted () {
        this.$store.dispatch('getMovies')
    },
    computed: {
        movies () {
            this.$store.getters.movies
        }
    }
}
</script>
// ------------------------------------------------------------
