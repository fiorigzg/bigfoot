import { defineStore } from "pinia";


export const useBoxplotChoose = defineStore("boxplot-choose", {
  state: () => ({
    boxplotParam: "temperature_mid",
  }),
  getters: {
    getBoxplotParam: (state) => state.boxplotParam,
  },
  actions: {
    setBoxplotParam(boxplotParam) {
      this.boxplotParam = boxplotParam;
    },
  },
});