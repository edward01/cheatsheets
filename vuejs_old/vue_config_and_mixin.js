// on "src/config.js"
module.exports = {
  title: 'Shuffle It! 2',
  description: 'An amazing number randomizer web app',
  myTwitter: 'https://twitter.com/ediward316',
  myPortfolio: 'https://twitter.com/ediward316',
}


// to use, example on "src/mixins/appConfigs.js"
import * as appConfig from '@/config'
export default {
  data() {
    return {
      appConfig
    }
  },
}


// from the component that will use the mixin
// "src/views/About.vue"
// <template>
  <v-toolbar-title>{{ appConfig.title }}</v-toolbar-title>
// </template>
// <script>
import appConfigs from '@/mixins/appConfigs';
export default {
  mixins: [appConfigs],
  data() { },
}
// </script>
