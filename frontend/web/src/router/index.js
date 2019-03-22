import Vue from 'vue'
import Router from 'vue-router'
import Map from '@/components/TreeMap'
import Municipalities from '@/components/Municipalities'
import Cities from '@/components/Cities'
import Parks from '@/components/Parks'
import Residents from '@/components/Residents'
import Transactions from '@/components/Transactions'
import Civic from '@/components/Civic'
import Index from '@/components/Index'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/map',
      name: 'TreeMap',
      component: Map
    },
    {
      path: '/map/:resident',
      name: 'TreeMapResident',
      component: Map
    },
    {
      path: '/map/tree/:id',
      name: 'TreeMapSelectTree',
      component: Map
    },
    {
      path: '/',
      name: 'Index',
      component: Index
    },
    {
      path: '/municipalities',
      name: 'Municipalities',
      component: Municipalities
    },
    {
      path: '/parks',
      name: 'Parks',
      component: Parks
    },
    {
      path: '/cities',
      name: 'Cities',
      component: Cities
    },
    {
      path: '/civic',
      name: 'Civic',
      component: Civic
    },
    {
      path: '/residents',
      name: 'Residents',
      component: Residents
    },
    {
      path: '/transactions',
      name: 'Transactions',
      component: Transactions
    }
  ]
})
