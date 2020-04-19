import Vue from 'vue'

Vue.filter('capitalize', value => {
  if (!value) return ''
  value = value.toString()
  return value.charAt(0).toUpperCase() + value.slice(1)
})

Vue.filter('cutText', (value, length, suffix) => {
  if (value.length > length) {
    return value.substring(0, length) + suffix
  } else {
    return value
  }
})

Vue.filter('singularize', value => {
  if (!value) return ''
  value = value.toString()
  if (value.slice(-3) == 'ies')
    return value.replace(/([A-Z])/g, ' $1').trim().slice(0, -3) + 'y'
  else if (value.slice(-1) == 's')
    return value.replace(/([A-Z])/g, ' $1').trim().slice(0, -1)
  return value
})

Vue.filter('roundTo7', value => {
  return +(Math.round(value + "e+7")  + "e-7")
})

// Vue.filter("numberToUSD", value => {
//   return value ? `$${value.toLocaleString("en-US")}` : "$0.0";
// });
