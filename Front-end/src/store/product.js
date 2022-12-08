import Vue from 'vue'
import axios from 'axios'

const resourceURL = 'product'

// export const state = () => ({
// })

export const getters = {
    productRead: state => {
        return state.product
    }
}

export const mutations = {
    productSet(state, data) {
        Vue.set(state.product, data.id, data)
    },
    productUnset(state, id) {
        Vue.delete(state.product, id)
    }
}


export const actions = {
    productRead({ commit }) {
        // Send get request to the backend.
        axios.get(
            resourceURL
        ).then(response => {
            // If request is successful then loop every item in the retrieved list
            // and add it to the state.
            response.data.forEach(item => {
                commit('productSet', item)
            })
        }).catch(error => {
            console.error(error)
        })
    },
    productGet({ commit }, { id }) {
        // Send get request to the backend.
        axios.get(
            `${resourceURL}/${id}`
        ).then(response => {
            // If request is successful then add the item to the state.
            commit('productSet', response.data)
        }).catch(error => {
            console.error(error)
        })
    }
}

export default {
    actions,
    mutations,
    getters
}
