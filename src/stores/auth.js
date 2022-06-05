import { writable } from 'svelte/store'

export const authenticated = writable(true)
export const jwt = writable('')