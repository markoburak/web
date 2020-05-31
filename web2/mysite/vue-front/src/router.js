import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
    mode: 'history',
    routes: [{
            path: '/',
            component: () =>
                import ('@/views/Home.vue')
        },
        {
            path: '/contact',
            component: () =>
                import ('@/views/Contacts.vue')
        },
        {
            path: '/login',
            component: () =>
                import ('@/views/Login.vue')
        },
        {
            path: '/signup',
            component: () =>
                import ('@/views/Registration.vue')
        },
        {
            path: '/cart/:id',
            component: () =>
                import ('@/views/CartItem.vue')
        }
    ]
})