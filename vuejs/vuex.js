// -----------------
// store.js
// -----------------
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        title: 'My Custom Title',
        links: [
            'http://google.com',
            'http://coursetro.com',
            'http://youtube.com'
        ]
    },
    getters: {
        countLinks: state => state.links.length
    },
    mutations: {
        ADD_LINK(state, link) {
            state.links.push(link)
        },
        REMOVE_LINK(state, link) {
            state.links.splice(link, 1)
        },
        REMOVE_ALL(state) {
            state.links = []
        }
    },
    actions: {
        removeLink(context, link) {
            context.commit('REMOVE_LINK', link)
        },
        removeAll({ commit }) { // this is called "argument destructuring"
            return new Promise((resolve, reject) => {
                setTimeout(() => {
                    commit('REMOVE_ALL')
                    resolve()
                }, 1500)
            })
        }
    }
})
// ------------------------------------------------------------

// -----------------
// HelloWorld.vue
// -----------------
<template>
    <div class="stats">
        <h1>{{ title }}</h1>
        <p>There are currently {{ countLinks }} links</p>

        <button v-on:click="removeAllLinks">Remove all links</button>
        <p>{{ msg }}</p>

        <form @submit.prevent="addLink">
            <input class="link-input" type="text" placeholder="Add a Link" v-model="newLink" />
        </form>

        <ul>
            <li v-for="(link, index) in links" v-bind:key="index">
            {{ link }}
            <button v-on:click="removeLinks(index)" class="rm">Remove</button>  <!-- Add this -->
            </li>
        </ul>
    </div>
</template>

<script>
import { mapState, mapGetters, mapMutations, mapActions } from 'vuex'

export default {
    name: 'Stats',
    data() {
        return {
            msg: '',
            newLink: ''
        }
    },
    computed: {
        ...mapState(['title', 'links']),
        ...mapGetters(['countLinks']),
    },
    methods: {
        ...mapMutations(['ADD_LINK']),
        ...mapActions(['removeAll', 'removeLink']),
        removeAllLinks() {
            this.removeAll().then(() => {
                this.msg = 'They have been removed'
            })
        },
        addLink () {
            this.ADD_LINK(this.newLink)
            this.newLink = ''
        },
        removeLinks (link) {
            this.removeLink(link)
        }
    }
}
</script>
// ------------------------------------------------------------
