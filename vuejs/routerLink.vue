<!-- literal string -->
<router-link to="home">Home</router-link>
<!-- renders to -->
<a href="home">Home</a>

<!-- Omitting `v-bind` is fine, just as binding any other prop -->
<router-link :to="'home'">Home</router-link>
<!-- same as above -->
<router-link :to="{ path: 'home' }">Home</router-link>

<!-- named route -->
<router-link :to="{ name: 'user', params: { userId: 123 }}">User</router-link>

<!-- with query, resulting in `/register?plan=private` -->
<router-link :to="{ path: 'register', query: { plan: 'private' }}">
  Register
</router-link>
