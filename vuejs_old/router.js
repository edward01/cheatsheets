const router = new Router({
  // mode: 'history',
  routes: [
    // {     // this is needed if mode is 'history'
    //   path: '*',
    //   component: NotFoundComponent
    // }
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: function () {
        return import( /* webpackChunkName: " about" */ './views/About.vue')
      }
    }
  ]
})

// Append document title with "name"
router.afterEach(route => {
  let appSubtitle = toTitleCase(route.name)
  // if (route.meta.appTitle) appSubtitle = route.meta.appTitle
  if (route.name != 'home') document.title = `${appSubtitle} | ${title}`
})

export default router
