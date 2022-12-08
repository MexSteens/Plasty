import Vue from 'vue'
import axios from 'axios'

const resourceURL = 'complaint'

// export const state = () => ({
// })

export const getters = {
    complaintRead: state => {
        return state.complaint
    }
}

export const mutations = {
    set(state, data) {
        Vue.set(state.complaint, data.id, data)
    },
    unset(state, id) {
        Vue.delete(state.complaint, id)
    }
}


export const actions = {
    complaintRead({ commit }) {
        // Send get request to the backend.
        axios.get(
            resourceURL
        ).then(response => {
            // If request is successful then loop every item in the retrieved list
            // and add it to the state.
            response.data.forEach(item => {
                commit('set', item)
            })
        }).catch(error => {
            console.error(error)
        })
    },
    complaintGet({ commit }, { id }) {
        // Send get request to the backend.
        axios.get(
            `${resourceURL}/${id}`
        ).then(response => {
            // If request is successful then add the item to the state.
            commit('set', response.data)
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