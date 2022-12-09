import Vue from 'vue'
import axios from 'axios'

const resourceURL = 'company'

// const state = () => ({
// })

const getters = {
    companyRead: state => {
        return state.company
    }
}

const mutations = {
    companySet(state, data) {
        Vue.set(state.company, data.id, data)
    },
    companyUnset(state, id) {
        Vue.delete(state.company, id)
    }
}
axios.defaults.baseURL = 'http://localhost:5000/api/' //'http://localhost:5000/api/'

const actions = {
    companyRead({ commit }) {
        // Send get request to the backend.
        axios.get(
            resourceURL
        ).then(response => {
            // If request is successful then loop every item in the retrieved list
            // and add it to the state.
            response.data.forEach(item => {
                commit('companySet', item)
            })
        }).catch(error => {
            console.error(error)
        })
    },
    companyGet({ commit }, { id }) {
        // Send get request to the backend.
        axios.get(
            `${resourceURL}/${id}`
        ).then(response => {
            // If request is successful then add the item to the state.
            commit('companySet', response.data)
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
