<template>
  <div>

  </div>
</template>


<script>
export default {
  props: ['id'],
  components: {},
  data () {
    const times = []
    for (let i = 0; i < 24; i++) { times.push(i + ':00') }
    return {
      foo: 'bar',
      times,
      event: this.createFreshEventObject(),
    }
  },
  created() {
    // api calls here
  },
  mounted() {
    // dom updates here
  },
  methods: {
    methodName1() {},
    createFreshEventObject() {},
  },
}
</script>


<style scoped>

</style>
