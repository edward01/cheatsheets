<script>
export default {
  getComponentPath(componentName) {
    const link = this.$router.resolve({
      name: componentName,
    })
    console.log('link:', link)
    return link.route.path
  }
}
</script>
