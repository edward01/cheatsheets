// source: https://github.com/Code-Pop/real-world-vue
import EventList from './views/EventList.vue'

export default new Router({
  routes: [
    {
      path: '/',
      name: 'event-list',
      component: EventList,
    },
    {
      path: '/event/create',
      name: 'event-create',
      component: EventCreate,
    },
    {
      path: '/event/:id',
      name: 'event-show',
      component: EventShow,
      props: true,
    },
  ]
})
