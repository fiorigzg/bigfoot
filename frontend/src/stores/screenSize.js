import { defineStore } from "pinia";


export const useScreenSize = defineStore("screenSize", {
  state: () => ({
    width: window.innerWidth > 750 ? window.innerWidth * 0.5 : window.innerWidth * 0.9,
  }),
  getters: {
    getWidth: (state) => state.width,
  },
  actions: {
    setWidth(width) {
      this.width = width;
    },
  },
});