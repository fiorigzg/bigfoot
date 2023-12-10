import { defineStore } from "pinia";


export const useTableDescription = defineStore("table", {
  state: () => ({
    describeParam: "index",
  }),
  getters: {
    getDescribeParam: (state) => state.describeParam,
  },
  actions: {
    setDescribeParam(describeParam) {
      this.describeParam = describeParam;
    },
  },
});