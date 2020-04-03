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
    ],
    books: [
      { id: 1, title: 'Ender\'s Game', available: true },
      { id: 2, title: 'Harry Potter and the Goblet of Fire', available: true },
      { id: 3, title: 'Fahrenheit 451', available: false }
    ]
  },
  getters: {
    countLinks: state => state.links.length,
    availableBooks: state => {
      return state.books.filter(book => book.available);
    }
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
    },
    toggleAvailability(state, book) {
      const index = state.books.findIndex(b => b.id === book.id);
      state.books[index].available = !state.books[index].available;
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
    },
    async rentBook(context, book) {
      context.commit('toggleAvailability', book);

      /* commit multiple mutations
      context.commit('logDateTime');
      context.commit('saveUsername');
      */

      /* commit mutation after API call
      await LibraryAPI.rentBook(book);
      context.commit('setUnavailable', book);
      */
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

    <select class="form-control" id="selectDepartment" v-model="selectedDepartment">
      ...
    </select>
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
    // or with modules
    ...mapState('user', ['addresses', 'creditCards']),
    ...mapState('vendor', ['products', 'ratings']),

    // with form 2 way binding
    selectedDepartment: {
      get() {
        return this.$store.state.navbar.selectedDepartment
      },
      set(value) {
        this.setSelectedDepartment(value)
      }
    },
  },
  methods: {
    ...mapMutations(['ADD_LINK']),
    ...mapActions(['removeAll', 'removeLink']),
    // or with modules
    ...mapMutations('navbar', ['setMiniSideBar', 'setSelectedDepartment']),

    removeAllLinks() {
      this.removeAll().then(() => {
        this.msg = 'They have been removed'
      })
    },
    addLink() {
      this.ADD_LINK(this.newLink)
      this.newLink = ''
    },
    removeLinks(link) {
      this.removeLink(link)
    }
  }
}
</script>
// ------------------------------------------------------------
